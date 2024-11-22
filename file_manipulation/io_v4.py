with open('people.csv', encoding='utf-8') as file:
    for item in file:
        print('Nome: {}, Idade: {}'.format(*item.strip().split(',')))