// Minimal setup checkup
document.getElementById("test-btn")?.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("Minimal check OK");
    eel.minimal_setup_check()();
    window.location.href = e.target.href;
});

eel.expose(reload_page);
function reload_page() {
    console.log("Reload signal received");
    window.location.reload();
}
