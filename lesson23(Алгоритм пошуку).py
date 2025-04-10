import time
import random as rd
my_list = [rd.randint(-50, 1000) for _ in range(1000_000)]
print(f'Список для пошуку: {my_list}')

#===============Алгоритм пошуку=================

def line_search(arr: list, search_item): #лінійний пошук - прямий перебір всього списку
    index = 0               # початковий індекс
    search_result = False
    attempts = 0            # кількість спроб для заміру часу

    while index < len(arr) and not search_result:
        attempts += 1                   # НЕ ЧАСТИНА АЛГОРИТМУ, а будемо використовувати для заміру
        if arr[index] == search_item:   # якщо по індексу знаходимо той елемент, що шукаємо
            search_result = True
        else:
            index += 1                  # в іншому випадку, просто збільшуємо індекс для наступної ітерації
    print(f'Кількість спроб (лінійний пошук): {attempts}')    # НЕ ЧАСТИНА АЛГОРИТМУ, просто замір кількісті ітерацій
    return  search_result

def binary_search(arr: list, search_item):
    arr.sort()                          # для цього алгоритму масив повинен бути відсортований
    low = 0                             # нижня границя пошуку
    high = len(arr) - 1                 # верхня границя пошуку
    search_result = False
    attempts = 0                        # НЕ ЧАСТИНА АЛГОРИТМУ, кількість спроб для заміру

    while low <= high and not search_result:
        attempts += 1                   # НЕ ЧАСТИНА АЛГОРИТМУ, просто для заміру
        middle_index = (low + high) // 2 # знаходимо середину, цільно ділимо
        item = arr[middle_index]        # дістаємо по індексу середину елемент

        if item == search_item:     # якщо знайшли - супер
            search_result = True    # закриваємо цикл
        elif item < search_item:    # якщо елемент менше шукомого
            low = middle_index + 1  # зсуваємо нижню границю
        else:                       # якщо елемент більше шукомого
            high = middle_index - 1 # зсуваємо верхню границю
    print(f'Кількість спроб (бінарний пошук): {attempts}')
    return  search_result

print(line_search(my_list, 100))
print(binary_search(my_list, 100))
