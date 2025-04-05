        #Строки. Методи строк.

text = 'Hello, world!'
print(text[:5]) # Виведе Hello

# Метод - "дія" об'єкта, направлена на його властивості чи атрибути
# Метод - функція, яка описана в середині класу

    # --- Методи строк
#1.  case-методи
print(text.upper()) # призводить всі літери у строці до великого кейсу
print(text.lower()) # призводить всі літери у строці до маленького кейсу
print('hEllo, wOrlD'.capitalize()) # першу літеру робить великою, а інші маленькі #Виведе Hello, world
print(text.swapcase()) # міняє кейс на протилежний, там де великі літери будуть малі, де малі - великі


#2. bool-методи (починаються з is) створені для використання в умовах
print('UPPeR!!!123'.isupper()) # True, якщо всі ЛІТЕРИ(символи, що мають кейс) - великі
print('lowEr'.islower()) # True, якщо всі ЛІТЕРИ(символи, що мають кейс) - маленькі
print('10045'.isdigit()) # True, якщо всі ЕЛЕМЕНТИ строки - цифри)
                         #False якщо хоч один ЕЛЕМЕНТ строки пробіл чи крапка
print('qwertyшошод'.isalpha()) # True, якщо ВСІ ЕЛЕМЕНТИ строки - літери
                               # False, якщо хоч один УЛЕМЕНТ строки - не літера
print(text.startswith('Hello')) # True, якщо строка ПОЧИНАЄТЬСЯ з вказаної підстроки
print(text.endswith('word'))    # True, якщо строка ЗАКІНЧУЄТЬСЯ з вказаної підстроки


#3. Робота із підстроками (підстрока(substring) - будь-яка частина строки)
text = 'Hello, world!'
print(text.index(',')) #5 / повертає індекс, з якого починається підстрока
print(text.index('python')) # якщо підстроки не існує - ValueError
print(text.find('world')) # повертає індекс, з якого починається підстрока
print(text.find('python'))  # на відміну від index, повертає -1, якщо підстроки не існує
print(text.count('l')) # кількість l виведе 3
# повертає кількість входжень у строку (кількість елементів)ю Може бути 0.
print(text.replace('l', '*')) # He**o, wor*d! /заміняє всі __old на __new
print(text.replace('l', '$')) # працює і з підстроками
print(text.replace('o', '[replace]')) # Hell[replace], w[replace]rld!
print(text.replace('l', '')) #Heo, word!/
        # можна навіть видаляти елементи, міняючи їх на порожню строку
print(' Python      '.strip()) #удаляє пробіли з обох боків строки
print('    123  4 56 123   '.strip()) #123  4 56 123/удаляє пробіли з обох боків строки, в середині ні
print('__-_-_1-_2-_3-__-_'.strip('-_')) #1-_2-_3/ якщо передати групу символів, відріже/видалить їх в середині

# наприклад login = input('Введіть login: '.strip())#повидаляє пробіли якщо хтось повводив

text = 'lower'
text = text.upper()
print(text) # напише всі букви у слові великими LOWER

#4. split та join
numbers = '543 -3 6543 400 54 236'
print(numbers.split()) #прибирає всі пробіли/  розрізає строку, поклавши всі елементи в список
print(' , '.join(str(number) for number in range(1, 101)))
print(' | '.join(numbers.split())) #543 | -3 | 6543 | 400 | 54 | 236#
print(''.join(str(number) for number in range(10))) #0123456789# вивело цифри від 0 до 9 та склеїло їх

word = 'HELLO' # задача: помістити між всіма літерами '|'
print('|'.join(word)) # H|E|L|L|O #
print('\n'.join(word)) # виведе кожну букву з абзацу


text = input("Введіть текст: ").lower()

most_common = ''
max_count = 0
for char in text:
    count = 0
    for symbol in text:
        if symbol == char and symbol!= ' ':
            count = count + 1
    if count > max_count:
        max_count = count
        most_common = char
print(f"Символ, що зустрічається найчастіше: '{most_common}' ({max_count} разів)")