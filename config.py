import os
import sys

if sys.platform == "win32":
    db_folder = os.path.join(os.getenv("APPDATA"), "TaskCLI")
elif sys.platform == "linux":
    xdg_data_home = os.getenv("XDG_DATA_HOME")
    if xdg_data_home:
        db_folder = os.path.join(xdg_data_home, "TaskCLI")
    else:
        db_folder = os.path.join(os.path.expanduser("~"), ".local", "share", "TaskCLI")
else:
    db_folder = os.path.join(os.path.expanduser("~"), ".local", "share", "TaskCLI")

# Ensure the directory exists
os.makedirs(db_folder, exist_ok=True)

# Set the database path
DB_PATH = os.path.join(db_folder, "task_reminder.db")
