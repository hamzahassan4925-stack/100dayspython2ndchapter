#file io
# Simple To-Do List Application in Python

def show_menu():
    print("\n" + "=" * 30)
    print("       TO-DO LIST APP       ")
    print("=" * 30)
    print("1. View Tasks (Tasks dekhein)")
    print("2. Add Task (Naya task shamil karein)")
    print("3. Remove Task (Task delete karein)")
    print("4. Exit (Bahir niklein)")
    print("=" * 30)

def todo_app():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Apna choice enter karein (1-4): ")
        
        if choice == '1':
            if not tasks:
                print("\nAapki to-do list abhi khaali hai!")
            else:
                print("\n--- Aapke Tasks ---")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            new_task = input("\nNaya task enter karein: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' successfully add ho gaya hai!")
            else:
                print("Task khaali nahi ho sakta!")
                
        elif choice == '3':
            if not tasks:
                print("\nDelete karne ke liye koi task nahi hai.")
            else:
                print("\n--- Aapke Tasks ---")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
                try:
                    task_num = int(input("\nKonsa task remove karna hai uska number dein: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"'{removed}' successfully remove ho gaya hai!")
                    else:
                        print("Ghalat number enter kiya hai!")
                except ValueError:
                    print("Kripya ek valid number enter karein!")
                    
        elif choice == '4':
            print("\nProgram band ho raha hai. Allah Hafiz!")
            break
        else:
            print("\nGhalat choice! Kripya 1 se 4 ke darmiyaan number enter karein.")

# Program yahan se run hona shuru hoga
if __name__ == "__main__":
    todo_app()







