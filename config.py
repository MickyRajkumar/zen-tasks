import os
import sys

# Determine the appropriate data directory based on the OS
if sys.platform == "win32":
    # Windows: Use APPDATA
    db_folder = os.path.join(os.getenv("APPDATA"), "TaskCLI")
elif sys.platform == "linux":
    # Linux: Use XDG_DATA_HOME or fallback to ~/.local/share
    xdg_data_home = os.getenv("XDG_DATA_HOME")
    if xdg_data_home:
        db_folder = os.path.join(xdg_data_home, "TaskCLI")
    else:
        db_folder = os.path.join(os.path.expanduser("~"), ".local", "share", "TaskCLI")
else:
    # macOS or other Unix-like systems: Use ~/.local/share
    db_folder = os.path.join(os.path.expanduser("~"), ".local", "share", "TaskCLI")

# Ensure the directory exists
os.makedirs(db_folder, exist_ok=True)

# Set the database path
DB_PATH = os.path.join(db_folder, "task_reminder.db")
