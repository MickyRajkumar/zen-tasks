import os

db_folder = os.path.join(os.getenv("APPDATA"), "TaskCLI")
os.makedirs(db_folder, exist_ok=True)
DB_PATH = os.path.join(db_folder, "task_reminder.db")
