Завдання №1
number = int(input("Введіть число: "))
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

Завдання №2
day = int(input("Введіть номер дня тижня (1-7): "))
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

Завдання №3
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

print("\nОберіть операцію:")
print("1 - Максимум")
print("2 - Мінімум")
print("3 - Середнє арифметичне")

choice = int(input("Ваш вибір (1-3): "))

if choice == 1:
    max_num = max(num1, num2, num3)
    print(f"Максимум: {max_num}")
elif choice == 2:
    min_num = min(num1, num2, num3)
    print(f"Мінімум: {min_num}")
elif choice == 3:
    avg = (num1 + num2 + num3) / 3
    print(f"Середнє арифметичне: {avg}")
else:
    print("Щось пішло не так! Виберіть число від 1 до 3")

Завдання №4
name = input("Введіть ваше ім'я: ")
number = int(input("Введіть число: "))

if number % 2 == 0:
   print(f"Привіт, {name}")
elif number % 2 != 0 and number % 3 == 0:
   print(number ** 2)
else:
   print(f"Допобачення, {name}")

Завдання №5
number = float(input("Введіть число: "))
if number % 1 == 0:
   result = int(number)
else:
   result = number
print(f"Результат: {result}")