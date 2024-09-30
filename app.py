def display_todos(todos):
    if not todos:
        print("Your to do list is empty")
    else:
        print("Your to do list:")
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo}")

def add_todo(todos):
    todo = input("Enter a new to-do item: ")
    todos.append(todo)
    print(f"Added: '{todo}'")

def remove_todo(todos):
    display_todos(todos)
    try:
        index = int(input("Enter the number of to-do to remove:")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print (f"Removed: '{removed}'")
        else:
            print ("Invalid number")
    except ValueError:
        print("Please enter a valid number.")
    
def main():
    todos = []
    while True:
        print(f"To-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add To-Do")
        print("3. Remove To-Do")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
