import csv

with open('people.csv', encoding='utf-8') as input:
    for person in csv.reader(input):
        print('Nome: {}, Idade: {}'.format(*person))