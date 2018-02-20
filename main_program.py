

def import_data_from_file(filename = 'data.txt'):

    data_temp = []
    data_preferences = []
    data_ingredients = []
    drink_data_dict = {}

    with open (filename) as file:
        data = file.read().strip()
        for line in data.split('\n'):
            line_list = [x for x in line.split(',')]
            data_temp.append(line_list)

    
    for data in range(0,len(data_temp),2):
        data_preferences.append(data_temp[data])
    for data in range(1,len(data_temp),2):
        data_ingredients.append(data_temp[data])


    for index in range(len(data_preferences)):
        drink_data_dict[data_preferences[index][0]] = [data_preferences[index][1:],data_ingredients[index]]

    
    print(drink_data_dict)


import_data_from_file()


def get_inputs(titles):

    data = []

    for parameter in titles:
        user_input = input(parameter)
        data.append(user_input)

    return data


def get_titles():

    titles = ['easy or complicated?', 'vodka, whiskey or wine?',
              'strong or soft?', 'sweet or sour taste?']
    return titles


def main():

    print('welcome in DrinkHub')
    # print("please choose your drink-type preferention: " + '\n')

    # preference = get_inputs(get_titles())
    # print(preference)


if __name__ == '__main__':
    main()
