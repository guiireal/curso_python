with open('people.csv', 'r', encoding='utf-8') as file:
    with open('people.txt', 'w', encoding='utf-8') as output:
        for item in file:
            person = item.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*person), file=output)
    