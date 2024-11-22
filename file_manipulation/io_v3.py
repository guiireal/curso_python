file = open('people.csv', encoding='utf-8')

try:
    file = open('people.csv', encoding='utf-8')

    for item in file:
        print('Nome: {}, Idade: {}'.format(*item.strip().split(',')))
except IndexError:
    pass
finally:
    file.close()
