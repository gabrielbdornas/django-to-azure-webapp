document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener("focus", function() {
            this.style.borderColor = "#007bff";
        });

        input.addEventListener("blur", function() {
            this.style.borderColor = "#ccc";
        });
    });
});


