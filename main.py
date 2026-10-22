import sys
import time
from pathlib import Path

import eel
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

eel.init("web")

INITIAL_PAGE_PATH = "game.html"
WATCHED_EXTENSIONS = {".html", ".css", ".js"}

@eel.expose
def minimal_setup_check():
    print("Minimal check OK.")

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.handle_change(event)

    def on_created(self, event):
        self.handle_change(event)

    def handle_change(self, event):
        if event.is_directory:
            return

        path = Path(event.src_path)

        if path.suffix.lower() not in WATCHED_EXTENSIONS:
            return

        print(f"File changed: {path}")

        time.sleep(0.3)

        try:
            eel.reload_page()()
            print("Reload command sent.")
        except Exception as error:
            print(f"Reload failed: {error}")


def on_window_close(page, websockets):
    if not websockets:
        sys.exit(0)


observer = Observer()
observer.schedule(
    FileChangeHandler(),
    path="web",
    recursive=True,
)
observer.start()

try:
    eel.start(
        INITIAL_PAGE_PATH,
        mode="chrome",
        cmdline_args=[
            "--auto-open-devtools-for-tabs",
            "--user-data-dir=./.eel_profile",
        ],
        close_callback=on_window_close
        )

finally:
    observer.stop()
    observer.join()