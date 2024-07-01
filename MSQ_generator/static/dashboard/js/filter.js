document.addEventListener("DOMContentLoaded", function() {
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
