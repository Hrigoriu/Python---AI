
room = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'R', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*']
]


def print_room():
    for row in room:
        print(*row)


def find_robot():
    for row_index in range(len(room)):
        if 'R' in room[row_index]:
            robot_row = row_index
            robot_column = room[row_index].index('R')
            break

    return robot_row, robot_column


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


def is_correct(command: str) -> bool:  # функція - валідатор ходу ('RIGHT 5')
    command = command.split()

    if len(command) != 2:
        return False

    if command[0].lower() not in ('right', 'left', 'down', 'up'):
        return False

    if not command[1].isdigit():
        return False

    return True


def main():
    while True:
        print_room()
        choice = input('Введіть команду(НАПРЯМ КІЛЬКІСТЬ): ')

        if choice == '0':
            return

        if is_correct(choice):
            choice = choice.split()

            direction = choice[0]
            distance = int(choice[1])

            row, column = find_robot()

            move(row, column, direction, distance)
        else:
            print('Команда неправильна!')


if __name__ == '__main__':  # якщо файл запускається вручну (як головний) а не через import
    main()
