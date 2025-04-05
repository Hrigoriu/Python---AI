# Завдання №1
"""
Напишіть функцію to_uppercase, яка приймає рядок та повертає його
у верхньому регістрі.
"""
def to_uppercase(text):
    return text.upper()
print(to_uppercase("привіт"))
print(to_uppercase("Hello"))


# Завдання №2
"""
Напишіть функцію find_intersection, яка приймає два списки 
та повертає список, що містить елементи, які є в обох списках.
"""
def find_intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
print(find_intersection(list_a, list_b))


# Завдання №3
"""
Створіть функцію is_anagram, яка приймає два рядки та перевіряє, 
чи є вони анаграмами (мають однакові символи у різному порядку).
"""
def is_anagram(str1, str2):
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
print(is_anagram('Listen', 'Silent'))
print(is_anagram('Hello', 'World'))

