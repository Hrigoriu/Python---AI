
bool_tru = True    # Істина, 1
bool_false = False # Брехня, 0

# Порівняння чисел
print(20 > 10)  #True
print(20 < 10)  #False
print(20 >= 20) # більше або дорівнює
print(10 <= 20) # менше або дорівнює
print(10 == 10.0) # дорівнює (порівнювання, а = це присвоєння)
print(25 != 25.0) # не дорівнює

#Порівняння строк
print('abc' > 'ABC') #True # на > < строки порівнюються за unicode
print(ord('A')) #65
print(ord('a')) #97

print('hello' == ' hello') #False
print('hello' == 'hello') #True
print('abc' == 'acb') #False  #== строки порівнюються на ідентичність
print('25' != '25.0')  #False

#Об'єднання порівнянь
# i (and) потребує True всюди (зліва та справа)
print(True and True)
print(False and False)
print(False and True) #False

# або (or) потребує True хоч десь
print(True or True) #True
print(False or False) #False
print(False or True) #True
print(10 > 1 or 5 < 1) #True

#not - робить хибне твердження повертає навпаки, розвертає твредження навпаки
print(not True) #False
print(not False) #True

print(not 10 >= 20) #True

'''
Задача : користувач вводить в консоль число. 
Результат поверніть: 
-Число більше нуля
-Число менше нуля
-Число дорівнює нуля
'''
number = int(input('Введіть число: '))

if number > 0: #  якщо <умова == True>: <код>
    print('Число більше нуля')
elif number < 0: # в іншому випадку, якщо <умова == True>: <код>
    print('Число менше нуля')
elif number == 0:
    print('Число дорівнює нуля')
else: # в усіх інших випадках: <код>
    print('Число дорівнює нуля')

'''
Структура умови:
- 1 if:
- скільки завгодно elif (0 також): (Перевіряються по черзі)
- 0 або 1 else: 
'''
number = int(input('Введіть число: '))

if number > 0: #  якщо <умова == True>: <код>
    print('Число більше нуля')
if number < 0: # в іншому випадку, якщо <умова == True>: <код>
    print('Число менше нуля')
elif number == 0:
    print('Число дорівнює нуля')
else: # в усіх інших випадках: <код>
    print('Число дорівнює нуля')
# Напише
# Число більше нуля
# Число дорівнює нуля

   #Завдання №1
#Варіант1
true_login = 'admin'
true_password = 'qwerty123'

login = input('Login: ')
password = input('Password: ')

if login == true_login and password == true_password:
    print("Все гаразд.")
else:
    print("Вибачте, щось пішло не так!!!")

#Варіант2
true_login = 'admin'
true_password = 'qwerty123'

login = input('Login: ')
password = input('Password: ')
if login == true_login:
    if password == true_password:
    print("Все гаразд.")
    print("Все гаразд.")
else:
    print("Вибачте, щось пішло не так!!!")

else:
    print("Вибачте, щось пішло не так!!!")

#Завдання #2

grade1 = int(input('Введіть оцінку 1: '))
grade2 = int(input('Введіть оцінку 2: '))
grade3 = int(input('Введіть оцінку 3: '))
average_grade = (grade1 + grade2 + grade3) / 3
average_grade = round(average_grade, 2) # округлення до 2-х знаків після коми
print(f'Ваш середній бал: {average_grade}')

if average_grade >= 95:
    print('Гарний результат!')
else:
    print('Тебе відраховано((')

'''
Завдання #3
Користувач вводить рік (наприклад, 2014)
Перевірте та виведіть чи являється цей рік високосним.
Високосним є рік, що ділиться на 4 та не ділиться на 100.
Винятком є роки, що діляться на 400.
Такі роки теж є високосними.
Підказка: число ділиться на інше число, якщо остача від ділення - 0 (%)
'''
year = int(input('Введіть рік: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Рік високосний')
else:
    print('Рік звичайний')

#Завдання №4
banknota = int (input('Введіть номінал гривні: '))
match banknota:
    case 1:
        print(f"{banknota}, Володимир Великий")
    case 2:
        print(f"{banknota}, Ярослав Мудрий")
    case 5:
        print(f"{banknota}, Богдан Хмельницький>")
    case 10:
        print(f"{banknota}, Іван Мазепа")
    case 20:
        print(f"{banknota}, Іван Франко")
    case 50:
        print(f"{banknota}, Михайло Грушевський")
    case 100:
        print(f"{banknota}, Тарас Шевченко")
    case 200:
        print(f"{banknota}, Леся Українка")
    case 500:
        print(f"{banknota}, Григорій Сковорода")
    case 1000:
        print(f"{banknota}, Володимир Вернадський")
    case _:
        print("Будь ласка введіть правильну банкноту")