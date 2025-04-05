import json
from datetime import datetime
DATABASE_FILE = 'files\\diary.json'
"""
Розробіть застосунок «Щоденник з базою даних». 
Застосунок передбачає наступний функціонал: 
створення нового запису, 
видалення запису та 
друк всіх наявних записів. 
Кожен запис щоденнику повинен мати: 
номер, назву, дату* та зміст запису. 
Застосунок повинен мати активну базу, яка оновлюється та не очищуватись після виходу. 
Рекомендовано робити за допомогою JSON.
"""

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

def add_entry():
    title = input('Введіть назву запису: ').strip()
    if not title:
        print('Назва запису не може бути порожньою!')
        return
    content = input('Введіть зміст запису: ').strip()
    if not content:
        print('Зміст запису не може бути порожнім!')
        return

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry_id = len(data) + 1
    new_entry = {
        'id': entry_id,
        'title': title,
        'date': date,
        'content': content
    }

    data.append(new_entry)
    save_data(data)
    print(f'Запис {entry_id} "{title}" успішно додано!')

def delete_entry():
    if not data:
        print('Щоденник порожній.')
        return
    try:
        entry_id = int(input('Введіть номер запису для видалення: '))
        entry_to_delete = None
        for entry in data:
            if entry['id'] == entry_id:
                entry_to_delete = entry
                break
        if entry_to_delete:
            data.remove(entry_to_delete)
            for index, entry in enumerate(data, start=1):
                entry[('i'
                       'd')] = index
            save_data(data)
            print(f'Запис {entry_id} "{entry_to_delete['title']}" видалено!')
        else:
            print('Запис із таким номером не знайдено!')
    except ValueError:
        print('Будь ласка, введіть коректний номер!')

def print_all_entries():
    if not data:
        print('Щоденник порожній.')
        return
    print('\nУсі записи щоденника:')

    for entry in data:
        print(f'\nЗапис #{entry['id']}')
        print(f'Назва: {entry['title']}')
        print(f'Дата: {entry['date']}')
        print(f'Зміст: {entry['content']}')
        print('-' * 40)

def main():
    while True:
        print('\n' + '=' * 30)
        print('\nМеню:')
        print('1. Додати запис')
        print('2. Видалити запис')
        print('3. Показати всі записи')
        print('4. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ')
        print('*!' * 15)

        if choice == '1':
            add_entry()
        elif choice == '2':
            delete_entry()
        elif choice == '3':
            print_all_entries()
        elif choice == '4':
            print('Дякую за використання щоденника! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')

if __name__ == "__main__":
            main()
