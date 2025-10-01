# toDoApp.py

tasks = []  

def addTask(task, priority="Medium"):
    tasks.append({"task": task, "priority": priority})
    print("Task added!")


def showTasks():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        for i in range(len(tasks)):
            task = tasks[i]
            print(f"{i + 1}. {task['task']} [{task['priority']}]")


def removeTask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid Task Number.")
    else:
        tasks.pop(tasknumber - 1)
        print("Task removed!")


def get_valid_priority():
    """Helper function to get valid priority input"""
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            return priority
        else:
            print("Invalid priority! Please enter High, Medium, or Low.")


def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter choice : ")

        if ch == "1":
            t = input("Enter task : ")
            priority = get_valid_priority()
            addTask(t, priority)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("Enter task # to remove: "))
            removeTask(n)
        elif ch == "4":
            break
        else:
            print("Wrong choice!")


main()
