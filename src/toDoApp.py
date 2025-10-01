# toDoApp.py

tasks = []  
completed = []

def addTask(task):
    """Add a new task to the list"""
    tasks.append(task)
    print("-------------------------------")
    print("           Task added!")
    print("-------------------------------\n")


def showTasks():
    """Display all tasks"""
    if len(tasks) == 0:
        print("No tasks yet. Try adding some!\n\n")
    else:
        print("\n===============================")
        print("Your Tasks:")
        print("-------------------------------")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print("-------------------------------\n")


def removeTask(tasknumber):
    """Remove a task by its number"""
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid Task Number.\n\n")
    else:
        tasks.pop(tasknumber - 1)
        print("-------------------------------")
        print("           Task removed!")
        print("-------------------------------")


def clearAllTasks():
    """
    Clear all tasks after user confirmation.
    """
    if len(tasks) == 0:
        print("No tasks to clear.\n\n")
        return
    answer = input("Are you sure you want to CLEAR ALL tasks? Type 'yes' to confirm: ").strip().lower()
    if answer == "yes":
        tasks.clear()
        saveTasks()
        print("All tasks cleared.\n\n")
    else:
        print("Clear cancelled.\n\n")


def searchTasks(keyword):
    """Search tasks by keyword and display matches"""
    found = [task for task in tasks if keyword.lower() in task.lower()]
    if found:
        print("\n===============================")
        print(" Search results:")
        print("-------------------------------")
        for i, task in enumerate(found, 1):
            print("-", task)
        print("-------------------------------\n")
    else:
        print("No matching tasks found.\n\n")


def saveTasks():
    """Save tasks to tasks.txt file"""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def loadTasks():
    """Load tasks from tasks.txt file"""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        # If file doesn't exist yet, ignore
        pass


def exportTasks(): # Define export task function to be able to export the updated tasks.txt file
    """Export tasks to a custom file"""
    filename = input("Enter filename to export to: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"Tasks exported to {filename}\n")
    except Exception as e:
        print(f"Error exporting tasks: {e}\n")


def importTasks(): # Define import task function to be able to upload exisiting .txt file
    """Import tasks from a custom file"""
    filename = input("Enter filename to import from: ")
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "r") as file:
            imported_count = 0
            for line in file:
                task = line.strip()
                if task:  # Only add non-empty lines
                    tasks.append(task)
                    imported_count += 1
        saveTasks()  # Save the updated tasks list
        print(f"Imported {imported_count} tasks from {filename}\n")
    except FileNotFoundError:
        print(f"File {filename} not found!\n")
    except Exception as e:
        print(f"Error importing tasks: {e}\n")


def main():
    loadTasks()  # Load saved tasks at startup

    while True:
        print("\n===============================")
        print("           TO DO APP")
        print("===============================")
        print(f"  Total Tasks: {len(tasks)}")
        print("-------------------------------")
        print(" [1] Add Task")
        print(" [2] Show Tasks")
        print(" [3] Remove Task")
        print(" [4] Clear All Tasks")
        print(" [5] Search Tasks")
        print(" [6] Export Tasks")
        print(" [7] Import Tasks")
        print(" [8] Exit")
        print("-------------------------------")
        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter task: ")
            addTask(t)
            saveTasks()

        elif ch == "2":
            showTasks()  # no need to save here

        elif ch == "3":
            showTasks() # Show tasks before asking which to remove
            n = int(input("Enter task # to remove: "))
            removeTask(n)
            saveTasks()

        elif ch == "4":
            clearAllTasks()
            saveTasks()
        
        elif ch == "5":
            keyword = input("Enter keyword to search: ")
            searchTasks(keyword)

        elif ch == "6":
            exportTasks()

        elif ch == "7":
            importTasks()

        elif ch == "8":
            print("Exiting... Goodbye!\n\n")
            break

        else:
            print("Invalid choice. Try again.\n\n")

main()
