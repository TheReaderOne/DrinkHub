import sys
import os
import ui
import time

def import_data_from_file(filename = 'data.txt'):

    data_temp = []
    data_preferences = []
    data_ingredients = []
    drink_data_dict = {}

    with open (filename) as file:
        data = file.read().strip()
        for line in data.split('\n'):
            line_list = [x for x in line.strip().split(',')]
            data_temp.append(line_list)

    for data in range(0,len(data_temp),2):
        data_preferences.append(data_temp[data])
    for data in range(1,len(data_temp),2):
        data_ingredients.append(data_temp[data])


    for index in range(len(data_preferences)):
        drink_data_dict[data_preferences[index][0]] = [data_preferences[index][1:],data_ingredients[index]]

    print('tekst z notatnika jest zamieniany na to:')
    for x,y in drink_data_dict.items():
        print(x,y)
    print('\n') ############
    
    return drink_data_dict


def choose_drink(preference, database):

    searched_dict = {}
    recipe_index = 1

    for drink, drink_data in database.items():
        if preference in drink_data:
            recipe = drink_data[recipe_index]
            searched_dict[drink] = recipe
    print('jezeli znajdzie [easy,vodka,strong,sweet] w bazie z notatnika tworzy nowy  slownik ( dodaje do zdefiniowanego pustego) gdzie klucz to nazwa drinka a wartosc to lista ze skladnikami'   )
    
    for x,y in searched_dict.items() :
        print(x,y)
    print('\n') ###########

    print("found drinks:" + '\n')

    for key in searched_dict.keys():
        print(key)

    search_name = True

    while search_name:
        pick_final_drink = input('\nchoose drink: ')
        if pick_final_drink in searched_dict.keys():
            print('\n' + 'ingredients for ' + pick_final_drink + ':')
            for ingredients in searched_dict[pick_final_drink]:
                print(ingredients)
                search_name = False
            
            answer = input("Do you want remember your choice? yes/no")
            if answer == "yes":
                time.sleep(1)
                print ("Your choises are remembered")
                time.sleep(2)
                to_save = pick_final_drink + ','
                save_statistic_to_file(to_save)
                print ('show stat? yesss')
                time.sleep(1)
                import_statistic()


            
            

               
        else:
            print('wrong name - try again')

def save_statistic_to_file(name_of_drink,filename='stats_drink_name'):
    with open (filename,'a') as file:
        file.write(name_of_drink)


def get_inputs(titles):

    # data = []
    # for parameter in titles:
    #     #time.sleep(1)
    #     user_input = input(parameter + '\n')
    #     data.append(user_input)
    # print(data)
    # print('\n')
    ser = ['easy','vodka','strong','sweet']
    return ser


def get_titles():
    print ('Give us your preferences')
    
    titles = ['easy, medium or hard to prepare? ', 'main ingredient is: vodka, rum, gin, whiskey or wine? ',
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
    print ('Give us your preferred ingredients')
    #time.sleep(1)
    titles = ['type of alkohol', 'type of juice', 'type of syrup', 'type of fruit']
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
        dict_counter[name] = (dict_counter.get(name,0) +1) 

    print(dict_counter)




    print('drink history')

    for value,key in dict_counter.items():
        print(value,key)



def display_saved_drinks():
    with open('Choosing_drinks.txt') as f:
        read_data = f.read()
    if not read_data:
        print('Empty!')
    else:                                          
        print(read_data)

def main():
    
    ui.start_menu_select()
    ui.handle_menu()


if __name__ == '__main__':
    main()
