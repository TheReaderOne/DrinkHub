
import data
import display

def get_inputs(titles):

    data = []
   
    for parameter in titles:
        user_input = input(parameter)
        data.append(user_input)
   
    return data


def get_titles():

    titles = ['easy or complicated?','vodka, whiskey or wine?','strong or soft?','sweet or sour taste?']
    return titles

def main():

    print('welcome in DrinkHub')
    print("please choose your drink-type preferention: " + '\n')

    preference = get_inputs(get_titles())
    print(preference)

  


if __name__ == '__main__':
    main()
