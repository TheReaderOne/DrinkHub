

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

    for key, value in database.items():
        if preference in value:
            search_name = key

            search_ingredients = value

    recipe = search_ingredients[1]

    print('ingredients for ' + search_name + '\n')
    for ingredient in recipe:
        print(ingredient)






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

    print('welcome in DrinkHub')
    print("please choose your drink-type preferention: " + '\n')
    preference = get_inputs(get_titles())
    choose_drink(preference,import_data_from_file())


if __name__ == '__main__':
    main()
