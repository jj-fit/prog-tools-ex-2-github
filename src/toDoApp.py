# toDoApp.py

tasks = []  

def addTask(task):
    tasks.append(task)
    print("Task added!")


def showTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])


def removeTask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid Task Number.")
    else:
        tasks.pop(tasknumber - 1)
        print("Task removed!")


def clearAllTasks():
    """
    Clear all tasks after user confirmation.
    """
    if len(tasks) == 0:
        print("No tasks to clear.")
        return
    answer = input("Are you sure you want to CLEAR ALL tasks? Type 'yes' to confirm: ").strip().lower()
    if answer == "yes":
        tasks.clear()
        saveTasks()
        print("All tasks cleared.")
    else:
        print("Clear cancelled.")


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
        print(f"Tasks exported to {filename}")
    except Exception as e:
        print(f"Error exporting tasks: {e}")


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
        print(f"Imported {imported_count} tasks from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except Exception as e:
        print(f"Error importing tasks: {e}")


def main():
    loadTasks()  # Load saved tasks at startup

    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Export Tasks")
        print("6. Import Tasks")
        print("7. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter task: ")
            addTask(t)
            saveTasks()

        elif ch == "2":
            showTasks()  # no need to save here

        elif ch == "3":
            n = int(input("Enter task # to remove: "))
            removeTask(n)
            saveTasks()

        elif ch == "4":
            clearAllTasks()
            saveTasks()

        elif ch == "5":
            exportTasks()

        elif ch == "6":
            importTasks()

        elif ch == "7":
            print("Goodbye!")
            break

        else:
            print("Wrong choice!")

main()
