# Рекурсія
from inspect import stack


def counter(n: int):
    if n <= 0:
        return
    print(n)
    counter(n - 1)
counter(100)


def factorial_recursive(n: int):
    if n <= 0:
        return 1
    return n * factorial_recursive(n - 1)
print(factorial_recursive(5))#120


queue()
stack()

l = []
l.append(1)
l.append(2)
l.append(3)
print(l.pop())#3

#Консольний сапер


#import functools

map(Зміни кожен елемент)    Просто: "Зроби щось із кожним елементом".
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Виведе: [1, 4, 9, 16]

functools.reduce(Згорни все в одне)     Просто: "Склади все в одне".
from functools import reduce
numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Виведе: 10

zip(З’єднай списки попарно)     Просто: "З’єднай списки попарно".
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))  # Виведе: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

filter(Відбери потрібне)    Просто: "Залиш те, що підходить".
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Виведе: [2, 4, 6]

all(Усе правда?)    Просто: "Чи все правда?".
values = [True, True, False]
print(all(values))  # Виведе: False
values = [1, 2, 3]
print(all(values))  # Виведе: True

any(Хоч щось правда?)   Просто: "Чи є хоч щось правдою?".
values = [False, False, True]
print(any(values))  # Виведе: True
values = [0, 0, 0]
print(any(values))  # Виведе: False

