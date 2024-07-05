from nada_dsl import *

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(name=task_name))

    def view_tasks(self):
        return [task.name for task in self.tasks]

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def clear_tasks(self):
        self.tasks = []

class Party:
    def __init__(self, name):
        self.name = name

class Input:
    def __init__(self, name, party):
        self.name = name
        self.party = party

class SecretInteger:
    def __init__(self, input_obj):
        self.input_obj = input_obj

    def reveal(self):
        return int(input(f"Enter secret integer for {self.input_obj.name}: "))

class Output:
    def __init__(self, result, output_name, party):
        self.result = result
        self.output_name = output_name
        self.party = party

def nada_main():
    party1 = Party(name="Party1")

    # Create a TodoList instance
    todo_list = TodoList()

    while True:
        print("\n=== Nada To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
            print(f"Task '{task_name}' added.")

        elif choice == '2':
            tasks = todo_list.view_tasks()
            if tasks:
                print("Tasks:")
                for idx, task in enumerate(tasks):
                    print(f"{idx + 1}. {task}")
            else:
                print("No tasks.")

        elif choice == '3':
            if todo_list.tasks:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_completed(task_index)
                print(f"Task {task_index + 1} marked as completed.")
            else:
                print("No tasks to mark as completed.")

        elif choice == '4':
            todo_list.clear_tasks()
            print("All tasks cleared.")

        elif choice == '5':
            print("Exiting Nada To-Do List.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    return [
        Output(None, "todo_list_output", party1)
    ]

# Entry point
if __name__ == "__main__":
    nada_main()
