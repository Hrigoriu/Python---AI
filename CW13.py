#Завдання1
def task1(text: str, n: int):
    return text * n
text = input("Введіть текст: ")
n = int(input("Введіть кількість повторів: "))
print(task1(text, n))


#Завдання2
def add_string(str1: str, str2: str):
    average_index = len(str1) // 2
    return str1[:average_index] + str2 + str1[average_index:]
print(add_string("abcdef", "123"))  # Парна довжина abc123def
print(add_string("abcde", "123"))   # Непарна довжина ab123cde


#Завдання3
def powers(n: int):
    result = {}
    for i in range(1, n + 1):
        result[i] = i * i
    return str(result)
number = int(input("Введіть натуральне число: "))
if number <= 0:
    print("Число має бути позитивним!")
else:
    result = powers(number)
    print(result)
