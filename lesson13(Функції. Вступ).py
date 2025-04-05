import random as rd
import string

       #Функції
def hello(): # def <назва>(<параметри>): <код>
    print('Hello, world')
hello()


def hello_for_name(name: str): # параметр - локальна змінна, яка створюється в момент виклику
    print(f'Привіт, {name.capitalize()}!')
hello_for_name('Сергій')
hello_for_name('Боб')


def sum_two_numbers(a, b):
    print(a+b)

n1 = int(input('Введіть цифру:'))
n2 = int(input('Введіть цифру:'))
sum_two_numbers(n1,n2)


def sum_two_numbers(a: int, b: int):
    print(a+b)
sum_two_numbers(10,15)


def sum_two_numbers(a: int | float, b: int | float):
    print(a + b)
sum_two_numbers(10,15)


def hello_for_name(name: str):
    print(f'Привіт, {name.capitalize()}!')
hello_for_name('Боб')


def sum_two_numbers(a: int | float, b: int | float):
    return a + b # return - повернути значення
                 # якщо функція не має return, вона по дефолту NONE
result = sum_two_numbers(10, 15)
print(result)


def sum_two_numbers(a: int | float, b: int | float):
    return a + b # return
print(sum_two_numbers((sum_two_numbers(1, 4), sum_two_numbers(7, 3))))

#import random as rd # Пиши в першому рядку, з самого верху: це правило!!!
def counter(n:int):
    for number in range(1, n + 1):
        return number   # return відразу закриває функцію

def password_generator(password_len: int):
    if password_len not in range(8, 31):
        return # фактично буде return None
    password = ''
    for _ in range(password_len):
        password += rd.choice(string.ascii_letters + string.digits)
    return password

return ''.join(rd.choice(string.ascii_letters + string.digits) for _ in range(password_len))

print(password_generator(-5)) # None
print(password_generator(5)) # None
print(password_generator(10_000_000))  # None
print(password_generator(8))  # PiPnMVU8
print(password_generator(12)) # Nh3z6WteJhEI
print(password_generator(25)) # d2ePtwIcI67EmgHWdltyYaxf6

