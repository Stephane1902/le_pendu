import sys
import eel
from src.game import choose_random_word

eel.init("gui")

INITIAL_PAGE_PATH = "main.html"

@eel.expose
def minimal_setup_check():
    print("Minimal check OK.")

@eel.expose
def page_ready():
    pass

if __name__ == "__main__":
    eel.start(
        INITIAL_PAGE_PATH,
        mode="chrome",
        # For dev (open devtools)
        # cmdline_args=[
        #     "--auto-open-devtools-for-tabs",
        #     "--user-data-dir=./.eel_profile",
        # ],
        shutdown_delay=5.0,
    )