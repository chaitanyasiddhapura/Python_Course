# Simple To-Do List Application

def show_menu():
    print("\n1. View To-Do List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

def view_list(todo_list):
    print("\nTo-Do List:")
    for idx, item in enumerate(todo_list, 1):
        print(f"{idx}. {item}")

def add_item(todo_list):
    item = input("Add item: ")
    todo_list.append(item)
    print(f"'{item}' added.")

def remove_item(todo_list):
    view_list(todo_list)
    idx = int(input("Remove item number: ")) - 1
    if 0 <= idx < len(todo_list):
        removed = todo_list.pop(idx)
        print(f"'{removed}' removed.")
    else:
        print("Invalid item number.")

def main():
    todo_list = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
