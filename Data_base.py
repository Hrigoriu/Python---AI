user_name = 'Bob'   = це присвоєння або створення змінної user_name з значенням 'Bob'
'Hello, ' + user_name + '!' # контамінація , склеювання слів , значок +
input - це ВВІД інформації в консоль

print(10 * 5)    # * -  множення
print(5 ** 3)    # ** - степінь
print(10 / 5)    # / -  ділення, покаже і після коми
print(11 // 3)   # // - цілочислене ділення - повертає тілу частку від ділення # покаже 3, нічого після коми (11/9=3)
print(10 % 3) # буде 1 (10-9=1)
print(11 % 3) # буде 2 (11-9=2)

print(text_2 + '20') #буде 1020, відбудеться склеювання, бо + для строк склеювання (contcatenate)

print(a, b, c, end='  |новий print|') # end - склеює цей рядок з наступним, тобто виведе рядок виводить -- 10 20 30  |новий print|a,b,c
print('a', 'b', 'c', sep=',') #/ виставить між аргументами коми
print('a', 'b', 'c', sep='') # sep - строка, яка ставиться МІЖ аргументами print
print('1\n2\n3\n4\n5')  # \n - перекидає на наступний абзац між аргументами
print(a, b, c, end='\n') # це по замовчуванню стоїть, але система не показує, система перекидає на новий рядок

print(number1)    # NameError - звертаємось до змінної, якої не існує
 print(number_1)   # IndentionError - зайвий абсзац або пробіл на початку рядка
print(number_1 + '!')  # TypeError - операція між різними типами даних (конфлікт типів даних)
var = 'Hi' = 5 # SyntaxError  - груба синтаксична помилка
text = 'Hello  # SyntaxError  - груба синтаксична помилка

#Типи даних
string = '10'    # str (строка) - текстовий літерал або послідовність символів
integer = 10     # int - ціле число
float_ = 10.10   # float - дробове десятичне число
boolean = True   # bool  - логічний тип даних: True(Істина, Так, 1); False(Брехня, Ні, 0)
none = None      # None  - відсутній тип даних

input() завжди повертає STR

#Перетворення
-на  str - (фактично майже завжди просто накладає лапки на об'єкт)
print(str(10) + '!')
print(str(True) + '.')
-на  int
print(int('10') + 1)
Виведе : 11
print(int('abc'))
Виведе  ValueError, бо таку строку не можна перетворити на число

int(input('Введіть число 2: ')) #- це перетворення на число int
str(sum_of_numbers) - це перетворення на строку str

# Порівняння чисел
print(20 > 10)  #True
print(20 < 10)  #False
print(20 >= 20) # більше або дорівнює
print(10 <= 20) # менше або дорівнює
print(10 == 10.0) #Виведе True #дорівнює (порівнювання, чи однакове?, нагадую, що = це присвоєння)
print(25 != 25.0) #Виведе False #не дорівнює

#Порівняння строк
print('abc' > 'ABC') #True # на > < строки порівнюються за unicode
print(ord('A')) #65
print(ord('a')) #97
print('hello' == ' hello') #False
print('hello' == 'hello')  #True
print('abc' == 'acb') #False  #== строки порівнюються на ідентичність
print('25' != '25.0')  #False

#Об'єднання порівнянь
i (and) потребує True всюди (зліва та справа)
print(True and True)   #True
print(False and False) #True
print(False and True)  #False

або (or) потребує True хоч десь
print(True or True)    #True
print(False or False)  #False
print(False or True)   #True
print(10 > 1 or 5 < 1) #True

#not - робить хибне твердження правдивим, повертає навпаки, розвертає твердження навпаки
print(not True) #False
print(not False) #True
print(not 10 >= 20) #True

Структура умови:
- 1 if:
- скільки завгодно elif (0 також): (Перевіряються по черзі)
- 0 або 1 else:

                #Умови
if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
    feed_the_sheepdogs()
===============================
if the_weather_is_good: # Якщо
    go_for_a_walk()
    have_fun()
else:                   # Якщо не виконується 1 умова, то
    go_to_a_theater()
    enjoy_the_movie()
    have_lunch()
===============================
if the_weather_is_good: # Якщо
    if nice_restaurant_is_found:
        have_lunch()
    else:               # Якщо не виконується 1 умова, то
        eat_a_sandwich()
else:                   # Якщо не виконується 1 умова, то
    if tickets_are_available:    # Якщо
        go_to_the_theater()
    else:                        # Якщо не виконується 1 умова, то
        go_shopping()
================================
if the_weather_is_good: # Якщо 1 умова
    go_for_a_walk()
elif tickets_are_available:  # Якщо 1 умова + 2 умова
    go_to_the_theater()
elif table_is_available:     # Якщо 1 умова + 2 умова + 3 умова
    go_for_lunch()
else:                  # В інших випадках
    play_chess_at_home()

            #WHILE (ПОКИ)
# ПОКИ <умова == Істина>: <код>
number = 1
while True:  #while True - нескінченний цикл
    print(number)
    number +=1
==============================
number = 1
while 10>1:  #while True - нескінченний цикл
    print(number)
    number +=1
    if number > 100_000:
        break # - вихід з циклу

        #цикл for та функція range
for i in range(10): #(перебирає від 0 до 9)
 print("Значення i зараз дорівнює", i)
================================================================
for i in range(2, 8, 3): #(перебирає від 2 до 8, з корком 3)
 print("Значення i зараз дорівнює", i)

        #функція break та continue
# приклад break
print("Інструкція break:")
for i in range(1, 6):
    if i == 3:
        break   # Зупиняє цикл і все
    print("Всередині циклу.", i)
print("За межами циклу.")
======================================
# приклад continue
print("Інструкція continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Всередині циклу.", i)
print("За межами циклу.")

"""
    Синтаксис range() має наступний вигляд: range(start, stop, step),де:
*start ‒ необов`язковий параметр, що задає початковий номер послідовності
        (за замовчуванням 0)
*stop ‒ необов`язковий параметр, що вказує на кінець згенерованої послідовності
        (не входить до складу),
*step ‒ необов`язковий параметр, що задає крок інтервалу між числами в послідовності
        (за замовчуванням ‒ 1).
"""
Ітерація - це повторення одного порядку дій через якусь послідовність.
_iterable - властивість об'єктів, що дозволяють їм ітеруватись
for char in text:  # ітерація строки (str)
    print(char)

n = int(input('Введіть число: '))
for n in range(1, n+1):  # range не включає останнє число
    print(n, '#' * n)

n = int(input('Введіть число: '))
for n in reversed(range(1, n+1)):  # range не включає останнє число
    print(n, '#' * n)

abs() Функція повертає додатній результат, навіть якщо різниця від'ємна.

    Функція: max() , min()
# Зчитайте три числа
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
number3 = int(input("Введіть третє число: "))
# Перевір, яке з чисел найбільше
# і передайте його largest_number variable.
largest_number = max(number1, number2, number3)
small_number = min(number1, number2, number3)
# Виведіть результат
print("Найбільше число це:", largest_number)
print("Найбільше число це:", small_number)

print(3E8) #Виведе: 100000000.0
print(0.0000000000000000000001) #Виведе: 1e-22

    Функція round(number, int), int округлить до числа після коми
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "миль це", round(miles_to_kilometers, 2), "кілометрів")
print(kilometers, "кілометрів це", round(kilometers_to_miles, 2), "миль")

""" 
    Комп`ютерна логіка
Різниця в роботі логічних і бітових операторів важлива: 
логічні оператори не проникають на бітовий рівень свого аргументу. 
Їх цікавить лише кінцеве ціле число.
    Логічні оператори
Оператор логічної кон`юнкції у мові Python є слово and
Оператор логічної диз`юнкції у мові Python є слово or
унарний оператор not
    Побітові оператори
& (амперсанд) ‒ побітова кон'юнкція;
| (риска) ‒     побітова диз'юнкція;
~ (тильда) ‒    побітове заперечення;
^ ( каретка ) ‒ побітове виключення або (xor).
& потрібно рівно дві 1,         щоб отримати в результаті 1;
| повинна мати хоча б одну 1,   щоб отримати в результаті 1;
^ повинна мати тільки одну 1,   щоб отримати в результаті 1;
Додамо важливе зауваження: аргументи цих операторів повинні бути цілими числами int,
тут не можна використовувати оператори з рухомою крапкою (float).
"""

    #Функція len()
length - довжина
len() - перевіряє поточну довжину списку [1, 2.0, 'dog'],
n = [1, 2.0, 'dog']
print(len(n))
# Видалення другого елементу зі списку, по індексу
del numbers[1]

Стандартний виклик функції може виглядати таким чином:
result = function(arg)
result = data.method(arg)
#Новий елемент можна додати до кінця існуючого списку
list.append(value)
#Новий елемент можна додати в будь-яке місце списку, а не тільки в кінець.
list.insert(location, value)
===============================
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
4
[111, 7, 2, 1]
###
numbers.append(4)
print(len(numbers))
print(numbers)
5
[111, 7, 2, 1, 4]
###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)
6
[222, 111, 7, 2, 1, 4]
===========================
my_list = [] # Створення порожнього списку.
for i in range(5):
    my_list.append(i + 1)
print(my_list)
[1, 2, 3, 4, 5]
###
my_list = []  # Створення порожнього списку.
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)
[5, 4, 3, 2, 1]
### Заміна місцями аргументів по індексу
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
[5, 3, 8, 1, 10]

    #list() Списки
*Сортування:
-sort()
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)   #[2, 4, 6, 8, 10]
-reverse()
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  #  [4, 2, 1, 3, 5]

*Зріз
my_list[start:end]  від start до end - 1
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) # [8, 6]
=========================
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) # [8, 6, 4]

#my_list[start:] == my_list[start:len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list  # [4, 2]
# del
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]


    ##Функції
def function_name():
    function_body
------------------------------------
def message():
    print("Введіть значення: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
-------------------------------------
def hello(name):  # визначення функції
    print("Привіт,", name)  # тіло функції
name = input("Введіть своє ім'я: ")
hello(name)  # виклик функції

