import random as rd
#Консольний сапер / mineswapper
"""
' ' - звичайна закрита клітинка БЕЗ БОМБИ
'M' - Міна
int - вже відкрита клітинка з кількістю мін навколо
'0' - порожня відкрита клітинка без мін навколо
"""

board = []
game_over = False #Кінець гри
ROW_COUNT = 10
COLUMN_COUNT = 10


def print_board(show_bombs=False):
    for row in board:
        for cell in row:
            if cell != 'M' or show_bombs:
                print(cell, end=' | ')
            else:
                print(' ', end=' | ')
        print()
        print('- ' * (COLUMN_COUNT * 2))

def restart():
    global game_over
    game_over = False
    board.clear()
    for _ in range(ROW_COUNT):
        board.append([" " for _ in range(COLUMN_COUNT)])

def create_bombs(bomb_count: int):  # бомба - 'M'
    while bomb_count:
        random_row = rd.randint(0, ROW_COUNT - 1)
        random_column = rd.randint(0, COLUMN_COUNT - 1)

        if board[random_row][random_column] != 'M':
            board[random_row][random_column] = 'M'
            bomb_count -= 1


def open_cell(row: int, column: int):
    global game_over
    if board[row][column] == '0':   # на всяк випадок, якщо клітинка вже відкрита
        return

    if board[row][column] == 'M':
        game_over = True
        print('Ти програв!')
        return

    bombs_count = bombs_around(row, column)

    if bombs_count: # якщо клітинка має бомби навколо
        board[row][column] = bombs_count
        return
    board[row][column] = '0' # ставимо, що вона порожня (бо не спрацювала умова зверху)

    for row_change, column_change in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
        new_row = row + row_change
        new_column = column + column_change
        if new_row not in range(ROW_COUNT) or new_column not in range(COLUMN_COUNT):
            continue
        open_cell(new_row, new_column) # рекурсивно відкриваємо всі порожні поля


def bombs_around(row: int, column: int):
    count = 0
            # по координатам row column ПОРАХУЙТЕ кількість 'M' навколо клітинки
            # board[row][column] - точка, навколо якої треба
    for row_change, column_change in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
        new_row = row + row_change
        new_column = column + column_change
        if new_row not in range(ROW_COUNT) or new_column not in range(COLUMN_COUNT):
            continue

        if board[new_row][new_column] == 'M':
            count += 1
    return count

            # далі перевіряємо координати на коректність
            # якщо все ок, то перевіряємо, що там лежить

def is_correct(choice: str) -> bool:
    split_result = choice.split()
    if len(split_result) != 2:
        return False
    if not split_result[0].isdigit() or not split_result[1].isdigit():
        return False

    row_index = int(split_result[0]) - 1
    column_index = int(split_result[1]) - 1

    if row_index not in range(ROW_COUNT) or column_index not in range(COLUMN_COUNT):
        return False
    if board[row_index][column_index] not in (' ', 'M'):
        return False
    return True

def main():
    while True:
        restart() #створюємо поле
        create_bombs(10) #заповнюємо бомбами

        while not game_over:
            print_board() #(show_bombs=True)
            choice = input('Оберіть клітинку(НОМЕР РЯДУ, НОМЕР КОЛОНКИ): ')
            if not is_correct(choice):
                continue # continue відразу повертає цикл на початок
            row, column = map(lambda el: int(el) - 1, choice.split())
            open_cell(row, column)
        need_restart = input('Y-почати ще: ')
        if need_restart.lower() != 'Y':
            break

#    print(*board, sep='\n')

if __name__ == '__main__':
    main()