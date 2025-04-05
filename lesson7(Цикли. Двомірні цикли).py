
            #Варіант№1

end = int(input('Кінцеве число діапазону: '))
for number in range(1, end + 1):
    print(number)
    if number >= 500:
        print('Діапазон перебільшено!')
        break
    number += 1
else:
    print('ELSE')
#Запитання : Коли спрацьовує else у циклі?
#Виконується, якщо цикл не був перерваний оператором break

            #Варіант№2

end = int(input('Кінцеве число діапазону: '))
number = 1
while number <= end:
    print(number)
    if number >= 500:
        print('Діапазон перебільшено!')
    number +=1
else:
    print('ELSE')


for number in range(1, 100_001):
    if number %2 != 0:
        continue # створює умову, щоб не бачити print 
                 # + перекидає цикл на наступний крок (ітерацію)
                 # + else не потрібно писати
    print(number)


            #Завдання 1
#Користувач вводить текст та якийсь символ.
#Замістіть всі ці символи у тексті на "*"

text = input('Введіть текст: ')
find_char = input('Введіть символ для заміни на зірочку: ')
result = ''
for char in text:
    if char != find_char:
        result += char
    else:
        result += '*'
print(result)



            #Завдання 2 Варіант№1
#Завдання. Чи є цифра у тексті?
text = input('Введіть текст: ')
for char in text:
    if char in '0123456789':
        print('У тексті є цифри!')
        break
else:
    print('У тексті немає цифр!')

            #Завдання 2 Варіант№2
text = input('Введіть текст': ')
for char in text:
    if char in '0123456789':
        print(f'У тексті є цифри!', {char})
        break
else:
    print('У тексті немає цифр!')    



import random
import time

computer_number = random.randint(1, 100) # рандомне число від 1 до 100 (включно)
attemps = 0 # кількість спроб (з якої спроби вгадав число) '0' - бо буде функція додавання спроб
start_time = time.time() # фіксуємо поточний час
while True:
    user_number = int(input('Я загадав число від 1 до 100, вгадай його: '))
    attemps += 1
    if computer_number > user_number:
        print('Моє число більше!')
    elif computer_number < user_number:
        print('Моє число менше!')
    else:
        end_time = time.time() # фіксуємо час закінчення
        result_time = round(end_time - start_time, 2) 
        # заміряємо, скільки секунд між двома часовими мітками

        print(f'Ти вгадав! Моє число: {computer_number}!')
        print(f'Ти вгадав за {attemps} спроб!')
        print(f'Час проходження: {result_time} секунд!')
        break


"""
Завдання: зробіть так, щоб після проходження гри, 
користувачу пропонувалося зіграти ще,
якщо він погоджується, гра перезапускається з новим числом
"""


import random
import time

play_again = 'y'
while play_again == 'y':

    computer_number = random.randint(1, 4) # рандомне число від 1 до 4 (включно)
    attemps = 0 # кількість спроб (з якої спроби вгадав число) '0' - бо буде функція додавання спроб
    start_time = time.time() # фіксуємо поточний час
    while True:
        user_number = int(input('Я загадав число від 1 до 4, вгадай його: '))
        attemps += 1
        if computer_number > user_number:
            print('Моє число більше!')
        elif computer_number < user_number:
            print('Моє число менше!')
        else:
            end_time = time.time() # фіксуємо час закінчення
            result_time = round(end_time - start_time, 2)
            # заміряємо, скільки секунд між двома часовими мітками

            print(f'Ти вгадав! Моє число: {computer_number}!')
            print(f'Ти вгадав за {attemps} спроб!')
            print(f'Час проходження: {result_time} секунд!')
            break
play_again = input('y - зіграти ще: ')



for x in range(1, 11): # зовнішній цикл
    print('x=', x)
    print('-------------')
    for y in range(1, 11): # внутрішній цикл
        print('y=', y)

         # Завдання 1
"""
1.	Підрахувати кількість цілих чисел у діапазоні від 100 до 999,
у яких є дві однакові цифри.
"""
        #variant1

count = 0
for number in range(100, 1000):
    digits = str(number)
    first_digit = digits[0]
    second_digit = digits[1]
    third_digit = digits[2]
    if first_digit == second_digit or second_digit == third_digit or first_digit == third_digit:
        count += 1
print(f'Кількість чисел з двома однаковими цифрами: {count}') #Відповідь 252


        #variant2

counter = 0
for number in range(100, 1000):
    memory = ''
    for digit in str(number):
        if digit not in memory:
            memory += digit
        else:
            counter += 1
            break
print(counter)


        #variant3

number = str(number)
if len(number) != len(set(number)):
    counter +=1
print(counter)


        # Завдання 2
"""
2.Підрахувати кількість простих чисел у діапазоні від 2 до 100
"""
        #variant1

counter = 0
for number in range(2, 101):
    proste_number = 2
    while proste_number < number:
        if number % proste_number == 0:
            break
        proste_number += 1
    else:
        counter += 1
print("Кількість простих чисел від 2 до 100: ", counter)

        #variant2

counter = 0
for number in range(2, 100):
    for divider in range(2, number):
        if number % divider == 0:
            break
    else:
        counter += 1
        print(number)
print(f'Загальна кількість: {counter}')


        # Завдання 3
"""
Користувач вводить будь-яке ціле число. 
Необхідно з цього цілого числа видалити всі цифри 3 і 6 
і вивести назад на екран.
"""

number = input('Введіть ціле число: ')
result = ''
for digit in number:
    if digit not in ('3', '6'):
        result += digit
print('Результат:', result)


        # Завдання 4
"""
Користувач вводить із клавіатури дві межі діапазону та число. 
Якщо число не потрапляє в діапазон, 
програма просить користувача повторно ввести число і так доти, 
доки він не введе число правильно. 
Програма відображає всі числа діапазону, 
виділяючи число знаками оклику («1 2 3 !4! 5 6»).
"""

start = int(input('Введіть початок діапазону: '))
end = int(input('Введіть кінець діапазону: '))
R = range(start, end + 1)
while True:
    user_number = int(input('Введіть число з вашого діапазону: '))
    if user_number in R:
        break
for number in R:
    if number != user_number:
        print(number, end =' ')
    else:
        print(f'!{number}!', end=' ')


        # Завдання 5
"""
Вивести на екран таблицю множення в діапазоні, 
зазначеному користувачем. 
Наприклад, якщо користувач вказав 3 і 5, 
таблиця може виглядати так:
3*1 = 3 3*2 = 6 3*3 = 9 ... 3*10 = 30
.......................................
5*1 = 5 5*2 = 10 5*3 = 15 ... 5*10 = 50
"""

start = int(input('Введіть початок діапазону: '))
end = int(input('Введіть кінець діапазону: '))

for i in range(start, end + 1):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}', end='  ')
    print()
