# toDoApp.py
tasks = []  
completed = []

def addTask(task, priority="Medium"):
    """Add a new task to the list with priority"""
    tasks.append({"task": task, "priority": priority})
    print("-------------------------------")
    print("           Task added!")
    print("-------------------------------\n")


def showTasks():
    """Display all tasks with priorities"""
    if len(tasks) == 0:
        print("No tasks yet. Try adding some!\n\n")
    else:
        print("\n===============================")
        print("Your Tasks:")
        print("-------------------------------")
        for i in range(len(tasks)):
            task_item = tasks[i]
            priority_display = f"[{task_item['priority']}]"
            print(f"{i + 1}. {priority_display} {task_item['task']}")
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
    """Clear all tasks after user confirmation"""
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
    """Search tasks by keyword and display matches with priorities"""
    found = [task for task in tasks if keyword.lower() in task['task'].lower()]
    if found:
        print("\n===============================")
        print(" Search results:")
        print("-------------------------------")
        for i, task_item in enumerate(found, 1):
            priority_display = f"[{task_item['priority']}]"
            print(f"- {priority_display} {task_item['task']}")
        print("-------------------------------\n")
    else:
        print("No matching tasks found.\n\n")


def markTaskCompleted(tasknumber):
    """Mark a task as completed by its number"""
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid Task Number.\n\n")
    else:
        # Move task from tasks to completed
        completed_task = tasks.pop(tasknumber - 1)
        completed.append(completed_task)
        saveTasks()
        print("-------------------------------")
        print("      Task marked as done!")
        print("-------------------------------")


def showCompletedTasks():
    """Display all completed tasks"""
    if len(completed) == 0:
        print("No completed tasks yet.\n\n")
    else:
        print("\n===============================")
        print("Completed Tasks:")
        print("-------------------------------")
        for i in range(len(completed)):
            task_item = completed[i]
            priority_display = f"[{task_item['priority']}]"
            print(f"{i + 1}. [X] {priority_display} {task_item['task']}")
        print("-------------------------------\n")


def saveTasks():
    """Save tasks to tasks.txt file with priorities"""
    with open("tasks.txt", "w") as file:
        for task_item in tasks:
            file.write(f"{task_item['task']}|{task_item['priority']}\n")
    
    # Save completed tasks to a separate file
    with open("completed_tasks.txt", "w") as file:
        for task_item in completed:
            file.write(f"{task_item['task']}|{task_item['priority']}\n")


def loadTasks():
    """Load tasks from tasks.txt file with priorities"""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    task, priority = parts
                    tasks.append({"task": task, "priority": priority})
                elif len(parts) == 1:
                    # Handle old format without priorities
                    tasks.append({"task": parts[0], "priority": "Medium"})
    except FileNotFoundError:
        # If file doesn't exist yet, ignore
        pass
    
    # Load completed tasks
    try:
        with open("completed_tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    task, priority = parts
                    completed.append({"task": task, "priority": priority})
                elif len(parts) == 1:
                    # Handle old format without priorities
                    completed.append({"task": parts[0], "priority": "Medium"})
    except FileNotFoundError:
        # If file doesn't exist yet, ignore
        pass


def exportTasks():
    """Export tasks to a custom file with priorities"""
    filename = input("Enter filename to export to: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w") as file:
            for task_item in tasks:
                file.write(f"{task_item['task']}|{task_item['priority']}\n")
        print(f"Tasks exported to {filename}\n")
    except Exception as e:
        print(f"Error exporting tasks: {e}\n")


def importTasks():
    """Import tasks from a custom file with priorities"""
    filename = input("Enter filename to import from: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "r") as file:
            imported_count = 0
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    task, priority = parts
                    if task:  # Only add non-empty lines
                        tasks.append({"task": task, "priority": priority})
                        imported_count += 1
                elif len(parts) == 1 and parts[0]:
                    # Handle files without priorities
                    tasks.append({"task": parts[0], "priority": "Medium"})
                    imported_count += 1
        saveTasks()  # Save the updated tasks list
        print(f"Imported {imported_count} tasks from {filename}\n")
    except FileNotFoundError:
        print(f"File {filename} not found!\n")
    except Exception as e:
        print(f"Error importing tasks: {e}\n")


def getPriorityInput():
    """Get priority input from user with validation"""
    while True:
        print("Priority options: [1] High, [2] Medium, [3] Low")
        priority_choice = input("Enter priority (1-3, default 2): ").strip()
        
        if priority_choice == "1" or priority_choice.lower() == "high":
            return "High"
        elif priority_choice == "2" or priority_choice.lower() == "medium" or priority_choice == "":
            return "Medium"
        elif priority_choice == "3" or priority_choice.lower() == "low":
            return "Low"
        else:
            print("Invalid priority choice. Please enter 1, 2, or 3.")


def main():
    loadTasks()  # Load saved tasks at startup

    while True:
        print("\n===============================")
        print("           TO DO APP")
        print("===============================")
        print(f"  Pending Tasks: {len(tasks)}")
        print(f"  Completed Tasks: {len(completed)}")
        
        # Count tasks by priority
        high_priority = len([t for t in tasks if t['priority'] == 'High'])
        medium_priority = len([t for t in tasks if t['priority'] == 'Medium'])
        low_priority = len([t for t in tasks if t['priority'] == 'Low'])
        
        print(f"  High Priority: {high_priority}")
        print(f"  Medium Priority: {medium_priority}")
        print(f"  Low Priority: {low_priority}")
        print("-------------------------------")
        print(" [1] Add Task")
        print(" [2] Show Pending Tasks")
        print(" [3] Remove Task")
        print(" [4] Mark Task as Completed")
        print(" [5] Show Completed Tasks")
        print(" [6] Clear All Tasks")
        print(" [7] Search Tasks")
        print(" [8] Export Tasks")
        print(" [9] Import Tasks")
        print(" [0] Exit")
        print("-------------------------------")
        choice = input("Enter choice: ")

        if choice == "1":
            t = input("Enter task: ")
            priority = getPriorityInput()
            addTask(t, priority)
            saveTasks()

        elif choice == "2":
            showTasks()  # no need to save here

        elif choice == "3":
            showTasks() # Show tasks before asking which to remove
            n = int(input("Enter task # to remove: "))
            removeTask(n)
            saveTasks()

        elif choice == "4":
            showTasks() # Show tasks before asking which to mark as completed
            n = int(input("Enter task # to mark as completed: "))
            markTaskCompleted(n)

        elif choice == "5":
            showCompletedTasks()

        elif choice == "6":
            clearAllTasks()
            saveTasks()
        
        elif choice == "7":
            keyword = input("Enter keyword to search: ")
            searchTasks(keyword)

        elif choice == "8":
            exportTasks()

        elif choice == "9":
            importTasks()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Wrong choice! Please enter a number from 0-9.")

if __name__ == "__main__":
    main()
