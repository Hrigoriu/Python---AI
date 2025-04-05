#text = input(' : ').upper().strip()
#Завдання 1
"""
Перевірь,
чи перше слово починається на ту ж букву,
на яку закінчується друге слово.
Python
Ruby
Враховуйте, що літери мають різний кейс,
тому переведіть всі слова в один регістр
"""
#variant1
word1 = input('Введіть слово №1: ').strip()
word2 = input('Введіть слово №2: ').strip()
result = word1[0].lower() == word2[-1].lower()
print(result)

#variant2
word1 = 'Python'.lower()
word2 = 'Ruby'.lower()
print(word1[0] == word2[-1])


#Завдання#2
"""
Заміни всі цифри "4" у тексті на слово "Four"
4 Christmases
Fantastic 4
The Nutcracker and the 4 Realms
"""
text = input('Введіть текст: ')
new_text = text.replace("4", "Four")
print(new_text)


#Завдання#3
"""
Введене слово-речення, де є цифри та літери. 
Видали всі цифри та виведи тільки 
букви й інші символи у тому ж порядку.
H1e2l3l4o5w6o7r8l9d
i1m3p4o9r0t4 6t7h8i9s
"""
#variant#1
line = input("Введіть слово-речення: ")
new_line = ''.join(char for char in line if not char.isdigit())
print(new_line)

#variant#2
text = 'H1e2l3l4o5w6o7r8l9d'
result = ''
for char in text:
    if not char.isdigit():
        result += char
print(result)


#Завдання#4
text = ' Lorem ipsum is   a dummy or   placeholder text  '
print(' '.join(text.split()))


#Завдання#5
text = 'Lorem ipsum is a dummy or placeholder text'
print(text.count(' '))


#Завдання#6
text = 'Lorem ipsum is a dummy or placeholder text commonly used in graphic design, publishing, and web development to fill empty spaces in a layout that does not yet have content.'
n = int(input('Введіть n: '))
print(text[:n].upper() + text[n:])