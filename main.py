from character import Character

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
        new_game()
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

def character_name_choice():
    while True:
        character_name = input("Назовите персонажа: ")
        if character_name == "" or character_name.isspace() == True:
            continue
        else:
            break
    return character_name

def character_class_choice():
    print("Выберите класс персонажа")
    print("1. Warrior  2. Mage  3. Archer")
    choice = input()
    character_class = "None"
    while True:
        match choice:
            case "1":
                character_class = "Warrior"
                break
            case "2":
                character_class = "Mage"
                break
            case "3":
                character_class = "Archer"
                break
            case _:
                print("Please enter a valid option")
                continue
    return character_class

def character_stats(character_name, character_class):
    match character_class:
        case "Warrior":
            character = Character(character_name, character_class, 200, 0, 20, 20, 200, 0)
        case "Mage":
            character = Character(character_name, character_class, 50, 500, 10, 10, 50, 500)
        case "Archer":
            character = Character(character_name, character_class, 100, 50, 15, 15, 100, 50)
    return character
def new_game():
    character_name = character_name_choice()
    character_class = character_class_choice()
    character = character_stats(character_name, character_class)
    character.describe_character()
    return character




while True:
    menu()
    should_exit = choice_menu_option()
    if should_exit:
        break



