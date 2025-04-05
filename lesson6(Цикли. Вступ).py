                 #Цикли
"""
Ітерація - це повторення одного порядку дій через якусь послідовність.
_iterable - властивість об'єктів, що дозволяють їм ітеруватись
"""
                 #WHILE (ПОКИ)
# ПОКИ <умова == Істина>: <код>
"""
Надрукувати від 1 до 100 тис.
"""
number = 1
while number <= 1000_000:  
    print(number)   #крок циклу - 1 виконання всього його коду (1 ітерація)
    number += 1 # значок += додає 1 до number
    print('Hello, world!') #якщо з абзацу, то буде друкувати після кожної цифри
print('Hello, Ukraine!') #якщо без абзацу, то буде друкувати в кінці циклу

# Hello, world!
# 999999
# Hello, world!
# 1000000
# Hello, world!
# Hello, Ukraine!

number = 1
while True:  #while True - нескінченний цикл
    print(number)
    number +=1

number = 1
while 10>1:  #while True - нескінченний цикл
    print(number)
    number +=1
    if number > 100_000:
        break # - вихід з циклу


'''
# ітерація строки по індексу, тобто після кожної букви 
# йде print, тобто абзац і слово пишеться по вертикалі
'''
text = input('Text: ') # 'Hell0' last index 4, len 5
index = 0
while index < len(text): 
    print(text[index])
    index += 1


            #FOR (ДЛЯ)
# ДЛЯ <частина> з <об'єкт>: <цикл>

for number in range(1, 11): # 1 - старт, 11 - кінець, 11 не пишиться, до цієї цифри
    print(number)


text = input('Text: ')
for index in range(len(text)):
    print(text[index])

for char in text:  # ітерація строки (str)
    print(char)

# Задача: користувач вводить строку.
# Порахуйте кількість голосних літер

text = input('Text: ')
counter = 0
for char in text:
    if char in 'OIUYEAoiuyea':
        counter += 1
print(f'Кількість голосних літер: {counter}')


#1
n = int(input('Введіть число: '))
for _ in range(n):
    print('Hello, Python!')


#2
n = int(input('Введіть число: '))
for n in range(1, n+1):  # range не включає останнє число
    print(n, '#' * n)

n = int(input('Введіть число: '))
for n in reversed(range(1, n+1)):  # range не включає останнє число
    print(n, '#' * n) 


#3
n = int(input('Введіть число: '))
for n in range(1, n + 1):
    print(str(n) * n)  


'''
4. Є правильний логін та пароль Користувач вводить логін та пароль, 
поки не напишете їх правильно. Якщо логін або пароль неправильний,
виводимо повідомлення про це та повторюємо ввід
'''
true_login = 'admin'
true_password = 'qwerty123'

while True:
    login = input('LOGIN: ')
    password = input('PASSWORD: ')

    if login == true_login and password == true_password:
        print('WELCOME')
        break
    else:
        print('Дані неправильні!!!!')
