
                    #Home Work

"""
1.Спочатку користувач обирає, скільки чисел треба ввести.
Потім, вводить ці числа. Програма каже, яке число наразі вводиться
(Приклад: «Введіть число 5: »).
Результатом виведіть всі числа користувача через пробіл.
"""
count = int(input("Скільки чисел потрібно ввести? "))
numbers = []
for i in range(1, count + 1):
    number = input(f"Введіть число {i}: ")
    numbers.append(number)
for number in numbers:
    print(number, end=" ")

"""
2.Користувач вводить текст. 
Порахуйте кількість голосних літер в цьому тексті.
"""
text = input("Введіть текст: ")
vowels = "аеєєиіїоуюяАЕЄЄИІЇОУЮЯeyuioaEYUIOA"
counter = 0
for char in text:
    if char in vowels:
        count += 1
print(f'Кількість голосних літер у тексті: {counter}')

"""
3.** Дан будь-який текст. Користувач вводить кількість літер(довжину). 
Порахуйте, скільки слів такої довжини є у тексті. 
Приклад: у тексті «Привіт, як твої справи? У мене все ок.» 
2 слова довжиною 4 літери. 
"""
text = input("Введіть текст: ")
length = int(input("Введіть кількість літер (довжину слів): "))
count = 0
word = ""
for char in text:
    if char.isalpha():  
# Перевіряє якщо символ це літера (знайшов в інтернеті, що є така функція!!!)
        word += char
    else:
        if len(word) == length:
            count += 1
        word = ""
if len(word) == length:
    count += 1
print(f'{count} слова довжиною {length} літери')

"""
4.*** Написати гру "Вгадай число". 
Програма загадує число в діапазоні від 1 до 100. 
Користувач намагається його вгадати. 
Після кожної спроби програма видає підказки: 
більше чи менше його число, ніж загадане. 
Наприкінці програма видає статистику: 
за скільки спроб вгадано число, скільки часу це зайняло. 
Передбачити вихід по 0 у разі, якщо користувачеві набридло вгадувати число.
Примітка до ДЗ: Завдання з написанням гри "Вгадай число" міняємо на наступне: 
Замість "Число більше" та "Число менше", 
програма повинна видавати "Холодно", "Тепло", "Жарко" і тд. 
в залежності від різниці чисел. 
Фактичну відстань двох чисел можна перевірити за допомогою 
abs() Функція повертає додатній результат, навіть якщо різниця від'ємна.
"""
import random
import time

play_again = 'y'
while play_again == 'y':
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    while True:
        try:
            user_number = int(input("Вгадайте число від 1 до 100 (або введіть 0 для виходу): "))
        except ValueError:
            print("Будь ласка, введіть правильне число.")
            continue
        if user_number == 0:
            print("Ви вийшли з гри.")
            break
        attempts += 1
        difference = abs(secret_number - user_number)
        if difference == 0:
            end_time = time.time()
            result_time = round(end_time - start_time, 2)
            print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб(и) і {result_time} секунд.")
            break
        elif difference <= 5:
            print("Прям в ядрі сонця ))!")
        elif difference <= 10:
            print("Близько до корони сонця ))!")
        elif difference <= 15:
            print("Найспекотніше!")
        elif difference <= 20:
            print("Спекотно!")
        elif difference <= 25:
            print("Тепло!")
        elif difference <= 30:
            print("Ледь тепло.")
        elif difference <= 35:
            print("Ледь холодно.")
        elif difference <= 40:
            print("Холодно.")
        elif difference <= 45:
            print("Дуже холодно.")
        elif difference <= 50:
            print("Північний полюс.")
        elif difference <= 55:
            print("На висоті польоту літака")
        elif difference <= 60:
            print("Майже в космосі")
        else:
            print("Абсолютний нуль)).")
    play_again = input("y - зіграти ще: ")
