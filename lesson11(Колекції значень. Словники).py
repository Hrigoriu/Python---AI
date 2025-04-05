        # Двомірний список
double_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
] # Довжина 3
print(double_list[1][2]) #Виведе 6/ double_list[ряд][колонка]
print(double_list[2][0]) #Виведе 7
#l = [1, 2, 3]
for row in double_list:
    for el in row:
        print(el) # Виведе кожен елемент з нового рядка

        # Словники
""" 
Ключ(key)       - унікальний ідентифікатор, що вказує на значення
Значення(value) - значення ключа
Пара(item)      - один елемент словнику (ключ-значення)
"""

user = ['admin', 'qwerty', 27, 'Bob'] #0 - login, 1 - password
if user[0] == admin

#1.Створення словнику
user = {
    'login': 'admin',
    'password': 'qwerty',
    'age': 27,
    'name': 'Bob'
} # item = key: value

#2. Робота з ключами
print(user['name']) # отримання значення за ключем

user['job'] = 'Google inc.' # Створення нової пари (user[key] = value)
print(user)
user['name'] = 'Alice' # Перезапис ключа з новим значенням
del user['job'] #Видалення пари по ключу

#3. Методи словника
    #3.1 Розширення
user.update(name='John', country='Ukraine', age=20) # Оновлення / створення ключів
user.setdefault('new_key') #Створює з нічим
user.setdefault('new_key', 'new_value') # якщо ключ існує - 0 реакції
                           # Якщо не існую - створюється з значенням default
print(user)
    #3.2 Отримання
delete_value = user.pop('new_key') # Видаляє пару по ключу
print(delete_value)                # Назад повертає видалене значення

delete_item = user.popitem()    # видаляє останню пару повернувши кортеж (key, value)
print(delete_item)              # 0 індекс - ключ 1 індекс - значення

print(user.get('name', 'Ключа не існує'))     #Отримує значення ключа, якщо він існує
print(user.get('country', 'Ключа не існує!')) #Якщо ключа немає - повертає default

""" 
Метод замінює конструкцію
if key in dict:
    print(dict[key])
else:
    print('Ключа не існує')
"""

#3.3 Стандартні методи
user.clear() # no comments
user_copy = user.copy() # саме, що і у list

#4. Ітерація
for el in user: # Ітерація тільки ключа   При будь-якій ітерації словник повертає ЛИШЕ КЛЮЧІ
    print(el)

for el in user.values(): # Ітерація тільки значень
    print(el)

for key, value in user.items(): # ітерація пар (повертає кортеж(key, value))
    print(f'{key}: {value}')  # Виводить кортеж

#5. Сортування
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