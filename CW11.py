"""
Завдання1 Записати базу робітників
Кожен робітник має : ім'я, вік, місце проживання
та навички (може бути декілька)
worker = {
    'name': str,
    'age': int,
    'country': str,
    'skills': [str, str, ...]
workers = [worker, worker, ...]
"""
workers = [
    {
        'name': 'Сергій Сергієв',
        'age': 25,
        'country': 'Україна',
        'skills': ['Python', 'HTML CSS', 'JavaScript']
    },
    {
        'name': 'Ольга Ольгова',
        'age': 38,
        'country': 'Чехія',
        'skills': ['C++', 'C', 'C#', 'Assembler', 'Ruby']
    },
    {
        'name': 'Антон Антонов',
        'age': 19,
        'country': 'Польша',
        'skills': []
    },
    {
        'name': 'Павло Павлов',
        'age': 41,
        'country': 'Канада',
        'skills': ['React', 'Angular', 'Vue', 'Ruby']
    }
]
# count = 1
# for worker in workers: # worker: dict
    # print(f'{count}. {worker}')
    # count += 1
    # print(count)
    # print(worker) # Завдання: зробіть нумерацію робітників (щоб кожен робітник
                  # був пронумерований, йшли елементи 1 - 2 - 3 -4)

for counter, worker in enumerate(workers, start=1): # worker: dict
    print(f'{counter}. {worker['name']}, {worker['age']} років:')
    print(f'\t-Місце проживання: {worker['country']};')
    print(f'\t-Навички:')
    for skill_counter, skill in enumerate(worker['skills'], start=1):
        print(f'\t\t{skill_counter}. {skill}')
print('\n'.join(f'{counter}. {worker['name']}, {worker["age"]} років:\n\t-Місце проживання: {worker["country"]}\n\t-Навички:\n{"\n".join(f'\t\t{c}. {skill}' for c, skill in enumerate(worker["skills"], start=1))}' for counter, worker in enumerate(workers, start=1)))

"""
Завдання №2 Ви створюєте пригодницьку гру і використовуєте для зберігання гравця словник, 
у якому ключі - це назви предметів, значення - кількість одиниць кожної із речей.
Виведіть повідомлення про усі речі гравця як у вихідних даних
"""
equip = {
    'stone': 3,
    'coin': 10,
    'sword': 1,
    'shield': 2,
    'gold ore': 15
}

#variant #1
print('Equipment:')
total = 0
for name, count in equip.items():
    print(f"{count} {name}")
    total += count
print(f"Total: {total}")

#variant #2
print('Equipment:')
for name, count in equip.items():
    print(f"{count} {name}")
print(f'Total: {sum(equip.values())}')
