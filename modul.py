''' uhiuhui'''


def print_info(name, age, city, lern):
    ''' метож '''
    print(f'Меня зовут {name}')

    if age == 1 or age % 10 == 1:
        let = 'год'
    elif age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        let = 'года'
    else:
        let = 'лет'

    print(f'Мне {age} {let}')
    print(f'Я живу в городе {city}')

    if lern == 'Да' or lern == 'да':
        print('Cейчас учусь')
    elif lern == 'Нет' or lern == 'нет':
        print('Cейчас не учусь')
