# IntershipTask2
**To-Do List Manager – Task 2**

This project is developed for Task 2, implementing a simple and user-friendly Command Line To-Do Application in Python.
It stores tasks permanently in a text file and supports adding, viewing, and removing tasks.

**Overview**

The To-Do List Manager helps users maintain their daily tasks.
Features included:

✔ Add new tasks
✔ View all tasks
✔ Remove tasks by number
✔ Data stored permanently in todo_list.txt
✔ Beginner-friendly Python code
✔ Works fully in command-line (CLI)

**Technologies Used**

Python 3.x
File Handling (text file persistence)
Standard Library modules: os

**Project Structure**

todo-application/
│── todo.py
│── todo_list.txt   (auto created on first run)
│── README.md

**How to Run the Project**

1️⃣ Install Python
Make sure Python 3 is installed.

2️⃣ Save the code in a file named:
todo.py

3️⃣ Run the script using:
python todo.py

4️⃣ A menu will appear:
1. View Tasks
2. Add Task
3. Remove Task
4. Exit

**Features Explained**

🔹 1. Load Tasks
Reads all existing tasks from todo_list.txt.
If file does not exist, it creates an empty list.

🔹 2. Add Task
User enters a new task
Task gets added to list
It is saved permanently using save_tasks()

🔹 3. View Tasks
Shows a clean numbered list of all tasks.
Example:
1. Buy groceries
2. Finish assignment

🔹 4. Remove Task
Shows all tasks
User selects task number
Task is removed with pop()

🔹 5. File Persistence
All tasks are stored safely in a text file:
todo_list.txt

 **Sample Screenshot (CLI Output)**

*** To-Do List Manager ***
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Enter your choice (1-4):


