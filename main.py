import sys
import os
import ui
import time


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
        drink_data_dict[data_preferences[index][0]] = [data_preferences[index][1:], data_ingredients[index], data_describe[index], data_ml[index]]
    # print(drink_data_dict)

    for k, v in drink_data_dict.items():
        print(k)
        print(v)
    # for x in data_ml:
    #     print(x)
    return drink_data_dict


def choose_drink(preference, database):

    filter_dick = {}

    for drink, drink_data in database.items():
        if preference in drink_data:
            filter_dick[drink] = drink_data

    print(filter_dick)
    print("found drinks:" + '\n')
    for key in filter_dick.keys():
        print(key)
    # for value in filter_dick.values():
    #     print(value)
    # print(filter_dick)

    picked_item_dict = {}
    picked_item_ml = []
    picked_item_ingr = []

    search_name = True

    while search_name:
        next_menu = False
        pick_final_drink = input('\nchoose drink: ')

        for key, value in filter_dick.items():
            if key == pick_final_drink:
                picked_item_dict[key] = value
                print(picked_item_dict)

                next_menu = True

        if next_menu:
            return_to_main = '5'
            answer = '1'
            while return_to_main != answer:
                print("menu:")
                print('1. show ingredients')
                print('2. drunk calculator')
                print('3. save choice ')
                print('4. show drink-pick history')
                print('5. return to main menu: ')
                time.sleep(1)
                answer = input('choose: ' + '\n')
                if answer == '1':
                    ml = 'ml'

                    for value in picked_item_dict.values():
                        picked_item_ingr = value[1]
                        picked_item_ml = value[3]
                        stats_recipe = dict(
                            zip(picked_item_ingr, picked_item_ml))

                        for k, v in stats_recipe.items():
                            stats_recipe[k] = v + ml
         
                        for k,v in stats_recipe.items():
                            print(k,v)
                        
                if answer == '5':

                    main()

    # if answer == '1':
    #     for index in range(show_ml_recipe_table):
    #         ml = show_ml_recipe_table[index]

    # answer = input("Do you want remember your choice? yes/no")
    # if answer == "yes":
    #     time.sleep(1)
    #     print ("Your choises are remembered")
    #     time.sleep(2)
    #     to_save = pick_final_drink + ','
    #     save_statistic_to_file(to_save)
    #     print ('show stat? yesss')
    #     time.sleep(1)
    #     import_statistic()

    #     else:
    #         print('wrong name - try again')


def save_statistic_to_file(name_of_drink, filename='stats_drink_name'):
    with open(filename, 'a') as file:
        file.write(name_of_drink)


def get_inputs(titles):

    # data = []
    # for parameter in titles:
    #     #time.sleep(1)
    #     user_input = input(parameter + '\n')
    #     data.append(user_input)
    # print(data)
    # print('\n'),

    ser = ['hard', 'vodka', 'medium', 'sour']
    
    return ser


def get_titles():
    print ('Give us your preferences')

    titles = ['easy, medium or hard to prepare? ', 'main ingredient is: vodka, rum, gin or whiskey? ',
              'light, medium or strong? ', 'sweet or sour taste? ']
    return titles


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
    #time.sleep(1)
    titles = ['type of alkohol', 'type of juice',
              'type of syrup', 'type of fruit']
    return titles


# def save_choose_drink():
#     searched_dict = choose_drink()
#     file = open("Choosing_drinks.txt", 'a+')
#     file.write(str(choose_drink(searched_dict)))

def import_statistic(filename='stats_drink_name'):
    database_table = []
    dict_counter = {}
    with open(filename) as file:
        data = file.read().strip()

    for name in data.split(','):
        database_table.append(name)
    database_table.pop()
    print(database_table)

    for name in database_table:
        dict_counter[name] = dict_counter.get(name, 0) + 1

    print(dict_counter)

    print('drink history')

    for value, key in dict_counter.items():
        print(value, key)


def display_saved_drinks():
    with open('Choosing_drinks.txt') as f:
        read_data = f.read()
    if not read_data:
        print('Empty!')
    else:
        print(read_data)


def main():
    # import_data_from_file()
    test = ['easy', 'vodka', 'strong', 'sweet']

    #test = ['hard', 'vodka', 'medium', 'sour']
    choose_drink(test, import_data_from_file())
    # ui.start_menu_select()
    # ui.handle_menu()


if __name__ == '__main__':
    main()
