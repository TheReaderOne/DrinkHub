
import os
import main
import sys
import time
import drinkcal

def start_menu_select():
    while True:
        os.system('clear')
        display_screen('start_screen.txt')
        answer = input("Choose option : ")

        if answer == '1':
            os.system('clear')
            break

        elif answer == '2':
            os.system('clear')
            display_screen('about.txt')
            input('\nPress any key to go back')

        elif answer == '3':
            os.system('clear')
            display_screen('goodbye.txt')
            sys.exit()


def handle_menu():
    options = ["Choose your drink.",
            "Make a drink.",
            "Show Your choises.",
            'Drink calculator (BAC).',
            'Back to main menu.']

    
    while True:
        print_menu("Options:", options)
        time.sleep(1)
        answer = input('Select option:')
        if answer == '1':
            preference = main.get_inputs(main.get_titles(),main.import_data_from_file())
            main.choose_drink(preference,main.import_data_from_file())

        if answer == '2':
            pref = main.ingr_input()
            main.search_drink_by_ingredients(main.import_data_from_file(),pref)

        if answer == '3':
            main.import_statistic(filename='stats_drink_name')

        if answer == '4':
            data = drinkcal.get_input()
            age = int(data[0])
            weight = int(data[1])
            height = int(data[2])
            sex = data[3]
            volume = int(data[4])
            precent = float(data[5])
            getbac = drinkcal.get_bac(age,weight,height,sex,volume,precent)
            x = getbac / 10
            time.sleep(1)
            print('Your BAC ratio:' + str(x))
            time.sleep(2)
            print_vac_table()
            

        if answer == '5':
            main.main()
    
def print_vac_table():
    print('BAC Chart Values') 
    print('0.00 – 0.03%	Normal behavior, no impairment')
    print('0.03 – 0.06%	Mild euphoria and impairment; decreased inhibitions')
    print('0.06 – 0.10%	Buzzed, euphoric, increased impairment')
    print('0.10 – 0.20%	Drunk, emotional swings, slurred speech, nausea, loss of reaction time and motor control')
    print('0.20 – 0.30%	Confused, nauseated, poor mentation, blackout')         
    print('0.30 – 0.40%	Possibly unconscious, unarrousable, loss of bladder function, risk of death')
    print('Above 0.40%	Unconscious, coma, impaired breathing, risk of death')


def print_menu(title, list_options):
   
    print(title+'\n')
    for index, value in enumerate(list_options,1):
        print("({}) {}\n".format(index, value))

def display_screen(filename):
    with open(filename) as f:
        read_data = f.read()
    print(read_data)

def print_error_message(message):
    print(message)
