"""
Задача1. Є список чисел. Надрукуйте тільки парні числа з цього списку
Список  повинен заповнюватись 100 випадковими числами.
"""
import random
#print(random.randint(1,)
#number = []
# for _ in range(100):
#     number.append(random.randint(-100, 100))
#print(number)
import random
numbers = [random.randint(-100, 100) for _ in range(100)]
result = []
for num in numbers:
    if num % 2 == 0:
        print(num, end=',')
    result.append(num)
print(result)

"""
Задача 2. Порахуйте кількість від'ємних цифр
"""
import random
numbers = [random.randint(-100, 100) for _ in range(100)]
negativ_count = 0
for num in numbers:
    if num % 2 == 0:
        print(num, end=',')
    if num < 0:
        negativ_count += 1
print(f'Кількість від"ємних чисел: {negativ_count}')

"""
Задача 3. Порахуйте кількість слів у тексті
"""
#Variant#1
words = 'Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend'
words = words.split()  #Метод .split() розбиває рядок на список слів за пробілами.
#print(len(set(words))) # Додатковий варіант рішення через set

#Variant#2
words = 'Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend'
words = words.split()
counter = 0
memory = []
for el in words:
    if el not in memory:
        counter += 1
        memory.append(el)
print(counter)

"""
Завдання 4: Вводиться дробове число. 
Надрукувати окремо цифри цілої частини і дробової.
Розділювачем є десяткова крапка.
12.567 -- 12 567
0.75 -- 0 75
"""
name = input('Введіть дробове число: ')
parts = name.split('.')
print(parts[0], parts[1])

"""
Завдання 5: Напишіть програму, яка отримує повне ім'я файлу 
від користувача та друкує на екрані розширення отриманого файлу
test.cpp --- cpp
"""

name = input('Введіть файл: ').split('.') #file.txt
print(name[-1])

"""
Завдання 6: Напишіть програму для підрахунку кількості днів, 
в яких температура була не нижче, ніж середня температура
за весь період. У першому рядку вводиться список показників 
температури на кожен день. 
У рядку виведення одне число - кількість днів, які відповідають умові.
"""
temp = [-3, -1, 0, 2, 6, 8, 12, 15]
counter = 0

average_temp = sum(temp)/ len(temp)
for n in temp:
    if n> average_temp
    counter += 1
print(f'Кількість днів: {counter}')