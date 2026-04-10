// ---------------- PAGE LOAD ----------------
document.addEventListener("DOMContentLoaded", function () {
    console.log("Resume Builder Loaded");

    addAnimations();
    setupFormValidation();
    setupLivePreview();
});

// ---------------- DOWNLOAD PDF ----------------
function downloadPDF() {
    window.print(); // simple browser print
}

// ---------------- FORM VALIDATION ----------------
function setupFormValidation() {
    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", function (e) {
        let inputs = form.querySelectorAll("input, textarea");
        let valid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                input.style.border = "2px solid red";
                valid = false;
            } else {
                input.style.border = "1px solid #ccc";
            }
        });

        if (!valid) {
            e.preventDefault();
            alert("Please fill all fields!");
        }
    });
}

// ---------------- LIVE PREVIEW (BASIC) ----------------
function setupLivePreview() {
    const inputs = document.querySelectorAll("input, textarea");

    inputs.forEach(input => {
        input.addEventListener("input", function () {
            let previewField = document.getElementById(input.name);

            if (previewField) {
                previewField.innerText = input.value;
            }
        });
    });
}

// ---------------- CARD HOVER EFFECT ----------------
function addAnimations() {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "scale(1.05)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)";
        });
    });
}

// ---------------- TEMPLATE SWITCH CONFIRM ----------------
function confirmTemplate(templateName) {
    let confirmAction = confirm("Use this template?");
    if (confirmAction) {
        window.location.href = "/template/" + templateName;
    }
}

// ---------------- SMOOTH SCROLL ----------------
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}