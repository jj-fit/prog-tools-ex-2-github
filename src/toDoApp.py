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


def main():
    loadTasks() # initialize the loadTask function to display saved tasks on the file

    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("Enter choice : ")

        if ch == "1":
            t = input("Enter task : ")
            addTask(t)
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
