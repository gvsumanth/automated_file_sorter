import os
import runpy
import subprocess
import threading
import logging

import tkinter as tk

watchdog_process = None

logging.basicConfig(
    filename="all_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - APP    FILE - %(message)s"
)

logging.info("App Started")

path = "C:/Users/Admin/Documents/projects/python projects/automatic file sorter/files"


def log(message):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"[INFO] {message}\n")
    output_text.see(tk.END)
    output_text.config(state=tk.DISABLED)

def run_sorter():
    subprocess.call(["python", "file_sorter.py"])
    log("Sorter ran.")

def run_reverter():
    subprocess.call(["python", "revert.py"])
    log("Reverter ran.")

def start_watchdog():
    global watchdog_process
    if watchdog_process is None or watchdog_process.poll() is not None:
        watchdog_process = subprocess.Popen(["python", "watch_dog.py"])
        log("Watchdog started.")
    else:
        log("Watchdog already running.")

def stop_watchdog():
    global watchdog_process
    if watchdog_process and watchdog_process.poll() is None:
        watchdog_process.terminate()
        log("Watchdog stopped.")
    else:
        log("Watchdog is not running.")

def run_watchdog():
    runpy.run_path("watch_dog.py", run_name="__main__")

def run_watchdog_thread():
    t = threading.Thread(target=run_watchdog, daemon=True)
    t.start
    print("Watchdog started in background")

# run_revert()
# run_sorter()
# run_display()
# run_watchdog()
# run_watchdog_thread()

root = tk.Tk()
root.title("File Sorter Controller")
root.geometry("300x250")

tk.Button(root, text="Start Watchdog", width=25, command=lambda: threading.Thread(target=start_watchdog).start()).pack(pady=5)
tk.Button(root, text="Stop Watchdog", width=25, command=stop_watchdog).pack(pady=5)
tk.Button(root, text="Run Sorter", width=25, command=run_sorter).pack(pady=5)
tk.Button(root, text="Run Reverter", width=25, command=run_reverter).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)


output_text = tk.Text(root, height = 8, state = tk.DISABLED, bg = "#000000", fg = "#00FF00", font = ("Consolas", 10))
output_text.pack(fill=tk.BOTH, padx=10, pady=10)

root.mainloop()