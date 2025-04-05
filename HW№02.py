# Завдання №1
#Варіант №1
a = 1
b = 5
c = 7
a = int(input("Перша цифра: "))
b = int(input("Друга цифра: "))
c = int(input("Третя цифра: "))
number = a * 100 + b * 10 + c
print('Результат: ' + str(number))
#--------------------------------
# #Варіант №2
a = input("Введіть першу цифру: ")
b = input("Введіть першу цифру: ")
c = input("Введіть першу цифру: ")
number = int(a + b + c)
print("Отримане число: ", number)
#--------------------------------

# Завдання №2
number = input("Введіть чотиризначне число: ")
dobutok = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print("Добуток цифр:", dobutok)

# # Завдання №3
meters = float(input("Введіть кількість метрів: "))

miles = meters / 1609.34
decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print("У милях:", miles)
print("У дециметрах:", decimeters)
print("У сантиметрах:", centimeters)
print("У міліметрах:", millimeters)

# # Завдання №4
osnova = float(input("Введіть основу трикутника: "))
vusota = float(input("Введіть висоту трикутника: "))
ploscha = 0.5 * osnova * vusota
print(f"Площа трикутника: {ploscha}")       #варіант №1
print("Площа трикутника: " + str(ploscha))  #варіант №2
print("Площа трикутника: ", ploscha)        #варіант №3

# # # Завдання №5
number = input("Введіть чотиризначне число: ")
zvorot_number = number[::-1]
print("Перевернуте число:", zvorot_number)

