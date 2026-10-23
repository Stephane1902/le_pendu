// Init Game
function whenEelReady(fn) {
    const check = () => {
        const ws = eel._websocket;
        if (ws && ws.readyState === WebSocket.OPEN) fn();
        else setTimeout(check, 50);
    };
    check();
}

window.addEventListener("load", () => {
    whenEelReady(async () => {
        try {
            await eel.page_ready()();
            const wordLength = await eel.choose_random_word()();
            drawWordPlaceholder(wordLength);
        } catch (err) {
            console.error("Init failed", err);
        }
    });
});

const drawWordPlaceholder = (wordLength) => {
    const wordToGuessEl = document.getElementById("word-to-guess");
    wordToGuessEl.innerHTML = ""; // avoid duplicate cases if init runs twice
    const lettersFragment = document.createDocumentFragment();

    for (let i = 0; i < wordLength; i++) {
        const el = document.createElement("span");
        el.textContent = "_";
        el.className = "case";
        lettersFragment.appendChild(el);
    }

    wordToGuessEl.appendChild(lettersFragment);
};

const HANGMAN_PARTS = [
    "hangman-head",
    "hangman-body",
    "hangman-left-arm",
    "hangman-right-arm",
    "hangman-left-leg",
    "hangman-right-leg",
];

document.querySelectorAll(".touche").forEach((touche) => {
    touche.addEventListener("click", async (e) => {
        const btn = e.currentTarget; // e.currentTarget is null after an await
        if (btn.disabled) return;

        try {
            const {
                wordToGuess,
                playedCharacter,
                roundIsSuccess,
                correctLocationsOfRound,
                errorsNOfGame,
                isEndOfGame,
                hasWon,
            } = await eel.play_user_move(btn.textContent)();

            if (roundIsSuccess) {
                document.querySelectorAll(".case").forEach((item, i) => {
                    if (correctLocationsOfRound.includes(i)) {
                        item.textContent = playedCharacter.toUpperCase();
                        item.style.color = "white";
                        item.style.backgroundColor = "green";
                    }
                });
            } else {
                document.getElementById("error-count").textContent =
                    errorsNOfGame;

                const part = HANGMAN_PARTS[errorsNOfGame - 1];
                if (part) {
                    document.getElementById(part).classList.remove("hidden");
                }
            }

            btn.style.backgroundColor = roundIsSuccess ? "green" : "red";
            btn.style.opacity = 0.5;
            btn.disabled = true;
            btn.style.cursor = "not-allowed";

            if (isEndOfGame) {
                document.querySelectorAll(".touche").forEach((b) => {
                    b.disabled = true;
                    b.style.cursor = "not-allowed";
                    b.style.opacity = 0.5;
                });

                if (hasWon) {
                    document
                        .getElementById("victory-message")
                        .classList.remove("hidden");
                } else {
                    document
                        .getElementById("defeat-message")
                        .classList.remove("hidden");

                    document.querySelectorAll(".case").forEach((el, i) => {
                        el.textContent = wordToGuess[i];
                        el.style.textTransform = "uppercase";
                    });
                }
            }
        } catch (err) {
            console.error("play_user_move failed", err);
        }
    });
});
