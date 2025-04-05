"""
Завдання №1.	Заповніть список випадковими цілими числами (не менше десяти штук).
У цьому списку, потрібно визначити мінімальний і максимальний елементи,
порахувати кількість від'ємних елементів, порахувати кількість додатних елементів,
порахувати кількість нулів. Результати вивести на екран.
"""
import random
numbers = [random.randint(-100, 100) for _ in range(10)]
min_numbers = min(numbers)
max_numbers = max(numbers)
minus = 0
plus = 0
nul = 0
for num in numbers:
    if num < 0:
        minus += 1
    if num > 0:
        plus += 1
    if num == 0:
        nul += 1

print(f"Список чисел: {numbers}")
print(f"Мінімальний елемент: {min_numbers}")
print(f"Максимальний елемент: {max_numbers}")
print(f"Кількість від'ємних чисел: {minus}")
print(f"Кількість додатних чисел: {plus}")
print(f"Кількість нулів: {nul}")


"""
Завдання №2. Дан список з словами. Залиште в цьому списку лише слова, 
що починаються з великої літери.
"""
#Variant №1
words = ['Apple', 'banana', 'Cat', 'dog', 'Elephant', 'fox']
result = []
for word in words:
    if word[0].isupper():
        result.append(word)
print(f'Список після змін: {result}')

#Variant №2
words = ['Apple', 'banana', 'Cat', 'dog', 'Elephant', 'fox']
result = [word for word in words if word[0].isupper()]
print(f'Список після змін: {result}')


"""
Завдання №3. Дан список цілих чисел. Знайдіть в ньому ті числа, 
що з`являється непарну кількість разів.
"""
numbers = [1, 2, 1, 1, 2, 2, 2]
unique_numbers = []
result = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
for num in unique_numbers:
    count = 0
    for n in numbers:
        if n == num:
            count += 1
    if count % 2 == 1:
        result.append(num)

print(f'Список чисел: {numbers}')
print(f'Числа, що з`являються непарну кількість разів: {result}')

numbers = [1, 2, 1, 1, 2, 2, 2]
for el in numbers:
    print(numbers.count(el))

"""
Завдання №4. Дан список (types_list) з даними всіх основних типів, 
що є в Python. Перенесіть дані із types_list у нові списки, 
кожен з яких відповідає своєму типу даних 
(list_int, list_str, list_bool, list_float). 
В кожному списку повинні бути лише ті дані, яким він відповідає.
"""
types = [1, 'B', 234, 'text', False, True, 54.54]
list_int = []
list_str = []
list_bool = []
list_float = []

for el in types:
    if type(el) == int:
        list_int.append(el)
    elif type(el) == str:
        list_str.append(el)
    elif type(el) == bool:
        list_bool.append(el)
    elif type(el) == float:
        list_float.append(el)

print(f'Список цілих чисел: {list_int}')
print(f'Список рядків: {list_str}')
print(f'Список булевих значень: {list_bool}')
print(f'Список дробових чисел: {list_float}')


"""
Завдання №5. Напишіть програму, яка приймає два списки чисел 
від користувача і створює новий список, що містить суму елементів 
з однаковими індексами двох вихідних списків. Виведіть отриманий список
 на екрані. Передбачається, що списки мають однакову довжину. 
 Наприклад, якщо користувач вводить списки [1, 2, 3] та [4, 5, 6], 
 програма повинна вивести [5, 7, 9].
"""
list1 = input('Введіть перший список чисел через пробіл:')
new_list1 = list1.split()
super_new_list1 = []
for n in new_list1:
    super_new_list1.append(int(n))

list2 = input('Введіть другий список чисел через пробіл:')
new_list2 = list2.split()
super_new_list2 = []
for n in new_list2:
    super_new_list2.append(int(n))

if len(super_new_list1) != len(super_new_list2):
    print("Помилка: списки повинні мати однакову довжину!")
else:
    result = []
    for i in range(len(super_new_list1)):
        result.append(super_new_list1[i] + super_new_list2[i])

    print(f'Результат: {result}')