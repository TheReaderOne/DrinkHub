import sys
import os
import ui
import time

def print_sub_menu ():
    print('\nmenu:\n')
    print('1. show ingredients')
    print('2. display recipe')
    print('3. show total volume of liquids')
    print('4. save choice to database ')
    print('5. show drink-pick history')
    print('6. return to main menu: \n')

def import_data_from_file(filename='data.txt'):

    data_temp = []
    data_preferences = []
    data_ingredients = []
    data_describe = []
    data_ml = []
    drink_data_dict = {}

    with open(filename) as file:
        data = file.read().strip()
        for line in data.split('\n'):
            line_list = [x for x in line.strip().split(',')]
            data_temp.append(line_list)

    for symbol_index in range(0, len(data_temp)-1, 4):
        data_preferences.append(data_temp[symbol_index])

    for symbol_index in range(1, len(data_temp)-1, 4):
        data_ingredients.append(data_temp[symbol_index])

    for symbol_index in range(2, len(data_temp)-1, 4):
        data_describe.append(data_temp[symbol_index])

    for symbol_index in range(3, len(data_temp)-1, 4):
        data_ml.append(data_temp[symbol_index])

    for index in range(len(data_preferences)-1):
        drink_data_dict[data_preferences[index][0]] = [data_preferences[index]
                                                       [1:], data_ingredients[index], data_describe[index], data_ml[index]]

    return drink_data_dict


def choose_drink(preference, database):

    filter_dict = {}
    picked_item_dict = {}
    picked_item_ml = []
    picked_item_ingr = []

    for drink, drink_data in database.items():
        if preference in drink_data:
            filter_dict[drink] = drink_data

    print("found drinks:" + '\n')
    for key in filter_dict.keys():
        print(key)

    search_name = True
    while search_name:
        next_menu = False
        pick_final_drink = input('\nchoose drink: ')

        for key, value in filter_dict.items():
            if key == pick_final_drink:
                picked_item_dict[key] = value
                next_menu = True

        if next_menu:
            return_to_main = '5'
            answer = '1'
            while return_to_main != answer:
                print_sub_menu()
                time.sleep(1)
                answer = input('choose: ')

                if answer == '1':
                    print('\n')

                    for value in picked_item_dict.values():
                        picked_item_ingr = value[1]
                        picked_item_ml = value[3]
                        stats_recipe = dict(
                            zip(picked_item_ingr, picked_item_ml))

                        for k, v in stats_recipe.items():
                            stats_recipe[k] = v + 'ml'

                        for k, v in stats_recipe.items():
                            print(k, v)

                if answer == '2':
                    data_index = 0
                    recipe_index = 2
                    print('\n')
                    values = list(picked_item_dict.values())
                    recipe = values[data_index][recipe_index]
                    print(', '.join(recipe))

                if answer == '3':
                    print('\n')
                    calc_vol = sum(map(int, picked_item_ml))
                    print('Total volume of drink: ' + str(calc_vol) + ' ml.')

                if answer == '4':
                    print('\n')
                    for key in picked_item_dict.keys():
                        save_statistic_to_file(key)
                    time.sleep(1)
                    print('Pick has been saved.')

                if answer == '5':
                    print('\n')
                    import_statistic()

                if answer == '6':
                    main()


def save_statistic_to_file(name_of_drink, filename='stats_drink_name'):
    with open(filename, 'a') as file:
        file.write(name_of_drink + ',')


def get_inputs(titles):

    data = []
    for parameter in titles:
        #time.sleep(1)
        user_input = input(parameter + '\n')
        data.append(user_input)
    print(data)
    print('\n'),

    # ser = ['hard', 'vodka', 'medium', 'sour']

    return data


def get_titles():
    print('Give us your preferences')

    titles = ['easy, medium or hard to prepare? ', 'main ingredient is: vodka, rum, gin or whiskey? ',
              'light, medium or strong? ', 'sweet or sour taste? ']
    return titles


def ingr_input():
    titles = ['type of alkohol u have','type of juice','type of syrup','type of fruit']
    data = []
   
    for title_index in range(len(titles)-1):
        user_input = input(titles[title_index])
        if user_input != 'none':
            data.append(user_input)

    return data  


def search_drink_by_ingredients(database, user_input):
    filtered_dict = {}

    test = ['vodka', 'orange juice', 'grenadine syrup']
    user_input = test
    for key, value in database.items():
        if user_input in value:
            filtered_dict[key] = value

    # print(filtered_dict)
    print('Found: ')
    for key in filtered_dict.keys():
        print(key)


    pick_drink = input('Please write drink which was found.')

    if pick_drink in filtered_dict.keys():
        match = filtered_dict[pick_drink]
        ingredients_index = 1
        match = match[ingredients_index] 
        choose_drink(match,database)



def make_drink(drinks_dict, user_input):

    match_dict = {}


    for key, value in drinks_dict.items():
        if user_input in value:
            recipe = value[1]
            match_dict[key] = recipe

    print("found drinks:" + '\n')
    for key in match_dict.keys():
        print(key)

    search_name = True
    while search_name:
        pick_final_drink = input('\nchoose drink: ')
        if pick_final_drink in match_dict.keys():
            print('\n' + 'ingredients for ' + pick_final_drink + ':')
            for ingredients in match_dict[pick_final_drink]:
                print(ingredients)
                search_name = False
        else:
            print('wrong name - try again')


def get_titles_to_make_drink():

    print('Give us your preferred ingredients')
    #
    titles = ['type of alkohol', 'type of juice',
              'type of syrup', 'type of fruit']
    return titles


def import_statistic(filename='stats_drink_name'):
    database_table = []
    dict_counter = {}
    with open(filename) as file:
        data = file.read().strip()

    for name in data.split(','):
        database_table.append(name)
    database_table.pop()

    for name in database_table:
        dict_counter[name] = dict_counter.get(name, 0) + 1

    print('drink history\n')

    for value, key in dict_counter.items():
        get_temp_key = str(key)
        get_temp_value = str(value)
        print(get_temp_value + ' was chosen ' + get_temp_key + ' times.')

def display_saved_drinks():
    with open('Choosing_drinks.txt') as f:
        read_data = f.read()
    if not read_data:
        print('Empty!')
    else:
        print(read_data)


def main():
    # get_inputs(get_titles())
    # import_data_from_file()
    test = ['easy', 'vodka', 'strong', 'sweet']
    search_drink_by_ingredients(import_data_from_file(),test)

    # # ui.start_menu_select()
    # # ui.handle_menu()
    # choose_drink(test, import_data_from_file())


if __name__ == '__main__':
    main()
