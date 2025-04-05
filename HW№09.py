#Завдання№1
"""
1.Напишіть програму, що замінює всі великі літери у тексті,
що вводить користувач, на зірочки(«*»).
"""
text = input('Введіть текст: ')
new_text = ''.join('*' if char.isupper() else char for char in text)
print("Результат:", new_text)
#print(f'Результат: {new_text}')

#Завдання№2
"""
2.Дано рядок нулів та одиниць. 
Напишіть програму для знаходження найдовшої неперервної 
послідовності нулів у рядку.
________________________________________
Вхідні дані:
1001
100001001010
1000001
Вихідні дані:
2
4
5
"""
zero_one = input("Введіть рядок з 0 і 1: ")
zero_all = zero_one.split('1')
max_zeros = max(len(char) for char in zero_all)
print(max_zeros)


#Завдання№3
"""
3.Напишіть програму, що приймає строку від користувача та знаходить:
a.	Символ, що трапляється найбільшу кількість разів.
b.	Кількість знаків пунктуації.
c.	Літери алфавіту, що не були знайдені у тексті.
d.	Кількість унікальних символів 
(тобто, загальна кількість елементів строки, що не повторюються).
"""
text = input("Введіть текст: ").lower()
#a. підпункт не зрозумів логічну послідовність як створити,
    # не зумів вірно написати, багато варіантів було не вірно

max_char = ''
max_count = 0
for char in text:
    if text.count(char) > max_count:
        max_count = text.count(char)
        max_char = char

max_char = max.(text, key=lambda el: text.count(el)) # ><

print(f'Символ, який трапляється який,трапляється: {max_char} ({max_count})')


alphabet = "абвгґдеєжзийклмнопрстуфхцчшщьюяabcdefghijklmnopqrstuvwxyz"
missing_letters = ""
for char in alphabet:
    if char not in text:
        missing_letters += char
print(f'Літери, що не зустрічаються: {','.join(missing_letters)}')

punctuation = ".,!?;:-()\"'«»—[]{}/"
punctuation_count = 0
for char in text:
    if char in punctuation:
        punctuation_count += 1
print(f'Кількість знаків пунктуації: {punctuation_count}')

unique_chars = ''
for char in text:
    if char not in unique_chars:
        unique_chars += char
print(f'Кількість унікальних символів: {len(unique_chars)}')

#Завдання№4
"""
4.Дано два слова. Складіть програму, 
що визначає чи можна чи ні з букв слова A скласти слово B. 
Програма не має враховувати регістр літер введених слів.
________________________________________
Вхідні дані:
not
Ruby
Buy
Python
Typhon

Вихідні дані:
Yes
No
"""
word1 = input("Введи перше слово: ").lower()
word2 = input("Введи друге слово: ").lower()

new_word = True
for simbol in word2:
    if simbol not in word1:
        new_word = False
        break

    count1 = 0
    for char in word1:
        if char == simbol:
            count1 += 1
    count2 = 0
    for char in word2:
        if char == simbol:
            count2 += 1

    if count1 < count2:  # Якщо в word_a менше літер ніж треба
        new_word = False
        break
if new_word:
    print('Yes')
else:
    print('No')

#Завдання№5
"""
5.*Напишіть програму, яка зчитує рядок, кодує її 
запропонованим алгоритмом і виводить закодовану послідовність. 
Кодування повинно враховувати регістр символів. 
Правила кодування: групи однакових символів початкового рядка 
замінюються на цей символ і кількість його повторень в цій позиції рядка. 
Наприклад: рядок aaaabbbсaa кодується в a4b3с1a2.
"""

# Це складно, навіть уявити важко який там алгоритм
# Можливо пізніше колись подолаю таку складність


"""
import itertools
a = [5, 6, 7, 8]
b = [10, 11, 12, 13]
c = []

#V#1

for index in range(len(a)):
    c.append(a[index] + b[index])
print(c)

#V#2
for el in zip(a, b):
    c.append(sum(el))

c = [sum(el) for el in zip (a, b)]
print(c)

#V#3
for el in itertools.zip_longest(a, b)
    print(el)

string1 = 'abcdefgh'
string2 = '12345678'
print(''.join(''.join(t) for y in zip(string1, string2)))
"""