
#Генератори
#variant№1
def powers(n:int): # ->1*2, 2*2, 3*2, 4*2, ...
    result = []
    for number in range(1, n+1):
        result.append(number **2)
    return result

print(powers(10))
for el in powers(1000000000000):
    print(el)

#variant№2
def powers(n:int): # ->1*2, 2*2, 3*2, 4*2, ...
     for number in range(1, n+1):
        yield number ** 2 # yield перетворює функцію на генератор
#це як return , відмінність - виводитьт значення
for el in powers(1000000000000):
    print(el)

#variant№3
def powers(n: int):  # ->1*2, 2*2, 3*2, 4*2, ...
    for number in range(1, n + 1):
        yield number ** 2  #

print(*powers(10), sep=',', end='!\n')   # генератор потребує "розпаковки"
print(map(int, ['1', '2', '3', '4', '5']))
print(max(powers(10)))
print(*map(lambda el: f'{el}!', powers(100)))

#Зона видимості
var = 15

def func():
    global var  # global - вказівка функції звертатись напряму до глобальної змінної
    var += 1    #var = var + 1
    print(var)

func()
func()
func()
func()
func()


def func2():
    local var = 15
func()
print(local var)


def func2(n: int):
    n += 1

func2(var)
func2(var)
print(var)


def appender(l: list):
    l.append(1)

my_list = []
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
print(my_list)


def appender(l: list):  #l - my_list, copy -
    copy = l
    l.append(1)

my_list = []
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
appender(my_list)
print(my_list)

________________________________________

def time_decorator(function):   # декоратор - це функція вищого порядку 
    def wrapper(*args, **kwargs):
        # код до ВИКЛИКУ функції
        result = function(*args, **kwargs)
        # код після ВИКЛИКУ функції
        return result
    return wrapper
_________________________________________
"""
start = time.time()
mult_numbers(1, 2, 3)
end = time.time()

функція вищого порядку
map()
filter()
"""
________________________________________
import time
def time_decorator(function):   # декоратор - це функція вищого порядку
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Час роботи функції {function.__name__ }: {end - start}')

        return result
    return wrapper

@time_decorator
def mult_numbers(*nums: int):
    result = 1

    for el in nums:
        result *= el

    print(result)

@time_decorator
def func():
    return 'Hi!'

print(mult_numbers(1, 2, 3, 4, 5))
#print(mult_numbers(*range(1, 10_000)))

print(func())