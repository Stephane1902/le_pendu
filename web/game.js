document.querySelectorAll(".touche").forEach((touche) => {
    touche.addEventListener("click", () => {
        eel.play_round();
    });
});
