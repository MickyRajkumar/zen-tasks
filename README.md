# Task Reminder CLI

A simple task reminder application for Windows and Linux terminals using SQLite.

## 🚀 Features

- Add, delete, and complete tasks
- Schedule tasks with due dates
- View tasks based on time filters (today, yesterday, this week, etc.)
- Automatically lists pending tasks when you open the terminal

## 🛠 Installation

### 🔹 Windows Installation

1. **Clone the [repository](https://github.com/MickyRajkumar/task-manager):**

   ```sh
   git clone https://github.com/MickyRajkumar/task-manager.git
   cd task-reminder-cli
   ```

2. **Ensure Python is installed:**

   ```sh
   python --version
   ```

   If Python is not installed, download it from [python.org](https://www.python.org/downloads/).


3. \*\*Make the script globally accessible:\*\*e:\*\*

   - Create a `task.bat` file in the project directory:
     ```bat
     @echo off
     python "%~dp0task" %*
     ```
   - Add the project folder to the system `PATH`:(change path D:\project\task-manager to your path)
     ```powershell
     [System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";D:\project\task-manager", [System.EnvironmentVariableTarget]::User)
     ```
   - Restart the terminal and test:
     ```sh
     task -h
     ```

### 🔹 Linux Installation

1. **Clone the [repository](https://github.com/MickyRajkumar/task-manager):**

   ```sh
   git clone https://github.com/MickyRajkumar/task-manager.git
   cd task-reminder-cli
   ```

2. **Ensure Python is installed:**

   ```sh
   python3 --version
   ```

   If not installed, run:

   ```sh
   sudo apt update && sudo apt install python3
   ```

3. **Make the script executable and accessible:**

   ```sh
   chmod +x task
   sudo ln -s $(pwd)/task /usr/local/bin/task
   ```

4. **Test the command:**

   ```sh
   task -h
   ```

## 📌 Usage

### Add a Task

```sh
task add "Finish project report" --due "2025-02-08 14:00"
```

### List Tasks

```sh
task list
```

### Mark a Task as Completed

```sh
task done 1
```

### Delete a Task

```sh
task delete 1
```

### View Tasks by Time Filter

```sh
task list --today  # View tasks created today
task list --week   # View tasks from this week
task list --month  # View tasks from this month
```

## 🔧 Reset Database

To delete all tasks and reset the database, run:

```sh
task reset
```

## ✅ Contributing

Feel free to contribute by submitting pull requests or reporting issues!

## 📝 License

MIT License © 2025 Micky Rajkumar


