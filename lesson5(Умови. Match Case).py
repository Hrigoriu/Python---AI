
day = int(input('Введіть номер для тижня (1-7): '))
if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Помилка! Введіть число від 1 до 7")
from calendar import day_name



day = int(input('Введіть номер для тижня (1-7): '))
match day:
    case 1:
        print('Понеділок')
    case 2:
        print('Вівторок')
    case 3:
        print('Середа')
    case 4:
        print('Четвер')
    case 5:
        print("П'ятниця")
    case 6:
        print('Субота')
    case 7:
        print('Неділя')
    case _:   # аналог else
        print('Такого дня тижня не існує')


login = input('Введіть логін: ')
password = input('Введіть пароль: ')

match login:
    case 'admin' if password == 'qwerty123': # login == 'admin' and password == 'qwerty123' 
        print('Welcome')
    case _:
        print('Доступ заборонено!')


'''
Користувач вводить номер місяця (1-12)
Поверніть відповідну пору року (Зима, Літо, Осінь, Весна)
Виконайте завдання через match case
'''


month = int(input('Введіть номер місяця (1-12): '))
match month:
    case 12 | 1 | 2:  # | читається як or
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')
    case 6 | 7 | 8:
        print('Літо')
    case 9 | 10 | 11:
        print('Осінь')
    case _:
        print('Такого місяця не існує!')


''' 
Користувач вводить номер дня (1-365). 
Відомо, що рік починається з понеділка.
Виведіть відповідний день тижня.
'''


day = int(input('Введіть номер дня(1-365): '))
result = day % 7
if result == 0:
    print('Неділя')
elif result == 1:
    print('Понеділок')
elif result == 2:
    print('Вівторок')
elif result == 3:
    print('Середа')
elif result == 4:
    print('Четвер')
elif result == 5:
    print("П'ятниця")
elif result == 6:
    print('Субота')


day = int(input('Введіть номер дня(1-365): '))
result = day % 7
match day % 7: # порівнюємо в match остачу від ділення на 7
    case 0:
        print('Неділя')
    case 1:
        print('Понеділок')
    case 2:
        print('Вівторок')
    case 3:
        print('Середа')
    case 4:
        print('Четверг')
    case 5:
        print("П'ятниця")
    case 6:
        print('Субота')


'''
Користувач вводить символ (літеру алфавіту). 
Скажіть чи являється цей символ голосним або приголосним.
Якщо вводиться не 1 символ, то видайте помилку
'''


char = input('Введіть 1 літеру: ')
print(len(char))  # функція , що показує число кількість букв у слові

if len(char) != 1:
    print('ERROR! Ви ввели не одну літеру!!! ')
elif char in 'яаиоїіеєЯАИОЇІЕЄ':
    print('Літера голосна!')
elif char in 'йцкнгшщзхфвпрлджчсмтбьЙЦКНГШЩЗХФВПРЛДЖЧСМТБЬ':
    print('Літера приголосна!')
else:
    print('Ви ввели не літеру або літеру іншої мови!')


print('a' in 'abc') # True
print('h' in 'abc') # False
print('hell' in 'hello') # True
print('helL' in 'hello') # False


''' 
Користувач вводить шестизначне число. 
Скажіть чи являється це число щасливим?
Примітка: щасливим числом вважається число, 
де сума перших трьох цифр дорівнює сумі останніх трьох 
'''


#V1
number = input('Введіть шестизначне число: ')
if len(number) == 6:
    first_part = int(number[0]) + int(number[1]) + int(number[2])
    second_part = int(number[3]) + int(number[4]) + int(number[5])
    if first_part == second_part:
        print('Число щасливе!')
else:
    print('Число звичайне')
  

#V2
number = input('Введіть шестизначне число: ')
if len(number) == 6:
    first_part = int(number[0]) + int(number[1]) + int(number[2])
    second_part = int(number[3]) + int(number[4]) + int(number[5])
    print('Число щасливе' if first_part == second_part else "Число звичайне")
else:
    print('Ви ввели не шестизначне число')    
