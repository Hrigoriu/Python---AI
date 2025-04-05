#Завдання №1
"""
Напишіть програму для підрахунку кількості рядків у текстовому файлі.
Вхідні дані:
Python
Ruby
C++
C
Java
GO
Вихідні дані:
6
"""
#Variant #1
with open('files\\data.txt', 'r') as file:
    print(len(file.readlines()))

#Variant #2
with open('files\\data.txt', 'r') as file:
    count = 0
    for line in file:
        count += 1
    print(count)

#Variant #3
def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    return count

def main():
    filename = 'files\\data.txt'
    line_count = count_lines(filename)
    print(line_count)

if __name__ == '__main__':
    main()


#Завдання №2
"""
У вихідному файлі записано два цілих числа, які можуть бути розділені пропусками 
і кінцями рядків. Виведіть у вихідний файл суму.
Вхідні дані:
Файл input.txt з вмістом
    2
2    
Вихідні дані:
Файл output.txt з вмістом
4
"""
with open('files//input.txt', 'r') as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())

total = num1 + num2

with open('out.txt', 'w') as file:
    file.write(str(total))
===============================================================

#Завдання №1
"""
Напишіть функцію, яка приймає кілька файлів (безліч) і створює новий файл, 
який містить їхній об'єднаний вміст. Новий файл повинен містити всі рядки 
вихідних файлів.
"""
def all_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for filename in input_files:
            with open(filename, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')

def main():
    input_files = ['files\\data.txt', 'files\\file1.txt']
    output_file = 'files\\file2.txt'
    all_files(input_files, output_file)
    print(f'Файли об`єднано у {output_file}')

if __name__ == '__main__':
    main()


#Завдання №2
"""
Напишіть функцію, яка запитує користувача список і виводить кожен елемент списку 
з його індексом. Опрацюйте виняток IndexError при спробі доступу до 
неіснуючого індексу списку та виведіть повідомлення про помилку.
"""
def list_with_indices():
    user_input = input('Введіть елементи списку через пробіл: ')
    user_list = user_input.split()
    print('Елементи списку з їхніми індексами:')
    try:
        for index in range(len(user_list) + 1):
            element = user_list[index]
            print(f'Індекс {index}: {element}')
    except IndexError:
        print('Помилка: Спроба доступу до не існуючого індексу списку!')

print(list_with_indices())


#Завдання №3
"""
Напишіть функцію, яка відкриває файл, зчитує його і виводить на екран. 
Опрацюйте виняток FileNotFoundError під час спроби відкрити неіснуючий файл та 
виведіть повідомлення про помилку.
"""
def read_and_display_file(filename):
    try:
        with open(filename, 'r') as file:
            print('Вміст файлу:')
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f'Помилка: Файл "{filename}" не знайдено!')

def main():
    filename = input('Введіть ім\'я файлу з шляхом, де він знаходиться: ')
    read_and_display_file(filename)

if __name__ == '__main__':
    main()
