

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

    return drink_data_dict


def choose_drink(preference,database):

    searched_dict = {}

    for drink,drink_data in database.items():
        if preference in drink_data:
            recipe = drink_data[1]
            searched_dict[drink] = recipe

    print("write name of interested drink:" + '\n')
    for key in searched_dict.keys():
        print(key)
    
    pick_final_drink = input('choose drink: ')
    print('\n' + 'ingredients for ' + pick_final_drink + ':')
    if pick_final_drink in searched_dict.keys():
        for ingredients in searched_dict[pick_final_drink]:
            print(ingredients)


def get_inputs(titles):

    data = []
    for parameter in titles:
        user_input = input(parameter + '\n')
        data.append(user_input)

    return data


def get_titles():

    titles = ['easy, medium or hard to prepare? ', 'main ingredient is: vodka, rum, gin, whiskey or wine? ',
              'light, medium or strong? ', 'sweet or sour taste? ']
    return titles


def main():
    preference = ['easy','vodka','strong','sweet']

    print('welcome in DrinkHub')
    print("please choose your drink-type preferention: " + '\n')
    # preference = get_inputs(get_titles())
    choose_drink(preference,import_data_from_file())


if __name__ == '__main__':
    main()
