document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggleNav");
    const navList = document.getElementById("navList");

    toggleButton.addEventListener("click", function() {
        navList.classList.toggle("collapsed");
    });
});