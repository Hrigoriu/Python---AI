"""
Завдання 1
Напишіть функцію, яка прийме текстовий файл з чиселами (в будь-якій послідовності)
та записує у новий файл відсортовані числа по порядку
Файл data.txt:
10-65       5
 564 7      3       67
 -1
54          5444            -564        0       1


5       90
"""

#Variant №1
def numbers_sorter(input_file_path: str, output_file_path='files\\result.txt'):
    numbers = []
    with open(input_file_path, 'r') as read_file:
        file_lines = [line for line in read_file.readlines() if line.strip() != '\n']
    for line in file_lines:
        numbers.extend(map(int, line.split()))
        numbers.sort()
    with open(output_file_path, 'w') as write_file:
        print(*numbers, sep='\n', file=write_file)

numbers_sorter('files\\data.txt')

#Variant №2

def numbers_sorter(input_file_path: str, output_file_path='files\\result.txt'):
    numbers = []
    with open(input_file_path, 'r') as read_file:
        for line in read_file:
            line_split = line.split()
            numbers.extend(int(el) for el in line_split)
    numbers.sort()
    with open(output_file_path, 'w') as write_file:
        print(*numbers, sep='\n', file=write_file)

number_sorter('files\\data.txt')
"""
Файл data.txt:
word1
word2

word3

word4


word5




word6
Отриманий файл:
word1
word2
==================
word3
==================
word4
==================
==================
word5
==================
==================
==================
==================
word6
"""
#def format_empty_lines(input_file_path: str):
    with open(input_file_path, 'r') as read_file:
        line = read_file.readlines()
    with open(input_file_path, 'w') as write_file:
        for line in lines:
            if line.strip(): #перевірка, що лінія не порожня
                print(line, file=write_file, end='')
            else:
                print('==================\n', file=write_file, end='')

format_empty_lines('files\\data.txt')

#Завдання №2
"""
Відсортуйте про учнів, записані у файлі input.txt, складалося з його 
прізвища і назви класу (рік навчання і буква без пробілів), також оцінки, 
отримані за семестр, у форматі: Прізвище Клас Оцінки. Число оцінок 
в різних класах може бути різним. Запишіть у файл output.txt прізвища учнів, 
середній бал яких більше, ніж 6.
Вхідні дані:
Файл input.txt з вмістом:
Barnes 9A 4 5 7 2 3 2
Davidson 10A 7 7 5
Clifford 11B 11 10 8 9 7
Ramacey 8A 5 6 6 5
White 7A 8 5 5 8 9
Porter 11A 11 8
Dean 10B 3 4 5 4 5
Gate 11A 6 5 3 4 3 5
Файл output.txt з вмістом:
Davidson
Clifford
white
Porter
"""

def get_best_students(input_file_path: str):
    with open(input_file_path, 'r') as read_file:
        with open('files\\output.txt', 'w') as write_file:
            for line in read_file:
                split = line.split()
                name = split[0]
                grades = list(map(int, split[2:]))
                if sum(grades) / len(grades) > 6:
                    print(name, file=write_file)
get_best_students('files\\input.txt')

==============================================================

# JSON - JavaScript Object Notation
"""
dump - з Python в Json-файл
load - з Json-файлу в Python

dumps - з Python в Json-строку
loads - з Json-строку в Python
"""
===================================
#Запис
import json

python_data = {
    'key1': True,
    'key2': [1, 2, 3],
    'key3': 54.656,
    'key4': None
}

with open('files\\data.json', 'w') as json_file:
    json.dump(python_data, json_file, indent=4)

==================================
#Читання
import json

with open('files\\data.json', 'r') as json_file:
    data = json.load(json_file)
print(data)

==================================
import json
json_data = json.dumps(python_data, indent=4)
print(json_data)
==================================
#Завдання №3
"""
файл data.json:
[1, 2, 3]
Написати програму, яка добавляє 1.
"""
import json
with open('files\\data.json', 'r') as file:
    data = json.load(file)
data.append(1)
with open('files\\data.json', 'w') as file:
    json.dump(data, file)
========================================================

"""
1.	Напишіть функцію, що приймає ім’я програміста, його вік, місто проживання та 
технології,  яким він володіє  та місце його поточної роботи. Місце поточної 
роботи повинно мати назву та адресу.  Кожному програмісту повинні співпадати його 
дані.  Якщо якась інформація відсутня, замість її повинно бути None. Конвертуйте 
інформацію у json та сформуйте її у файл data.json. При кожному наступному запуску,
функція повинна додавати нового програміста у файл data.json, зберігаючи минулі 
записи.
2.	Напишіть функцію – парсер, що відкриває файл data.json, та парсить його зміст,
видавши на кожного програміста подібне досьє:
Приклад:
•	Іван Іванов, 27 років
o	Місце роботи: Google corp., Mountain View, USA
o	Навички:
	Python(Django, Flask, Pandas)
	HTML, CSS
	SQL
	Мережеве адміністрування
"""

"""
worker = [
    worker1
]


worker = {
    name: str,
    age: int,
    job: str,
    skills: list[str]
}
"""

import json

def add_worker(name: str, age: int, job: str, skills: list[str]):
    try:
        with open('files\\workers.json', 'r') as json_file: # відкриваємо на читання, щоб зберегти попередній зміст
            data = json.load(json_file)
    except FileNotFoundError:   # якщо попредньо файлу не має - створюємо порожній список
        data = []

    new_worker = {
        'name': name,
        'age': age,
        'job': job,
        'skills': skills
    }
    data.append(new_worker)
    with open('files\\workers.json', 'w') as file:
        json.dump(data. file, indent=4)

def print_workers():
    pass
print_workers()

add_worker(name:'Петро Петров', age:30, job:"МакДональдс", skills:['Python', 'С++'])
add_worker(name:'Ольга Ольгова', age:25, job:"Google Inc", skills:['Python', 'HTML CSS', 'JavaScript'])
add_worker(name:'Сергій Сергієв', age:17, job:"Meta Incальдс", skills:['С++', 'C', 'C#', '.Net'])
add_worker(name:'Антон Антонов', age:45, job:"Ajax Systems", skills:['Gjango', 'React'])

============================================================================
import json

def add_worker(name: str, age: int, job: str, skills: list[str]):
    try:
        with open('files\\workers.json', 'r') as json_file:  # відкриємо на читання, щоб зберегти попередній зміст
            data = json.load(json_file)
    except FileNotFoundError:  # якщо попередньо файлу немає - створюємо порожній список
        data = []

    new_worker = {
        'name': name,
        'age': age,
        'job': job,
        'skills': skills
    }
    data.append(new_worker)

    with open('files\\workers.json', 'w') as file:
        json.dump(data, file, indent=4)


def print_workers():
    try:
        with open('files\\workers.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('Робітників немає! База порожня!')
        return

    for counter, worker in enumerate(data, start=1):
        print(f'{counter}. {worker['name']}, {worker['age']} років: ')
        print(f'\t-Місце роботи: {worker['job']};')
        print('\t-Навички: ')

        for skill in worker['skills']:
            print(f'\t\t-{skill}')

print_workers()
==============================================================================







