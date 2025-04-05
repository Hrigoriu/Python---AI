
'''
Домашнє завдання №1
Ваше завдання: знайти та виправити помилки, що код виконався без помилок.
Результат роботи завантажте файлом «1.py».
var_1 = 1 
var_2 = 2
var_3 = 4
sumOfVars = var_1 + var_2 + var_4
print(sumOfvars)

Знайдені помилки:
-виведено неіснуюча змінна var_4 у формулі
-в команді print у назві буква v маленьке, а до того була буква велика V
'''

#Після виправлення
var_1 = 1
var_2 = 2
var_3 = 4
sumOfvars = var_1 + var_2 + var_3
print(sumOfvars)
Результат - 7

'''
Домашнє завдання №2
2.	Виведіть на екран:
«OMG, 
Python
Work!»
Відповідно, дотримуючись абзаців.
'''

# #Variant1
print("OMG,")
print("Python")
print("Work!")

# #Variant2
print("OMG\nPython\nWork!")

# #Variant3
print("""OMG,
Python
Work!""")

# #Variant4
print("OMG,", "Python", "Work!", sep="\n")

# #Variant5
print("OMG,", end="\n")
print("Python", end="\n")
print("Work!")

'''
Домашнє завдання №3
Оголосіть три змінні і присвоїти першій числове значення, 
друга змінна дорівнює першій змінній збільшеної на 3, 
а третя змінна дорівнює сумі перших двох. 
Виведіть на екран значення кожної змінної
'''

x = 5
y = x + 3
z = x + y
print(x)
print(y)
print(z)

var_1 = 15
var_2 = var_1 + 3
var_3 = var_1+ var_2
print(var_1, var_2, var_3)

'''
Домашнє завдання №4
Поміняйте значення двох змінних місцями
(уявіть, що ви на знаєте, що саме зберігається в цих змінних)
'''
# #Variant1
a, b = b, a

# #Variant2
a = a + b
b = a - b
a = a - b

# #Variant3
temp = a
a = b
b = temp

a = input('a: ') #1
b = input('b: ') #100
print(a)

