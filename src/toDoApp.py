# toDoApp.py

tasks = []


def addTask(task):
    """Add a new task to the list"""
    tasks.append(task)
    print("Task added!")


def showTasks():
    """Display all tasks"""
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def removeTask(tasknumber):
    """Remove a task by its number"""
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid Task Number.")
    else:
        removed = tasks.pop(tasknumber - 1)
        print(f"Task removed: {removed}")


def clearAllTasks():
    """Clear all tasks after user confirmation"""
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


def searchTasks(keyword):
    """Search tasks by keyword and display matches"""
    found = [task for task in tasks if keyword.lower() in task.lower()]
    if found:
        print("\nSearch results:")
        for i, task in enumerate(found, 1):
            print(f"{i}. {task}")
    else:
        print("No matching tasks found.")


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


def exportTasks():
    """Export tasks to a custom file"""
    filename = input("Enter filename to export to: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"Tasks exported to {filename}")
    except Exception as e:
        print(f"Error exporting tasks: {e}")


def importTasks():
    """Import tasks from a custom file"""
    filename = input("Enter filename to import from: ").strip()
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
        saveTasks()
        print(f"Imported {imported_count} tasks from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except Exception as e:
        print(f"Error importing tasks: {e}")


def main():
    loadTasks()  # Load saved tasks at startup

    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Clear All Tasks")
        print("5. Search Tasks")
        print("6. Export Tasks")
        print("7. Import Tasks")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                addTask(task)
                saveTasks()
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            showTasks()

        elif choice == "3":
            try:
                num = int(input("Enter task # to remove: ").strip())
                removeTask(num)
                saveTasks()
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            clearAllTasks()  # already saves inside the function

        elif choice == "5":
            keyword = input("Enter keyword to search: ").strip()
            searchTasks(keyword)

        elif choice == "6":
            exportTasks()

        elif choice == "7":
            importTasks()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Wrong choice! Please enter a number from 1-8.")


if __name__ == "__main__":
    main()
