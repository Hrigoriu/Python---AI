
# Множини
# Множина - невпорядкована (!!!) послідовність УНІКАЛЬНИХ елементів
#1. Створення множини
numbers = {1, 10, 45, 2, 1, 10, 45, 2, 1, 10, 54, 10} # Створення множини
empty_set = set()  # Створення порожньої множини


#2. Методи множини
#2.1 Розширення
numbers.add(100) # Додає елемент в множину (неважливо на яке місце)
numbers.add(True) # Якщо елемент вже є, жодної реакції True = 1, а 1 вже є
numbers.remove(54) # Видаляє елемент по значенню
numbers.remove(200) # Якщо елемента не існує - помилка KeyError
numbers.discard(2) # Видаляє елемент по значенню (як і remove)
numbers.discard(200) # На відміну від remove,якщо не існує - жодної реакції
numbers.clear() # Очищення множини від всіх елементів
number_copy = numbers.copy()
# як і в списках та словниках,
# створює автономну копію, не пов'язану з оригіналом
el = numbers.pop() # Витягує умовно перший елемент та видаляє його (як і у списках)
print(el)

numbers.update([10, 20, 45, 2]) # Об'єднує множину з іншою послідовністю
new_set = numbers.union([200, 300, 20, 2])
# Робить update, але результат повертає новою множиною
print(numbers)
#2.4. Аналіз множин
worker_1 = {'Python', 'Java', 'C++'}
worker_2 = {'Java', 'JavaScript', 'C#','Python'}
print(worker_1.intersection(worker_2)) # Спільні елементи множини А та множини Б
print(worker_2.intersection(worker_1)) # Метод повністю симетричний
print(worker_1.difference(worker_2)) # Елемент множини А, яких не має в Б
print(worker_2.difference(worker_1)) # Метод не симетричний
print(worker_1.symmetric_difference(worker_2))
# Все, що не пересікається (інікальні елементи для кожної множини)

#Задача. Скажіть, які символи є у першої строки і у другої строки

string_1 = input('Текст: ').lower()
string_2 = input('Текст: ').lower()
print("Спільні елементи: " + ','.join(set(string_1).intersection(string_2)))

