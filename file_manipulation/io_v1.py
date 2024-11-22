file = open('people.csv', encoding='utf-8')

data = file.read()

file.close()

for item in data.splitlines():
    print('Nome: {}, Idade: {}'.format(*item.split(',')))