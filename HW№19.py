#Завдання на уроці
"""
1. Створіть JSON-файл, в якому знаходяться товари: Назва товару та його ціна. Напишіть :
а) Парсер, що відкриває файл та виводить всі товари, ціна яких більше за 1000
б) Парсер, що відкриває файл та виводить весь його зміст наступним чином:
1. Яблуко - 10$
2. Банан - 20$
Можна створення та доповнення файлу зробити окремою функцією
"""
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
    print('-' * 30)
    for product in expensive_products:
        print(f'Назва: {product['name']}, Ціна: {product['price']}$')

def print_all_products():
    if not data:
        print('Список товарів порожній.')
        return

    print('\nУсі товари:')
    print('-' * 30)
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

#==================================================================
#Домашнє завдання
"""
Розробіть застосунок «Менеджер контактів». 
Застосунок передбачає наступний функціонал: 
*створення нового контакту, 
*видалення контакту та 
*друк всіх наявних контактів. 
Контакт повинен мати: 
номер, ім’я та опис контакту. 
Застосунок повинен мати активну базу, 
яка оновлюється та не очищуватись після виходу. 
Зробіть збереження бази за допомогою pickle. 
"""
import pickle

CONTACTS_FILE = 'files\\contacts.pkl'

def load_contacts():
    try:
        with open(CONTACTS_FILE, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "wb") as file:
        pickle.dump(contacts, file)

def add_contact():
    contacts = load_contacts()
    number = input('Введіть номер телефону: ').strip()
    name = input('Введіть ім\'я: ').strip()
    description = input('Введіть опис: ').strip()

    if not number or not name:
        print('Номер і ім\'я не можуть бути порожніми!')
        return

    contacts.append({"number": number, "name": name, "description": description})
    save_contacts(contacts)
    print(f'Контакт "{name}" успішно додано!')

def delete_contact():
    contacts = load_contacts()
    print_contacts()
    choice = input('Введіть порядковий номер або ім\'я контакту для видалення: ').strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f'Контакт "{deleted_contact["name"]}" видалено.')
        else:
            print('Некоректний номер контакту.')
    else:
        new_contacts = [c for c in contacts if c["name"] != choice]
        if len(new_contacts) == len(contacts):
            print('Контакт не знайдено!')
        else:
            save_contacts(new_contacts)
            print(f'Контакт "{choice}" видалено.')

def print_contacts():
    contacts = load_contacts()
    if not contacts:
        print('Контактів немає.')
        return

    print("\nУсі контакти:")
    print("-" * 30)
    for i, c in enumerate(contacts, start=1):
        print(f'{i}. {c["name"]} ({c["number"]}) - {c["description"]}')

def main():
    while True:
        print('\n' + "=" * 30)
        print('Меню:')
        print('1. Додати контакт')
        print('2. Видалити контакт')
        print('3. Показати всі контакти')
        print("4. Вийти")
        print("=" * 30)
        choice = input("Оберіть опцію: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            print_contacts()
        elif choice == "4":
            print('Дякую за використання програми! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')

if __name__ == "__main__":
    main()


