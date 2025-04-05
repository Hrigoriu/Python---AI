#КОНСОЛЬНИЙ КАЛЬКУЛЯТОР

number_1 = float(input('Введіть число: '))
operation = input('Введіть операцію(+, -, *, /): ')
number_2 = float(input('Введіть число: '))

if operation == '+':  # якщо
    print(number_1 + number_2)
elif operation == '-':  # в іншому випадку
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    if number_2 != 0:  # != - не дорівнює
        print(number_1 / number_2)
    else:
        print('ERROR. На нуль ділити не можна!')
   #pass # pass - це заглушка, нічого не буде робитися
else:   # тоді якщо не спрацювали вище (в іншому випадку робимо)
    print('ERROR. Невідома операція!')