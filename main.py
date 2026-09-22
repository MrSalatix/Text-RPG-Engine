def menu():
    print("======================")
    print("      TEXT RPG        ")
    print("======================")

    print("1. New Game")
    print("2. Load Game")
    print("3. Exit")

def choice_menu_option():
    option = input("Выберите опцию: ")
    if option == "1":
        print("This don't work yet:(")
        return False
    elif option == "2":
        print("This don't work yet:(")
        return False
    elif option == "3":
        print("Goodbye")
        return True
    else:
        print("Please enter a valid option")
        return False

while True:
    menu()
    should_exit = choice_menu_option()
    if should_exit:
        break



