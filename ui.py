
import os
import main
import sys

def start_menu_select():
    while True:
        os.system('clear')
        display_screen('start_screen.txt')
        answer = input("Choose option : ")

        if answer == '1':
            break

        elif answer == '2':
            os.system('clear')
            display_screen('about.txt')
            input('\nPress enter key to go back')

        elif answer == '3':
            os.system('clear')
            display_screen('goodbye.txt')
            sys.exit()
            


def handle_menu():
    options = ["Choose your drink",
            "Make a drink",
            "Show Your choises"]

    print_menu("Options:", options, "Exit program")
    while True:
        answer = input()
        if answer == '1':
            preference = main.get_inputs(main.get_titles())
            main.choose_drink(preference,main.import_data_from_file())

        elif answer == '2':
            preferences = main.get_inputs(main.get_titles_to_make_drink())
            main.make_drink(main.import_data_from_file('data_craft_drink.txt'), preferences)

        #elif answer == '3':
            
        elif answer == '4':
            os.system('clear')
            display_screen('goodbye.txt')
            sys.exit()


def print_menu(title, list_options, exit_message):
    print(title)
    for index, value in enumerate(list_options, 1):
        print("\t({}) {}".format(index, value))
    print("\t(3) {}".format(exit_message))

def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


def print_error_message(message):
    print(message)
