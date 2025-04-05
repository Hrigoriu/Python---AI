import random   #Це для завдання про генерацію пароля
import string   #Це для завдання про генерацію пароля
from random import choice

#variant1
def test_func(a, b, *args):
    print(f'Позиційні: {a, b}')
    print(f'Нескінченні позиційні: {args}')
test_func(10, 11)
test_func(10, 11,10, 20, 30,40, 50, 60)

print()
print(10)
print(10, 10, 10)
print(20, 20, 20, sep=' | ')
print(1, 2, 3, 4, 5, 6, 7, 8)
print(10, 20, 30, end=' , ')
print('!')

#variant2
def test_func(a, b, *args, key_1=1, key_2=2):
    print(f'Позиційні: {a}, {b}')
    print(f'Нескінченні позиційні: {args}')
    print(f'Ключові: {key_1}, {key_2}')
test_func(10, 11,key_1=0, key_2=0)

#variant3
def test_func(a, b, *args, key_1=1, key_2=2, **kwargs):
    print(f'Позиційні: {a}, {b}')
    print(f'Нескінченні позиційні: {args}')
    print(f'Ключові: {key_1}, {key_2}')
    print(f'Нескінченні ключові: {kwargs}')
test_func(1, 2,test_key=100000)
dict.update(key1=10, key2=450)


#Завдання№1 : Напишіть код добутку всіх чисел
def mult_numbers(*numbers: int | float):
    result = 1
    for n in numbers:
        result *= n
    return result

nums = [10, 2, 3, 15]
print(mult_numbers())
print(mult_numbers(1, 2, 3, 4, 5))
print(mult_numbers(10, 20, 30))
print(mult_numbers(nums))
#print(mult_numbers(*nums)
print(*nums, sep='|' )
print(*'HELLO')


#Завдання№2 : Напишіть програму для генерації пароля
#variant1
def password_generator(password_len: int):
    if password_len not in range(8, 31):
        return
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_len))

#variant2
def password_generator(password_len: int, include_punctuation=False):
    if password_len not in range(8, 31):
        return
    pattern = string.ascii_letters + string.digits
    if include_punctuation:
        pattern += string.punctuation
    return ''.join(random.choice(pattern) for _ in range(password_len))
print(password_generator(10))
print(password_generator(10, include_punctuation=True))


#Завдання№3 Сортування словника
#Variant№1
humans = {
    'Bob': 20,
    'Qwerty': 13,
    'John': 25,
    'Vi': 31,
    'Johann': 37
} # {Ім'я: вік}

sorted_name = dict(sorted(humans.items(), key=lambda el:len(el[0]))) # 0 ключ
sorted_age = dict(sorted(humans.items(), key=lambda el:[1]))          # 1 значення
print(sorted_name)
print(sorted_age)

#Variant№2
def for_sort(el):
    return el[1]
d = {
    'string1': 10,
    'string2': 25,
    'string3': 1,
    'string4': -4
}
print(sorted(d.items(), key=for_sort))
print(dict(sorted(d.items(), key=for_sort)))

## Lambda-функції/ функція, яка викликається і передається тут і зараз
# Вона не описується зверху, а тут описалася, передалася і більше не бачимо
my_lambda = lambda x, y: x + y
# назва будь-яка = lambda <параметри, що приймає>: <що повертаємо>
print(my_lambda(10, 20))

#Variant№3
d = {
    'string1': 10,
    'string2': 25,
    'string3': 1,
    'string4': -4
}
print(dict(sorted(d.items(), key=lambda el: el[1])))

# Завдання#3: Потрібно щоб кожен символ був зі знаком ! з обох сторін
print(*map(lambda el: '!' + el + '!', 'HELLO'))


# Завдання#4:
"""
Створимо карту кімнати 5x5, посередині якої знаходиться робот 
(у вигляді двомірного списку). Робот позначається рядком “R”,  
порожній простір: “*”.
Приклад кімнати (можна скопіювати собі): 
room = [
    ['*', '*', '*', '*', '*',], 
    ['*', '*', '*', '*', '*',], 
    ['*', '*', 'R', '*', '*',], 
    ['*', '*', '*', '*', '*',], 
    ['*', '*', '*', '*', '*',]
]
Користувач вводить команди, поки не введе «0». 
Кожна команда вводиться у форматі «<Напрям> <Кількість клітинок>». 
Кожна команда рухає робота на вказану кількість клітинок у вказаний напрям. 
Наприклад: “RIGHT 2” – означає на 2 клітинки вправо. 
Кількість команд не обмежена, поки не буде введено 0. 
Якщо робот упирається в стіну, він просто встає не місці, 
поки не буде обрано інший напрям. Обробіть весь рух робота, 
і після того, як буде введено «0», надрукувати список, 
де буде зафіксовано останнє положення робота.
"""
room = [
    ['*', '*', '*', '*', '*',],
    ['*', '*', '*', '*', '*',],
    ['*', '*', 'R', '*', '*',],
    ['*', '*', '*', '*', '*',],
    ['*', '*', '*', '*', '*',]
]

def generate_room():
    pass

def print_room():
    for row in room:
        print(*row)

def find_robot():
    for row_index in range(len(room)):
        if 'R' in room[row_index]:
            robot_row = row_index
            robot_column = room[row_index].index('R')
            break
    return  robot_row, robot_column

def move(robot_row: int, robot_column: int, dir: str, dis: int):
    room[robot_row][robot_column] = '*'

    match dir.lower():
        case 'up':
            # robot_row = max(0, robot_row - dis)
            robot_row -= dis
            if robot_row < 0:
                robot_row = 0
        case 'down':
            # robot_row = min(len(room) - 1, robot_row + dis)
            robot_row += dis
            if robot_row >= len(room):
                robot_row = len(room) - 1
        case 'left':
            robot_column -= dis
            if robot_column < 0:
                robot_column = 0
        case 'right':
            robot_column += dis
            if robot_column > len(room[robot_row]):
                robot_row = len(room[robot_row]) - 1

    room[robot_row][robot_column] = 'R'

# функція - валідатор ходу ('RIGHT 5')
def is_correct(command: str) -> bool:
    command = command.split()
    if len(command) != 2:
        return False
    if command[0].lower() not in ('right', 'left', 'down', 'up'):
        return False
    if not command[1].isdigit():
        return False
    return True

def main():
    generate_room()
    while True:
        print_room()
        choice = input('Введіть команду (НАПРЯМ КІЛЬКІСТЬ): ')
        if choice == '0':
            return
        if is_correct(choice):
            choice = choice.split()
            direction = choice[0]
            distance = int(choice[1])
            row, column = find_robot()
            move(row, column, direction, distance)
        else:
            print('Команда не коректна!')

# якщо файл запускається вручну (як головний), а не через import
if __name__ == '__main__':
main()


