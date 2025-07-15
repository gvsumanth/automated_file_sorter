import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import runpy

import logging

logging.basicConfig(
    filename="all_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - WTHDOG FILE - %(message)s"
)
logging.info("Watchdog is watching")

# Define your path
WATCH_PATH = "C:/Users/Admin/Documents/projects/python projects/automatic file sorter/files"
SORTER_PATH = "file_sorter.py"

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            logging.info(f"We've got a folder named: {os.path.basename(event.src_path)}")
            return

        logging.info(f"New file detected: {os.path.basename(event.src_path)}")
        logging.info("Running file_sorter.py to sort the file")

        try:
            runpy.run_path(SORTER_PATH)
            logging.info(f"the file {os.path.basename(event.src_path)} is sorted")
        except Exception as e:
            logging.info(f"❌ Error while running file_sorter: {e}")

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=False)

    observer.start()
    logging.info(f"Watching folder: {WATCH_PATH}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Watchdog Stopped")
    observer.join()
