#Завдання №1
"""
Вам потрібно створити програму, яка дозволяє користувачеві
управляти списком завдань. Програма повинна підтримувати
додавання нових завдань,
видалення існуючих,
відмітку виконаних завдань, а також
виведення всіх завдань та невиконаних завдань.
Вся програма повинна виконуватись за допомогою
функціонального програмування
(кожен елемент програми – це окрема функція) та
об’єднуватись у функції виклику.
За бажанням, можете вдосконалити функціонал на власний розсуд.
"""
data = [
    {'name': 'Вивчити Python',
     'is_complete': False}
]

def add_task():
    task_name = input('Введіть назву завдання: ').strip()
    if task_name:
        data.append({'name': task_name, 'is_complete': False})
        print(f'Завдання "{task_name}" успішно додано!')
    else:
        print('Назва завдання не може бути порожньою!')

def delete_task():
    if not data:
        return
    try:
        dil_num = int(input('Введіть номер завдання для видалення: ')) - 1
        if 0 <= dil_num < len(data):
            removed = data.pop(dil_num)
            print(f'Завдання "{removed['name']}" видалено!')
        else:
            print('Невірний номер завдання!')
    except ValueError:
        print('Будь ласка, введіть корректний номер!')

def mark_task_complete():
    try:
        done_num = int(input("Введіть номер завдання для позначення як виконаного: ")) - 1
        if 0 <= done_num < len(data):
            data[done_num]['is_complete'] = True
            print(f'Завдання "{data[done_num]['name']}" позначено як виконане.')
        else:
            print('Невірний номер завдання.')
    except ValueError:
        print('Будь ласка, введіть коректний номер.')

def print_all_task():
    if not data:
        print('Список завдань порожній.')
    else:
        print('\nСписок всіх завдань:')
        for index, task in enumerate(data, start=1):
            status = 'Виконано' if task['is_complete'] else 'Не виконано'
            print(f'{index}. {task['name']} [{status}]')

def print_incomplete_tasks():
    incomplete_tasks = [task for task in data if not task['is_complete']]
    if not incomplete_tasks:
        print('Немає невиконаних завдань.')
    else:
        print('\nСписок невиконаних завдань:')
        for index, task in enumerate(incomplete_tasks, start=1):
            print(f'{index}. {task['name']}')

def main():
    while True:
        print('\n' + '=' * 30)
        print('\nМеню:')
        print('1. Додати завдання')
        print('2. Видалити завдання')
        print('3. Позначити завдання як виконане')
        print('4. Показати всі завдання')
        print('5. Показати невиконані завдання')
        print('6. Вийти')
        print('\n' + '=' * 30)
        choice = input('Виберіть опцію: ')
        print('*!' * 15)

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            print_all_task()
        elif choice == '5':
            print_incomplete_tasks()
        elif choice == '6':
            print('Дякую що були з нами))! До побачення!')
            break
        else:
            print('Невірний вибір. Спробуйте ще раз.')


if __name__ == "__main__":
    main()