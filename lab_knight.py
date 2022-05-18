# ввод

with open("input_knight.txt") as file:
    line = int(file.readline())
    column = int(file.readline())
    XStart = int(file.readline())
    YStart = int(file.readline())


# print(line, column, XStart, YStart)

def move_of_a_knight(X, Y, counter):
    board[X][Y] = counter
    if counter == int(line * column):
        return True
    for s in steps:
        if (0 <= X + s[0] < column) and \
                (0 <= Y + s[1] < line) and \
                (board[X + s[0]][Y + s[1]] == 0) and \
                move_of_a_knight(X + s[0], Y + s[1], counter + 1):
            return True
    board[X][Y] = 0
    return False


def board_printing():
    for i in range(column):
        for j in range(line):
            file_out = open("output_knight.txt", "a")
            file_out.write('|' + "%02d" % board[i][j] + '|')
            file_out.close()
        file_out = open("output_knight.txt", "a")
        file_out.write('\n')
        file_out.close()


# Возможные ходы, размеры поля
steps = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
board = [[0 for x in range(line)] for y in range(column)]

if move_of_a_knight(XStart, YStart, 1):
    board_printing()
else:
    file_error = open("output_knight.txt", "w")
    file_error.write('Маршрута не существует')
    file_error.close()
