document.addEventListener("DOMContentLoaded", function() {
    const audio = document.getElementById('click-sound');
    
    document.querySelectorAll("tbody tr").forEach(row => {
        row.addEventListener("click", function() {
            audio.play();
            const url = row.getAttribute("data-url");
            setTimeout(() => {
                window.location.href = url;
            }, 300); // Adjust the delay to match the duration of your sound effect
        });
    });
    
    document.getElementById("statusFilter").addEventListener("change", filterTable);
});

function filterTable() {
    const filter = document.getElementById("statusFilter").value.toLowerCase();
    const rows = document.querySelectorAll("tbody tr");

    rows.forEach(row => {
        const status = row.querySelector("td:last-child").textContent.toLowerCase();
        if (filter === "all" || status === filter) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}
