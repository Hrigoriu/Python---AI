""" Завдання №1
Напишіть функцію, яка отримує 3 аргументи:
перші 2 - числа, третій - операція (+, -, *, /),
яка повинна бути проведена над ними.
У випадку невідомої операції, функція повертає рядок Unknown operation.
Результатом має бути дійсне число з двома знаками після десяткової крапки.
________________________________________
Вхідні дані:
3
8
+
Вихідні дані:
11.00
"""
def calculator(num1: float, num2: float, operation: str):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return 'Ділити на 0 не можна !'
        result = num1 / num2
    else:
        return 'Щось ти зробив не так'
    return f'{result:.2f}'

num1 = float(input('Введіть перше число: '))
num2 = float(input('Введіть друге число: '))
operation = input('Введіть операцію (+, -, *, /): ')

print(calculator(num1, num2, operation))


"""Завдання №2
Створіть функцію is_palindrome, яка приймає рядок і перевіряє, 
чи вона є паліндромом. Паліндромом називається рядок, 
який читається однаково як зліва направо, так і праворуч наліво. 
Функція повинна повертати булевне значення (True or False).
"""
def is_palindrome(s: str):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
s = input('Введіть текст: ')

print(is_palindrome(s))

"""Завдання №3
Напишіть функцію для створення позначок тегів HTML навколо введених рядків. 
Функція отримує назву тега HTML і рядок, який необхідно помістити у відповідні теги.
________________________________________
Вхідні дані:
strong Python
Вихідні дані:
<strong>Python</strong>
"""
def wrap_in_tag(tag: str, text: str):
    return f'<{tag}>{text}</{tag}>'

tag = input('Введи позначку тег: ')
text = input('Введи назву заголовок HTML: ')

print(wrap_in_tag(tag, text))


"""Завдання №4
Напишіть функцію is_prime, яка приймає число та перевіряє, 
чи воно є простим. Простим числом називається натуральне число, 
більше 1, яке немає дільників, крім 1 і себе.
"""

n = int(input('Введіть число: '))
print(is_prime(n))
#Але щось тут не виходить, щось я тут не зрозумів що ще потрібно вписати в код,
# щоб решта цифр могли визначатися чи вони прості

def is_prime(n: int):   # x -> [2; x-1]
    for div in range(2, n):
        if n% div == 0:
            return False
    return True
n = int(input('Введіть цифру: '))
print(is_prime(n))


"""Завдання №5
Реалізуйте функцію count_vowels_consonants, яка приймає рядок та 
підраховує кількість голосних та приголосних літер у цьому рядку.
"""
def count_vowels_consonants(text: str):
    vowels = set('aeiouAEIOUуеїіаоєяиюУЕЇІАОЄЯИЮ')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZйцкнгшщзхфвпрлджчсмтьбЙЦКНГШЩЗХФВПРЛДЖЧСМТЬБ')

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return {
        "vowels": vowel_count,
        "consonants": consonant_count
    }
text = input('Введіть текст: ')
print(count_vowels_consonants(text))