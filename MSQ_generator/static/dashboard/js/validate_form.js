document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("editingForm");
    const completeButton = document.getElementById("completeButton");
    const textareas = form.querySelectorAll("textarea");

    function validateForm() {
        let allFilled = true;
        textareas.forEach(textarea => {
            if (textarea.value.trim() === "") {
                allFilled = false;
            }
        });
        completeButton.disabled = !allFilled;
    }

    textareas.forEach(textarea => {
        textarea.addEventListener("input", validateForm);
    });

    validateForm(); // Initial check
});
