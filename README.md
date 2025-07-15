# Smart File Watcher and Organizer

This is a Python-based automation tool that monitors a folder in real time and sorts newly added files into categorized directories based on their file types. It also includes functionality to revert the sorting and restore the original folder structure. A simple GUI built with Tkinter allows the user to control these functions with start, stop, and exit buttons.

## Features
```
- Real-time folder monitoring using `watchdog`
- Automatic sorting of files into categorized folders
- Revert function to move files back to the original folder
- GUI with buttons to control sorter, reverter, and watcher
- Logging of all actions and errors
```
## Technologies Used
```
- Python 3
- watchdog
- tkinter
- logging
- shutil, os
```
## Project Structure
```
project/
├── files/              # Folder being monitored
├── resources/              # Folder with various files
├── file_sorter.py           # Sorts files into folders
├── revert.py         # Reverts sorted files back
├── watch_dog.py         # Watches folder and triggers sorter
├── app.py              # GUI interface for user interaction
├── all_logs.log          # Logs actions taken by the sorter
└── README.md
```

You can edit this file to customize the sorting behavior.

## Installation

Install the required packages using pip:

```
pip install watchdog 
```

## Usage

### Run the GUI:

```
python app.py
```

### Or run scripts manually:

Start file monitoring:

```
python watch_dog.py
```

Sort files in the monitored folder:

```
python file_sorter.py
```

Revert the sorted files:

```
python revert.py
```

## Logging
```
Logs are saved in `all_logs.log` with timestamps for each operation and any warnings for unknown file types.
```
