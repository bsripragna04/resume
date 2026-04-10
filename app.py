from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"

# Dummy database
users = {}

# ---------------- HOME ----------------
@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if username in users:
            return "User already exists!"

        users[username] = password
        return redirect(url_for('login'))

    return render_template('register.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return redirect(url_for('dashboard'))

        return "Invalid username or password!"

    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')

# ---------------- RESUME FORM ----------------
@app.route('/form', methods=['GET', 'POST'])
def form():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Store form data in session
        session['resume'] = request.form.to_dict()
        return redirect(url_for('select_template'))

    return render_template('form.html')

# ---------------- TEMPLATE SELECTION ----------------
@app.route('/select-template')
def select_template():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('template_select.html')

# ---------------- DYNAMIC TEMPLATE RENDER ----------------
@app.route('/template/<template_name>')
def render_template_page(template_name):
    if 'user' not in session:
        return redirect(url_for('login'))

    data = session.get('resume', {})

    # Prevent invalid template access
    allowed_templates = ['template1', 'template2', 'template3']
    if template_name not in allowed_templates:
        return "Template not found!"

    return render_template(f"{template_name}.html", data=data)

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)