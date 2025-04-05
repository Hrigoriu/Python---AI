        #Винятки
try:
    number_1 = int(input('Введіть число 1: '))  # ValueError
    number_2 = int(input('Введіть число 2: '))  # ValueError

    result = number_1 / number_2    #ZeroDivisionError
    print(result)
except:
    print('Сталася помилка')
#================================================================
try:
    number_1 = int(input('Введіть число 1: '))  # ValueError
    number_2 = int(input('Введіть число 2: '))  # ValueError

    result = number_1 / number_2    #ZeroDivisionError
    print(result)
except ValueError:
    print('Ви ввели не число!')
except ZeroDivisionError:
    print('Не можна ділити на нуль!')
except ArithmeticError:
    print('Математична помилка!')
else:       # спрацьовує, якщо не було помилок
    print('ELSE')
finally:    # спрацьовує в будь-якому разі вкінці, навіть якщо помилка не була оброблена exept
    print('FINALLY')

# Конструкція для існування повинна мати: 1 try і або finally, або 1 except
#===========================================================================
class MyException(Exception):
    def __str__(self):
        return 'Привіт, це моя власна помилка!'

def raiser(n: int):
    match n:
        case 1:
            raise ValueError
        case 2:
            raise FloatingPointError
        case 3:
            raise IndexError ('Це мій власний IndexError!🤯')
        case 4:
            raise KeyboardInterrupt
        case 5:
            raise MyException

try:
    raiser(5)

    number_1 = int(input('Введіть число 1: '))  # ValueError
    number_2 = int(input('Введіть число 2: '))  # ValueError

    result = number_1 / number_2    #ZeroDivisionError
    print(result)
except ValueError:  # обробка винятку ValueError
    print('Ви ввели не число!')
except ZeroDivisionError:
    print('Не можна ділити на нуль!')
except ArithmeticError:
    print('Математична помилка!')
except Exception as exc:
    print(f'Сталася помилка: {exc}')
except KeyboardInterrupt:
    print('Ви закрили програму вручну!')
else:       # спрацьовує, якщо не було помилок
    print('ELSE')
finally:    # спрацьовує в будь-якому разі в кінці, навіть якщо помилка не була оброблена exept
    print('FINALLY')

 # Ми можемо :
1.Обробляти винятки
2.Генеретувати винятки
3.Створювати винятки

================================================================================

"""
Адреса для файлу:
1. Глобальний (абсолютний) шлях: D:\\IT schcool\\IT Step Academy\\Projects_IT_School\\Python---AI\\files\\data.txt
2. Локальний шлях: files\\data.txt
"""

# запис (write)
#1
file = open('files/data.txt', 'w') # 'w' - або створює файл, якщо його немає, або перезаписує
file.write('PYTHON\n')                      # 1-й спосіб запису: метод запису write()
file.write('Jcript')
file.write('Django\n')
#2
file = open('files/data.txt', 'w')
print('LINE 1', file=file)                  # 2-й спосіб запису: використання print()
print('Jcript 2', file=file)
print('Django 3', file=file)
file.close()
#3
file = open('files/data.txt', 'w')
words = ['python', 'new', 'old', 'print', 'input', 'sep']
print(*words, sep='\n', file=file)          # 3-й спосіб запису: тільки через print
file.close()
#4
file = open('files/data.txt', 'w')
words = ['python', 'new', 'old', 'print', 'input', 'sep']
file.writelines(el + '\n' for el in words)  # 4-й спосіб запису: запис ітерованої послідовності
file.close()


# читання (read)
#1.
file = open('files/data.txt', 'r') # для того, щоб відкрити файл на читання, ФАЙЛ ПОВИНЕН ІСНУВАТИ !!!
data = file.read()      # 1-й спосіб: читання всього файлу цілком
print(data)
file.close()
#2.
file = open('files/data.txt', 'r')
data = file.read()
print(file.readline())  # 2-й спосіб: повертає список, в якому є рядок файлу
file.close()
#3.
file = open('files//data.txt', 'r')
for line in file:       # 3-й спосіб: ітерація файлу (в Python текстовий файл являється ітерованою послідовністю)
    print(line, end='')
file.close()
#4.
file = open('files/data.txt', 'r')
#a
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
#b
print(file.readline(), end='')  4-й спосіб: прочитати один рядок
print(file.readline(), end='')
print(====================)
print(file.readline())
print(file.read())
#Щоб курсор підняти знизу до верху, щоб далі читати рядки, є
#(Python рухає курсор в один бік і переходить на наступний рядок)
file.seek(0)    #переміщує курсор на початок файлу
file.seek(3)    #переміщує курсор по індексу символу
print(file.readline())
file.close()
====================================

file1 open()
file2 open()

file2.close()
file1.close()

====================================================
# 'a' - режим для доповнення, додає нову інформацію і зберігає стару (запис або видалення)
with open('files/data.txt', 'a') as file:
    print('HELLO WORLD', file=file)
print('HELLO WORLD', file=file) #не ставимо з початку, бо буде помилка
=============================================
"""
Напишіть програму для підрахунку кількості рядків у текстовому файлі
"""
#Variant#1
with open('files/data.txt', 'r') as file:
    counter = 0
    for line in file:
        counter += 1
    print(counter)
# Variant#1
with open('files/data.txt', 'r') as file:
    print(len(file.readlines()))
