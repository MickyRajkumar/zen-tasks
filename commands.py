import sqlite3
from config import DB_PATH
import random
from datetime import datetime, timedelta

GREETINGS = [
    "🌟 Welcome back! Ready to conquer the day? 🚀",
    "👋 Hello there! What’s on the agenda today? 📝",
    "🎯 New day, new goals! Let’s make it productive! 💪",
    "☕ Grab a coffee, take a deep breath, and let’s get started! 🌿",
    "🔄 Another day, another chance to achieve something great! 🌍"
]

NO_TASK_MESSAGES = [
    "🎉 No pending tasks! Time to relax! 😎",
    "🚀 All tasks completed! Maybe add some new goals? 📝",
    "🎯 You're all caught up! What's next on your list? 🤔",
    "🔥 No tasks left! Now's a great time to learn something new. 📚",
    "🏆 No tasks? You deserve a break! ☕"
]

def add_task(task, due_date=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        "INSERT INTO tasks (task, due_date) VALUES (?, ?)",
        (task, due_date),
    )
    conn.commit()
    conn.close()
    print("✅ Task added!")
    print("\n")

def list_tasks():
    conn = sqlite3.connect(DB_PATH)
    print("\n" + "=" * 50)
    print("📌 PENDING TASKS".center(50))
    print("=" * 50)
    
    print(random.choice(GREETINGS))
    c = conn.cursor()
    c.execute("SELECT id, task, due_date, created_at FROM tasks WHERE status = 'pending' ORDER BY created_at ASC")
    tasks = c.fetchall()
    conn.close()

    if not tasks:
        print(random.choice(NO_TASK_MESSAGES))
    else:
        print(f"{'ID':<5} {'TASK':<40} {'DUE DATE'}")
        print("-" * 60)
        for task in tasks:
            print(f"{task[0]:<5} {task[1]:<40} {task[2] if task[2] else 'No due date'}")
    print("\n")

def complete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print("✅ Task marked as completed!")
    print("\n")

def delete_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print("🗑 Task deleted!")
    print("\n")



def get_completed_tasks(filter_type="today"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = datetime.today().date()
    
    filters = {
        "today": f"DATE(completed_at) = '{today}'",
        "yesterday": f"DATE(completed_at) = '{today - timedelta(days=1)}'",
        "week": f"DATE(completed_at) >= '{today - timedelta(days=today.weekday())}'",
        "month": f"strftime('%Y-%m', completed_at) = '{today.strftime('%Y-%m')}'",
        "year": f"strftime('%Y', completed_at) = '{today.strftime('%Y')}'",
        "all": "1=1",
    }
    
    if filter_type not in filters:
        print("❌ Invalid filter! Use: today, yesterday, week, month, or year.")
        return
    
    print('filter_type:', filters[filter_type])
    query = f"""
        SELECT id, task, created_at, completed_at 
        FROM tasks 
        WHERE status = 'completed' AND {filters[filter_type]} 
        ORDER BY completed_at DESC
    """
    
    cursor.execute(query)
    tasks = cursor.fetchall()
    conn.close()
    
    print("\n" + "=" * 80)
    print(f"✅ TASKS COMPLETED {filter_type.upper()}".center(80))
    print("=" * 80)
    
    if not tasks:
        print("\n🎉 No completed tasks for this period!\n")
    else:
        for task in tasks:
            print(f"👉 {task[1]}   | 📅 Created: {task[2]} | ✅ Completed: {task[3]}")
    print("\n")

def reset_database():
    """Deletes all tasks and resets the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Drop the table if it exists
    c.execute("DROP TABLE IF EXISTS tasks")

    # Recreate the tasks table
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            due_date TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP DEFAULT NULL,
            status TEXT DEFAULT 'pending'
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database has been reset!")
    print("\n")