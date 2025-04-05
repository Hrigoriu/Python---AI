
#=========================================================================
#1.	ТЕОРІЯ. Що таке функція вищого порядку?
"""
Функція вищого порядку — це така функція в програмуванні,
яка може або приймати інші функції як аргументи, або повертати функцію
як результат. Простіше кажучи, це функція, яка "працює з іншими функціями".
Функція, яка приймає іншу функцію як аргумент:
Найпоширеніші приклади — це вбудовані функції Python,
такі як map(), filter() та sorted()
"""
from curses import wrapper
from importlib.metadata import pass_none

#=========================================================================
#2.	ТЕОРІЯ. Що таке генератор?
"""
Генератор у Python — це спеціальний інструмент, який дозволяє створювати 
послідовності значень "на льоту", тобто по одному за раз, а не зберігати 
їх усі в пам’яті одразу. Це дуже корисно, коли тобі потрібно працювати з 
великими даними або нескінченними послідовностями, наприклад, числами 
від 1 до мільйона, але не хочеш займати багато місця в пам’яті.
Генератори створюються за допомогою функцій, у яких є ключове слово yield 
замість return. Коли функція доходить до yield, вона "призупиняється" і 
віддає значення, а потім чекає, поки її попросять дати наступне.
"""

#==============================================================================
#3.	ТЕОРІЯ. Що означає конструкція “if __name__ == ‘__main__’: ”?
"""
Конструкція if __name__ == '__main__': це конструкція, яка використовується 
для визначення, чи запущений файл як головна програма, 
чи імпортований як модуль в інший файл.
Це точка входу,
*Якщо файл запускається безпосередньо (як головна програма), 
то __name__ дорівнює '__main__'.
*Якщо файл імпортується в інший файл як модуль, 
то __name__ дорівнює імені модуля (назві файлу без розширення .py).
"""

#========================================================================
#4.	ТЕОРІЯ. Чим позиційний аргумент відрізняється від ключового?
"""
*Позиційні аргументи передаються у функцію у строгому порядку, 
який визначений при оголошенні функції. 
Порядок передачі аргументів має значення.
*Ключові аргументи передаються за іменем параметра, 
який визначений у функції. Порядок передачі аргументів не має значення.
У Python можна комбінувати позиційні та ключові аргументи. 
Однак є правило: спочатку передаються позиційні аргументи, а потім ключові.
"""
print(sep=, end=, file=)
#===========================================================================
#Завдання №5.
"""
Напишіть функцію, яка перероблює текст із символів наступним чином:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
Параметр accum — це рядок, який містить лише літери з a..z та A..Z.
"""
#Variant 1
def accum(text):
    result = ''
    for index in range(len(text)):
        letter = text[index]
        group = letter.upper() + letter.lower() * index
        result += group
        if index < len(text) - 1:
            result += '-'
    return result
print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))

#Variant 2
def accum(s):
    result = []
    for index, letter in enumerate(s):
        group = letter.upper() + letter.lower() * index
        result.append(group)
    return '-'.join(result)
print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))

#Variant 3
def accum(s: str):
    return '-'.join(char.upper() + (char.lower() * counter) for counter, char in enumerate(s))
print(accum('aBcDeFgH'))

#Variant 4
def accum(s: str):
    return '-'.join(char * counter).capitalize() for counter, char in enumerate(s, start=1))
print(accum('aBcDeFgH'))

# Variant 5

def accum(s: str):
    return '-'.join(char * counter for counter, char in enumerate(s, start=1)).capitalize()
print(accum('aBcDeFgH'))

#===================================================================
#Завдання №6.
"""
Напишіть функцію-таймер. Користувач вводить час у хвилинах і 
отримує у консоль відлік у реальному часі. 
Використайте будь-який модуль для заміру часу, наприклад time. 
"""
import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print('Час вийшов!')

minutes = float(input('Введіть час у хвилинах: '))
timer(minutes)

#=========================================================================
#Завдання №7.
"""
Напишіть функцію, яка приймає рядок з одного або кількох слів і 
повертає той самий рядок, але з усіма п’ятьма або більше літерами слів, 
перевернутими. Передані рядки складатимуться лише з літер і пробілів. 
Пробіли будуть додані, лише якщо присутнє більше одного слова.
spinWords( "Hey fellow warriors" ) => return "Hey wollef sroirraw" 
spinWords( "This is a test") => return "This is a test" 
spinWords( "This is another test" )=> return "This is rehtona test"
"""
# Variant 1
def spinWords(text):
    words = text.split()
    new_words = []
    for word in words:
        if len(word) >= 5:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    return " ".join(new_words)
print(spinWords("Hey fellow warriors"))
print(spinWords("This is a test"))
print(spinWords("This is another test"))

# Variant 2
def spin_words(word: str):
    return ' '.join(word if len(word) < 5 else word [::-1] for word in word.split())
print(spin_words("Hey fellow warriors"))

# Variant 3
def spin_words(words: str):  # функція приймає слова через пробіл
    result = ''
    for word in words.split():
        if len(word) < 5:
            result += word
        else:
            result += word[::-1]
        result += ' '
    return result.strip()
#    return result.[::-1]
print(spin_words("Hey fellow warriors"))

#=================================================================
#Завдання №8.
"""
Створіть генератор простих чисел до числа n
(аргумент, що передається у генератор).
"""
# Variant 1
def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True
        for index in range(2, num):
            if num % index == 0:
                is_prime = False
                break
        if is_prime:
            yield num
n = int(input('Введіть число: ')) # n = 20
for prime in prime_generator(n):
     print(prime, end=" ")  # Виведе: 2 3 5 7 11 13 17 19

# Variant 2
def prime_generator(n: int):
    for number in range(1, n + 1):
        for dividar in range(2, number):
            if number % divider == 0:
                break
        else:
            yield number
print(*prime_generator(100))

#===================================================================
#Завдання №9.
"""
Напишіть генератор, який для заданого натурального числа n (n > 0) 
генерує послідовність чисел, описану в гіпотезі Коллатц: якщо n парне, 
то ділимо його навпіл, якщо непарне, то множимо на 3 і додаємо 1. 
З підсумком обчислення знову проробляємо цю операцію до тих пір, 
поки в результаті не отримаємо число 1. Наприклад, для числа n = 17 
послідовність обчислень виглядає наступним чином: 
17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
"""
# Variant 1
def collatz_generator(n):
    if n <= 0:
        return
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        yield n
n = int(input('Введіть число: ')) # n = 17
for num in collatz_generator(n):
    print(num, end=" ")  # 17 52 26 13 40 20 10 5 16 8 4 2 1

# Variant 2
def collatz_generator(n: int):
    while n != 1:
        yield n
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n *= 1
    yield n

print(collatz_generator(17))

#================================================================
#Завдання №10.
"""
*Напишіть функцію-декоратор, що зберігає результат функції. 
Наступного разу, при її виклику, результати повинні додаватись.
"""
def accumulate_decorator(function):
    accumulated = 0
    def wrapper(*args, **kwargs):
        ?????????????????
        return accumulated
    return wrapper
@accumulate_decorator
def add_five(x):
    ???????????
#Щось я тут не розумію логіку та що далі писати в коді

def memory(func):
    def wrapper(*args. **kwargs):
        pass
    return wrapper()


def memory(function):
    cache = {} # func: sum result
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if function  in cache:
            cache[function] += result
        else:
            cache[function] = result
        return cache[function]
    return wrapper

@memory
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(1, 2))

#Приклад замикання
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
count1 = counter()
print(count1())
print(count1())
print(count1())

#=================================================================
#Завдання №11.
"""
*На шаховій дошці стоїть кінь. Відзначте положення коня на дошці
і всі клітинки, які б’є кінь. Клітинку, де стоїть кінь, відзначте
буквою K, клітинки,  які б’є кінь, відзначте символами *, решта 
клітинок заповніть крапками.  Програма отримує на вхід координати 
коня на шаховій дошці в шаховій нотації,  тобто, у вигляді e2, де 
спочатку записується номер стовпця (буква від a до h, зліва направо),
потім номер рядка  (цифра від 1 до 8, знизу догори). Виведіть на 
екран зображення шахової дошки як у вихідних даних.
____________________________________________________________________
Вхідні дані:
e4
Вихідні дані:
. . . . . . . .
. . . . . . . .
. . . * . * . .
. . * . . . * .
. . . . K . . .
. . * . . . * .
. . . * . * . .
. . . . . . . .
"""
#Variant №1
board = [['.' for _ in range(8)] for _ in range(8)]

def print_board():
    for row in board[::-1]:
        print(*row)

def place_knight(position: str):
    col = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    for i in range(8):
        for j in range(8):
            board[i][j] = '.'
    board[row][col] = 'K'
    moves = [
            (-2, -1), (-2, 1),  # 2 вгору,  1 вліво/вправо
            (2, -1), (2, 1),    # 2 вниз,   1 вліво/вправо
            (-1, -2), (-1, 2),  # 1 вгору,  2 вліво/вправо
            (1, -2), (1, 2)     # 1 вниз,   2 вліво/вправо
    ]
    for move_row, move_col in moves:
        new_row = row + move_row
        new_col = col + move_col
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            board[new_row][new_col] = '*'

def is_valid_position(position: str) -> bool:
    if len(position) != 2:
        return False
    col, row = position[0], position[1]
    return col.lower() in 'abcdefgh' and row.isdigit() and int(row) in range(1, 9)

def main():
    while True:
        position = input('Введіть позицію коня (наприклад, e4): ')
        if is_valid_position(position):
            place_knight(position)
            print_board()
            break
        else:
            print('\nНевірний формат!\n'
                  'Введіть, наприклад, e4.\n'
                  'Значення мають бути в проміжку a-h, 1-8\n')

if __name__ == '__main__':
    main()

#Variant №2

def move_knight(position: str): # Приклад позиції: e4, h5
    columns = {char: index for index,  char in enumerate('abcdefgh')}
    board = [['.' for _ in range(8)] for _ in range(8)]
    knight_row = int(position[1]) - 1
    knight_column = columns.get(position[0])
    board[knight_row][knight_column] = 'k'
    moves = [(1, 2), (2, 1), (-1, 2),(-2, 1), (-2, -1), (-1, -2), (-1,-2), (1, -2)]
    for row_change, column_change in moves:
        new_row = knight_row + row_change
        new_column = knight_column + column_change
        if new_row not in range(8) or new_column not in range(8):
            continue

    board.reverse()
    return board

print(*move_knight('c3'), sep='\n')





#=================================================================
#Завдання №12.
"""
**Ускладніть попередню задачу. Напишіть повноцінний движок, 
що дозволяє рухати коня по координатам. Використовуйте попередню
функцію для виводу поточного положення коня. Задача повинна 
включати декілька функцій (наприклад: функція друку(11 завд.), 
функція руху, функція запиту, тощо), що пов’язані головною, 
виклик якої відбувається у точці входу “if __name__ == ‘__main__’”. 
"""
board = [['.' for _ in range(8)] for _ in range(8)]

def print_board():
    for row in board[::-1]:
        print(*row)

def place_knight(position: str):
    col = ord(position[0].lower()) - ord('a')
    row = int(position[1]) - 1
    for i in range(8):
        for j in range(8):
            board[i][j] = '.'
    board[row][col] = 'K'
    moves = [
            (-2, -1), (-2, 1),  # 2 вгору,  1 вліво/вправо
            (2, -1), (2, 1),    # 2 вниз,   1 вліво/вправо
            (-1, -2), (-1, 2),  # 1 вгору,  2 вліво/вправо
            (1, -2), (1, 2)     # 1 вниз,   2 вліво/вправо
    ]
    for move_row, move_col in moves:
        new_row = row + move_row
        new_col = col + move_col
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            board[new_row][new_col] = '*'

def is_valid_position(position: str) -> bool:
    if len(position) != 2:
        return False
    col, row = position[0], position[1]
    return col.lower() in 'abcdefgh' and row.isdigit() and int(row) in range(1, 9)

def find_knight() -> tuple:
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'K':
                return row, col
    return None

def is_valid_move(current_row: int, current_col: int, new_row: int, new_col: int) -> bool:
    moves = [
            (-2, -1), (-2, 1),  # 2 вгору,  1 вліво/вправо
            (2, -1), (2, 1),    # 2 вниз,   1 вліво/вправо
            (-1, -2), (-1, 2),  # 1 вгору,  2 вліво/вправо
            (1, -2), (1, 2)     # 1 вниз,   2 вліво/вправо
    ]
    row_diff = new_row - current_row
    col_diff = new_col - current_col
    return (row_diff, col_diff) in moves

def move_knight(new_position: str) -> bool:
    if not is_valid_position(new_position):
        return False
    new_col = ord(new_position[0].lower()) - ord('a')
    new_row = int(new_position[1]) - 1
    current_row, current_col = find_knight()
    if not is_valid_move(current_row, current_col, new_row, new_col):
        return False
    place_knight(new_position)
    return True

def request_move():
    while True:
        move = input('\nВведіть нову позицію коня (наприклад, f6)'
                     '\nабо exit для завершення: ')
        if move.lower() == 'exit':
            return None
        if move_knight(move):
            return True
        else:
            print('\nНевірний формат!\n'
                  'Введіть, наприклад, e4 -> f6.\n'
                  'Значення мають бути в проміжку a-h, 1-8\n')

def main():
    while True:
        start_pos = input('Введіть початкову позицію коня (наприклад, e4): ')
        if is_valid_position(start_pos):
            place_knight(start_pos)
            break
        print('\nНевірний формат!\n'
              'Введіть, наприклад, e4 або f6.\n'
              'Значення мають бути в проміжку a-h, 1-8\n')
    while True:
        print_board()
        if request_move() is None:
            print("Гру завершено!")
            break

if __name__ == '__main__':
    main()
