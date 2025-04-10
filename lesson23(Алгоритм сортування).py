import time
import  random as rd

my_list = [rd.randint(-500, 1000) for _ in range(10_000)]
print(f'Список для сортування: {my_list}')

def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Результат функції {function.__name__} - {end - start} сек')
        return result
    return wrapper


#==========================Алгоритм сортування=========================
@time_decorator
def bubble_sort_for_beginners(arr: list):   # сортування бульбашкою 1(дитячий варіант)
    while True:
        reshuffles = False                  # змінна, яка говорить, чи були перестановки
        for index in range(len(arr) - 1):   # для всіх індексів, окрім останнього
            if arr[index] > arr[index + 1]: # якщо лівий більше правого
                arr[index], arr[index + 1] = arr[index + 1], arr[index] # міняємо місцями
                reshuffles = True
        if not reshuffles:  # якщо перестановок не було
            break           #завершуємо while, бо сортування завершено

#bubble_sort_for_beginners(my_list)
#print(my_list)

#--------------------------------------------------------------------------------------------------
@time_decorator
def bubble_sort_standart(arr: list):    # стандартне сортування бульбашкою
    l = len(arr)
    for i in range(l):                  # цикл для кожного елементу, що буде рухатись
        for j in range(0, l - i - 1):   # цикл тільки для елементів, що знаходяться СПРАВА від нашого (- 1, щоб не включити останній)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# bubble_sort_standart(my_list)
# print(my_list)

#------------------------------------------------------------------------------------------------
#@time_decorator
def merge_sort(arr: list):
    l = len(arr)
    if l == 1:              # це для РЕКУРСІЇ
        return arr
    middle = l // 2
    left = merge_sort(arr[:middle]) # рекурсивно розрізаємо, поки не залишиться по одному елементу
    right = merge_sort(arr[middle:]) #
    res = []    # відсортований список, який будемо передавати далі
    i = 0       # лічильник для лівої частини
    j = 0       # лічильник для правої частини
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):           # якщо залишився лівий список
        res.extend(left[i:])    # цілком доєднуємо до результату те, що залишилося від списку
    if j < len(right):          # аналогічно з правою частино
        res.extend(right[j:])
    return res
#print(merge_sort(my_list))

my_list_copy1 = my_list.copy()
my_list_copy2 = my_list.copy()
my_list_copy3 = my_list.copy()

bubble_sort_for_beginners(my_list_copy1)
bubble_sort_standart(my_list_copy2)
#merge_sort(my_list_copy3)

start = time.time()
merge_sort(my_list_copy3)
end = time.time()
print(f'Результат merge sort: {end - start}')

#--------------------------------------------------------------------------------------

def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr
    item = arr[0]

    left = [number for number in arr if number < item]
    middle = [number for number in arr if number == item]
    right = [number for number in arr if number > item]
    return quick_sort(left) + middle + quick_sort(right)

    # left = []
    # middle = []
    # right = []
    # for number in arr:
    #     if number < item:
    #
    #         left.append(number)
    #     elif number > item:
    #         right.append(number)
    #     else:
    #         middle.append(number)
    # return quick_sort(left) + middle + quick_sort(right)

start = time.time()
res2 = merge_sort(my_list)
end = time.time()
print(f'Результат quick sort: {end - start}')

start = time.time()
res3 = sorted(my_list)
end = time.time()
print(f'Результат Python sort: {end - start}')

start = time.time()
my_list.sort()
end = time.time()
print(f'Результат Python sort: {end - start}')