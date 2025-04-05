
            #Типи даних

string = '10'    # str (строка) - текстовий літерал або послідовність символів
integer = 10     # int - ціле число
float_ = 10.10   # float - дробове десятичне число
boolean = True   # bool - логічний тип даних: True(Істина, Так, 1); False(Брехня, Ні, 0)
none = None      # None - відсутній тип даних


a = input()
result = print(input)
print(result)

result = print('Hi')
print(result)

# Задача
num_1 = input('Введіть число 1: ') # input () завжди повертає STR
num_2 = input('Введіть число 2: ')
#
sum_of_numbers = num_1 + num_2
print('Сума чисел: ' + sum_of_numbers)
# Виведе
# Введіть число 1: 10
# Введіть число 2: 25
# Сума чисел: 1025

#Перетворення

### на  str - (фактично майже завжди просто накладає лапки на об'єкт)
print(str(10) + '!')
print(str(True) + '.')

### на  int
print(int('10') + 1)
Виведе : 11

print(int('abc'))
Виведе  ValueError, бо таку строку не можна перетворити на число

print(int('10_000_000'))
# Виведе 10000000
n=0_0_0_0_0_0_0 # можна розділяти цифри  '_'

print(int(9.99)) #9 , бо це не округлення
print(int(False)) #0
print(int(True)) #1

### на bool - True , якщо об'єкт НЕ порожній
print(bool(1))   True
print(bool(-5))  True
print(bool(0))  False

print(bool('False')) # True
print(bool(''))  #False
print(bool(' '))    # True
print(bool(None)) #False

num_1 = input('Введіть число 1: ') # input () завжди повертає STR
num_2 = input('Введіть число 2: ')

sum_of_numbers = int(num_1) + int(num_2)
print('Сума чисел: ' + str(sum_of_numbers))

num_1 = int(num_1)
num_2 = int(num_2)
sum_of_numbers = num_1 + num_2
print('Сума чисел: ' + str(sum_of_numbers))

num_1 = int(input('Введіть число 1: ')) #int- це перетворення на число int
num_2 = int(input('Введіть число 2: ')) #- це перетворення на число int
sum_of_numbers = int(num_1) + int(num_2)
print('Сума чисел: ' + str(sum_of_numbers)) - це перетворення на строку str
# Виведе
# Введіть число 1: 25
# Введіть число 2: 40
# Сума чисел: 65

num_1 = int(input('Введіть число 1: ')) #- це перетворення на число int
num_2 = int(input('Введіть число 2: ')) #- це перетворення на число int
sum_of_numbers = int(num_1) + int(num_2)
print(f'Сума чисел: {sum_of_numbers}')
# # Виведе
# Введіть число 1: 45
# Введіть число 2: 20
# Сума чисел: 65

print(0.6 / 2)
print(2.9 - 3)

string = "Hello" ,
індекс - це відстань від початку (H=0, e=1, l=2, l=3, o=4)
string = 'Hello, world!'
print(string[5]) # Виведе: ,

string = 'Hello, world!'
print(len(string)) # Виведе: 13

string = 'Hello, world!'
#Індекс - це відстань від початку (H=-5, e=-4, l=-3, l=-2, o=-1)

print(string[0:5]) #зріз від 0 до 4 (кінець не включається)
print(string[7:12]) #зріз від 7 до 11
print(string[5:])   #зріз від 5 до 11
print(string[7:-1])  # world

# #Завдання #1
#
# #  Дані
days = 1
hours = 16
minutes = 25
seconds = 50
# Перетворити в секунди
all_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
print(all_seconds)

days = int(input('Days: '))
hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))
total = (days*24*60*60) + (hours*60*60) + (minutes*60) + seconds
print(total)

# # #Завдання #2
price = 150
discount = 0.3
final_price = price - (price * discount)
print(final_price)

price = int(input('Price: '))
disc = float(input('Discount: '))
print(price - price * disc)


##Завдання #3
a = int(input('Введіть число 1: '))
b = int(input('Введіть число 2: '))
# a = 6
# b = 3

suma = a + b
minus = a - b
mnoz = a * b
dilen = a / b
stepin = a ** b
#
print(suma, "&", minus, "&", mnoz, "&", dilen, "&", stepin)
print(a + b, a - b, a * b, a / b, a ** b, sep='&')

#Завдання #4
# 17.9 - 0.9
# 1.066 - 0.066
# 0.01 - 0.01

number = float(input("Введіть дробове число: "))
drob_chislo = number % 1

print(f"Дробова частина числа: {drob_chislo}")

