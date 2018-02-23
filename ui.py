
import os
import main
import sys
import time

def start_menu_select():
    while True:
        os.system('clear')
        display_screen('start_screen1.txt')
        answer = input('Are you over 18 years old?  yes/no: ' + '\n')
        if answer == "yes":
            display_screen('start_screen.txt')
            answer = input("Choose option :" + '\n')
        else:
            print ('It will be better if you drink Fanta!')
            time.sleep(1)
            display_screen('goodbye.txt')
            sys.exit()

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
            "Fast sobriety test",]

    print_menu("Options:" + '\n', options, "Exit program")
    while True:
        answer = input()
        if answer == '1':
            preference = main.get_inputs(main.get_titles())
            main.choose_drink(preference,main.import_data_from_file())

        elif answer == '2':
            preferences = main.get_inputs(main.get_titles_to_make_drink())
            main.make_drink(main.import_data_from_file('data_craft_drink.txt'), preferences)

        elif answer == '3':
            os.system('clear')
            display_screen('test.txt')
            time.sleep(3)
            display_screen('goodbye.txt')
            sys.exit()

        elif answer == '4':
            os.system('clear')
            display_screen('goodbye.txt')
            sys.exit()


def print_menu(title, list_options, exit_message):
    print(title)
    for index, value in enumerate(list_options, 1):
        print("\t({}) {}".format(index, value))
    print("\t(4) {}".format(exit_message))

def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)


#def print_error_message(message):
 #   print(message)
