
# Завдання 1
numbers = input('Введіть числа через пробіл: ') + " "

even_count = 0 #парні
odd_count = 0 #непарні
memory = ''
for char in numbers:
    if char != ' ':
        memory += char
    else: # якщо char - пробіл
        if not memory:  #if memory == '' (якщо змінна порожня)
            continue
        if int(memory) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        memory = ''

print(f'Кількість парних: {even_count}')
print(f'Кількість непарних: {odd_count}')

# Бонусний варіант:
numbers = list(map(int, input('Введіть числа через пробіл: ').split()))
print(f'Кількість парних: {sum(1 for number in numbers if number % 2 == 0)}')
print(f'Кількість непарних: {sum(1 for number in numbers if number % 2 != 0)}')


# Складна задача 2
find_len = int(input('Введіть шукому довжину слова: '))
text = 'Привіт, як твої справи? У мене все ок.'
counter  = 0

word = ''
for char in text:
    if char in '!?.,:;()':  # якщо символ - знак пунктуації
        if len(word) == find_len:
            counter += 1
        word = ''
    else:  # якщо символ - не знак пунктуації
        word += char
print(f'Результат: {counter}')


#Завдання 1
"""
1. Напишіть програму, яка запитує у користувача цілі числа, 
доки він не введе 0, а потім виводить суму всіх введених чисел.
"""
total = 0
while True:
    number = int(input("Введіть число (0 для завершення): "))
    if number == 0:
        break
    total += number
print(f'Сума всіх введених чисел: {total}')

#Завдання 2
"""
2. *Напишіть програму, яка запитує у користувача число 
та виводить послідовність чисел Фібоначчі до цього числа
за допомогою циклу while.
"""
#variant1
number = int(input('Введіть число: '))
# a = 0 # завжди передостаннє число
# b = 1 # завжди останнє число
a, b = 0, 1
while a <= number:
    print(a, end=' ')
    a, b = b, a + b
#variant2
user_number = int(input('Введіть число: '))
a = 0  # завжди передостаннє число
b = 1  # завжди останнє число
while a <= user_number:
    print(a, end=' ')
    a, b = b, a + b

#Завдання 3
"""
3. Напишіть програму, яка знаходить всі числа Армстронга 
в заданому діапазоні. Число Армстронга - це таке число, 
яке дорівнює сумі своїх цифр, піднятих до ступеня, 
рівного кількості цифр у числі. Наприклад, 153 є 
числом Армстронга, оскільки 1^3 + 5^3 + 3^3 = 153.
"""
start = int(input('Введіть початок: '))
end = int(input('Введіть кінець: '))

for number in range(start, end + 1):
    result = 0
    str_number = str(number)
    number_len = len(str_number)
    for str_digit in str_number:
        result += int(str_digit) ** number_len
    if result == number:
        print(f'Число Армстронга знайдено: {number}')

#Завдання 4
"""
4. Дана строка. Зсуньте всі знаки пунктуації та 
пробіли на кінець строки. Приклад: 
«Привіт, я просто тестую. Це звичайний текст!!»
 -> «ПривітяпростотестуюЦезвичайний текст,   .  !!»
"""

text = 'Привіт, я просто тестую. Це звичайний текст!!'
punctuacii = ''
chars = ''
for char in text:
    if char in ' ,.!?;:\'"()<>':
        punctuacii += char
    else:
        chars += char
result = chars + punctuacii
print(result)

