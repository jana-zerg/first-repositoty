# x - строки
# y - столбцы

fild = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]


def see():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {fild[i][0]} {fild[i][1]} {fild[i][2]}")


def check(x, y):
    if 0 <= x <= 2 and 0 <= y <= 2:
        if fild[x][y] == " ":
            return True
        else:
            print('Клетка занята. Попробуйте еще!')

    else:
        print('Так ходить нельзя. Давайте еще раз!')


motion = 0
while True:
    motion += 1

    see ()

    if motion % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    while True:
        x, y = map(int, input('Ваш ход. Введите координаты:').split())
        if check(x, y):
            break

    if motion % 2 == 1:
        fild[x][y] = "X"
    else:
        fild[x][y] = "0"

    if  motion == 9:
        break
        print('Ничья')