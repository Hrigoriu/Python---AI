"""
Завдання №1
Напишіть функцію, яка генерує множники для заданого числа.
Функція приймає ціле число як параметр і повертає список цілих чисел.
Цей список містить прості множники в числовій послідовності.
1  ==>  []
3  ==>  [3]
8  ==>  [2, 2, 2]
9  ==>  [3, 3]
12 ==>  [2, 2, 3]
Замість списку, зробити генератор
"""
#variant №1
def get_dividers(n: int):
    dilnuk = 2
    while dilnuk * dilnuk <= n:
        while n % dilnuk == 0:
            yield dilnuk
            n //= dilnuk
        dilnuk += 1
    if n > 1:
        yield n
print(list(get_dividers(1)))
print(list(get_dividers(3)))
print(list(get_dividers(8)))
print(list(get_dividers(9)))
print(list(get_dividers(12)))

#variant №2
def get_dividers(n: int):
    while n !=1:
        for divider in range(2, n + 1):
            if n % divider == 0:
                yield divider
                n //= divider
                break
print(*get_dividers(543645))

"""
Завдання №3
Напишіть функцію persistence, яка приймає додатний параметр num 
і повертає його мультиплікативну стійкість, тобто кількість разів, 
які ви повинні помножити цифри в num, доки не досягнете однієї цифри.
39 --> 3 (оскільки 3*9 = 27, 2*7 = 14, 1*4 = 4 і 4 містить лише одну цифру)
999 --> 4 (оскільки 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12 і, нарешті, 1*2 = 2)
4 --> 0 (оскільки 4 вже є однозначним числом)
"""
#variant №1
def persistence(n: int):
    krok = 0
    while n >= 10:
        digits = str(n)
        mnoz = 1
        for digit in digits:
            mnoz *= int(digit)
        n = mnoz
        krok += 1
    return krok
print(persistence(999))
print(persistence(39))
print(persistence(4))

#variant №2
def persistence(n: int):
    counter = 0
    while n not in range(1, 10):
        result = 1
        for str_digit in str(n):
            result *= int(str_digit)
        counter += 1
        n = result
#variant №3
___________________________
import functools
def persistence(n: int):
    counter = 0
    while n not in range(1, 10):
        result = functools.reduce(lambda el1, el2: int(el1) * int(el2), str(n))
        counter += 1
        n = result
    return counter
print(persistence(35))


"""
Завдання №5
Команда маркетингу витрачає занадто багато часу на введення хештегів.
Давайте допоможемо їм за допомогою нашого власного генератора хештегів!
Ось умови:
•	Він повинен починатися з хештегу (#).
•	Усі слова мають мати першу літеру з великої літери.
•	Якщо кінцевий результат довший за 140 символів, він має повернути false.
•	Якщо вхід або результат є порожнім рядком, він повинен повернути false.
Приклади
•	" Hello there thanks for trying my Kata " => "#HelloThereThanksForTryingMyKata"
•	"Hello World " => "#HelloWorld"
"""
#variant №1
def create_hashtag(text: str):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = "#" + "".join(capitalized_words)
    if len(hashtag) > 140:
        return False
    return hashtag
print(create_hashtag(" Hello there thanks for trying my Kata "))
print(create_hashtag("Hello World "))

#variant №2
def create_hashtag(string: str):
    if len (string) == '':
        return False
    result = '#' + ''.join(string.split())
    return result if len(result) <= 140 else False
print(create_hashtag('Hello world!'))
