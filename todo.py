import os

# Define the file name for persistence
TODO_FILE = "todo_list.txt"

def load_tasks():
    """Reads tasks from the file and returns them as a list."""
    tasks = []
    # Check if the file exists. If not, return an empty list.
    if not os.path.exists(TODO_FILE):
        return tasks

    try:
        # [span_0](start_span)Use 'with' statement (context manager) for clean file handling[span_0](end_span)
        with open(TODO_FILE, 'r') as file:
            # [span_1](start_span)Loop through the file line by line[span_1](end_span)
            for line in file:
                # [span_2](start_span)Use .strip() to remove leading/trailing whitespace and the newline character[span_2](end_span)
                task = line.strip() 
                if task: # Only add non-empty lines
                    tasks.append(task)
    except IOError:
        print(f"Error reading file: {TODO_FILE}")
    return tasks

def save_tasks(tasks):
    """Writes the current list of tasks back to the file."""
    try:
        # 'w' mode opens the file for writing. [span_3](start_span)It truncates (clears) the file first[span_3](end_span).
        with open(TODO_FILE, 'w') as file:
            for task in tasks:
                # Add a newline character after each task for proper formatting
                file.write(task + '\n')
    except IOError:
        print(f"Error writing to file: {TODO_FILE}")

def view_tasks(tasks):
    """Displays all current tasks with their index."""
    if not tasks:
        print("\n🎉 Your to-do list is empty! 🎉")
        return
    
    print("\n--- Current To-Do List ---")
    # Loop through the list using enumerate to get both index and task
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("--------------------------")

def add_task(tasks):
    """Prompts the user for a task and adds it to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        # [span_4](start_span)append() adds the item to the end of the list[span_4](end_span)
        tasks.append(task) 
        save_tasks(tasks)
        print(f"✅ Task added: '{task}'")
    else:
        print("❌ Task cannot be empty.")

def remove_task(tasks):
    """Prompts the user for a task index and removes it."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        # Get user input and convert it to an integer index
        task_num = int(input("Enter the number of the task to remove: "))
        
        # Lists are 0-indexed, so we subtract 1 from the user-provided number
        if 1 <= task_num <= len(tasks):
            # [span_5](start_span)Use pop() to remove the element at the specified index[span_5](end_span)
            removed_task = tasks.pop(task_num - 1) 
            save_tasks(tasks)
            print(f"🗑️ Task removed: '{removed_task}'")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    except IndexError:
        # This is a fallback, but the 'if' condition above should prevent it
        print("❌ Task number is out of range.") 

def main():
    """Main function to run the CLI application loop."""
    tasks = load_tasks()
    
    while True:
        print("\n*** To-Do List Manager ***")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("👋 Saving and exiting. Goodbye!")
            break
        else:
            print("🛑 Invalid choice. Please select 1, 2, 3, or 4.")

# Standard practice to run the main function when the script is executed
if __name__ == "__main__":
    main()