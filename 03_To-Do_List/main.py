# 3. To-Do List

tasks = []

# Load Tasks From File
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line:
                task_name, status = line.split(" | status: ", 1)

                tasks.append({
                    "task": task_name,
                    "status": status
                })

except FileNotFoundError:
    pass


# Main Program
while True:
    print("\n----- Welcome To To-Do List -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        # Add Task
        if choice == 1:
            task_name = input("Enter your task: ").strip().lower()

            if not task_name:
                print("Task cannot be empty.")
                continue

            tasks.append({
                "task": task_name,
                "status": "pending"
            })

            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(
                        f"{task['task']} | status: {task['status']}\n"
                    )

            print("Task Added Successfully!")

        # View Tasks
        elif choice == 2:
            if not tasks:
                print("No Tasks Found.")
            else:
                print("\n----- Your Tasks -----")

                for index, task in enumerate(tasks, start=1):
                    print(
                        f"{index}. {task['task']} | status: {task['status']}"
                    )

        # Update Task
        elif choice == 3:
            if not tasks:
                print("No Tasks Found.")
                continue

            for index, task in enumerate(tasks, start=1):
                print(
                    f"{index}. {task['task']} | status: {task['status']}"
                )

            task_number = int(input("\nEnter task number to update: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid Task Number.")
                continue

            print("\n1. Update Task Name")
            print("2. Update Task Status")

            update_choice = input("\nEnter your choice: ").strip()

            if update_choice == "1":
                new_name = input("\nEnter new task name: ").strip().lower()

                if not new_name:
                    print("Task name cannot be empty.")
                    continue

                tasks[task_number - 1]["task"] = new_name
                print("Task Name Updated Successfully!")

            elif update_choice == "2":
                print("\n1. Pending")
                print("2. Completed")

                status_choice = input("\nEnter your choice: ").strip()

                if status_choice == "1":
                    tasks[task_number - 1]["status"] = "pending"
                    print("Task Status Updated Successfully!")

                elif status_choice == "2":
                    tasks[task_number - 1]["status"] = "completed"
                    print("Task Status Updated Successfully!")

                else:
                    print("Invalid Status Choice.")
                    continue

            else:
                print("Invalid Choice.")
                continue

            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(
                        f"{task['task']} | status: {task['status']}\n"
                    )

        # Delete Task
        elif choice == 4:
            if not tasks:
                print("No Tasks Found.")
                continue

            for index, task in enumerate(tasks, start=1):
                print(
                    f"{index}. {task['task']} | status: {task['status']}"
                )

            task_number = int(input("\nEnter task number to delete: "))

            if task_number < 1 or task_number > len(tasks):
                print("Invalid Task Number.")
                continue

            deleted_task = tasks.pop(task_number - 1)

            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(
                        f"{task['task']} | status: {task['status']}\n"
                    )

            print(f"Task '{deleted_task['task']}' Deleted Successfully!")

        # Exit
        elif choice == 5:
            print("Thank You For Using To-Do List!")
            break

        # Invalid Choice
        else:
            print("Invalid Choice. Try Again.")

    except ValueError:
        print("Invalid Input. Please Enter a Valid Number.")
