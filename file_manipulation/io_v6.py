import csv

def read(file_name):
    with open(file_name, encoding="ISO-8859-1") as input:
        for city in csv.reader(input):
            print(f'{city[8]}: {city[3]}')

if __name__ == '__main__':
    read('ibge.csv')