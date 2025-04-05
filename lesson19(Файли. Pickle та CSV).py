import  pickle

data = {'set': {1, 2, 3}, 'tuple': (1, 2, 3)}
with open('files\\data.pkl', 'wb') as file:
    pickle.dump(data, file)
===============================================
import  pickle

with open('files\\data.pkl', 'rb') as file:
    print(pickle.load(file))

===============================================
import csv
with open('files\\data.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Bob', '30'])
    writer.writerow(['ALice', '20'])
==============================================
import csv
with open('files\\data.csv', 'r', newline='', encoding='UTF-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

==============================================

#Завдання №1
"""
1. Створіть JSON-файл, в якому знаходяться товари: Назва товару та його ціна. Напишіть :
а) Парсер, що відкриває файл та виводить всі товари, ціна яких більше за 1000
б) Парсер, що відкриває файл та виводить весь його зміст наступним чином:
1. Яблуко - 10$
2. Банан - 20$
Можна створення та доповнення файлу зробити окремою функцією
"""
#Variant #1
import json

DATABASE_FILE = 'files\\products.json'

def load_data():
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_product():
    name = input('Введіть назву товару: ').strip()
    if not name:
        print('Назва товару не може бути порожньою!')
        return

    try:
        price = float(input('Введіть ціну товару: '))
        if price < 0:
            print('Ціна не може бути від\'ємною!')
            return
    except ValueError:
        print('Будь ласка, введіть коректну ціну (число)!')
        return

    new_product = {
        'name': name,
        'price': price
    }
    data.append(new_product)

    save_data(data)
    print(f'Товар "{name}" з ціною {price}$ успішно додано!')


def print_expensive_products():
    expensive_products = [product for product in data if product['price'] > 1000]
    if not expensive_products:
        print('Немає товарів із ціною більше 1000.')
        return

    print('\nТовари з ціною більше 1000:')
    for product in expensive_products:
        print(f'Назва: {product['name']}, Ціна: {product['price']}$')
        print('-' * 40)


def print_all_products():
    if not data:
        print('Список товарів порожній.')
        return

    print('\nУсі товари:')
    for index, product in enumerate(data, start=1):
        print(f'{index}. {product['name']} - {product['price']}$')


def main():
    while True:
        print('\n' + '=' * 30)
        print('\nМеню:')
        print('1. Додати товар')
        print('2. Показати товари з ціною більше 1000')
        print('3. Показати всі товари')
        print('4. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ')
        print('*!' * 15)

        if choice == '1':
            add_product()
        elif choice == '2':
            print_expensive_products()
        elif choice == '3':
            print_all_products()
        elif choice == '4':
            print('Дякую за використання програми! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')

if __name__ == "__main__":
    main()

==================================
"""
Витягти жіночі імена зі списку Титаніка.
"""
import csv

with open('files\\titanic.csv', 'r', encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        is_survive = row[1]
        name = row[3]
        sex = row[4]
        if sex == 'female' and is_survive:
            print(name)

===============================================
import datetime
print(datetime.datetime.now().strftime('%Y %A %B'))
