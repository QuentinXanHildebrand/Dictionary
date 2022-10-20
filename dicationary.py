files = {}

def add_items():
    done = False
    while done == False:
        key = input("What do you want to add? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
        elif key != "done":
            value = input("How much is it $")
            print("Adding", value, key)
            files[key] = value          
        

def remove_items():
    done = False
    while done == False:
        key = input("What do you want to remove? Type 'done' to exit > ").lower()
        if key == "done":
            done = True
        elif key != "done":
            if key in files:
                print("Erasing", key)
                del files[key]
            else:
                print("your done, try again")

def print_items():
    for (key,value) in files.items():
        print("You have", value, key)

def main():
    go = 1
    while go == 1:
        print("Welcome to the Shopping list")
        print("What would you like to do?")
        choice = input("Add, View, Remove, Quit? ").lower()
        if choice == "add":
            add_items()
        elif choice == "view":
            print_items()
        elif choice == "remove":
            remove_items()
        elif choice == "quit":
            go = 0
            print("Good Bye!")
        else:
            print("Try again")
            
main()