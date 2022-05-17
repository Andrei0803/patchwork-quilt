print("Игра: Лоскутное одеяло")
print("Правила игры: ")
print("Вводите координаты хода через пробел: строка, столбец")

players = ['1', '2', '3']  # обозначаем номер игрока, делающий ход
width = 5  # ширина таблицы
height = 4  # высота таблицы
table = [['*'] * width for i in range(height)]  # построение таблицы как массивы в массиве


def draw_board(a):  # рекурсия, создающая игровое поле со столбцами и строками
    print("-" * (len(table) * 5 + 1))  # выводит верхние границы строк на поле
    for i in range(len(a)):  # установка левых границ игрового поля
        print("|", end="")
        for j in range(len(a[0])):  # устновка правых границ игрового поля
            print(f" {a[i][j]} |", end="")
        print("\n" + "-" * (len(table) * 5 + 1))  # установка нижних границ ячеек игрового пол


draw_board(table)
print("Введите координаты хода: номер_строки номер_столбца")

move = 0  # ход
while move < 20:
    player = move % 3  # номер игрока, делающий ход
    try:  # если нет ошибки вводится ход определенного игрока и координаты
        y, x = map(int,
                   input(f'Ход игрока {player + 1}:').split())  # вводится: "ход игрока и его номер: строка столбец"
    except:  # в случаем ошибки при вводе просят ввести еще раз координаты
        print("Неверно введены координаты, введите еще раз")
        continue
    try:
        if table[y - 1][
            x - 1] == "*":  # проверка на определенный элемент игрового поля, если оно не занято звезда меняется на номер игрока, делающего ход
            table[y - 1][x - 1] = players[player]
        elif table[y - 1][x - 1] != "*":  # если на поле нет звезды, то выводится комментарий об ишибке
            print('Поле уже занято')
            move -= 1  # при вывидении ошибки номер хода остается прежним
        elif 'end' in x or y:  # если ячейки строки или столбца заняты игра завершается
            print('ffwfw')
            break
    except:  # если коорднинаты выходят за границу игрового поля выводится
        print('Введите координаты, удовлетворяющие количеству строк (1-5) и количеству столбцов (1-4)')
        continue
    draw_board(table)  # поле перерисовывается в соответствии с введенными координатами и игроком, который делает ход
    move += 1

dxy = [[-1, -1], [-1, 0], [-1, 1],  # создаем еще одно игровое поле для проверки соседних клеток
       [0, -1], [0, 0], [0, 1],
       [1, - 1], [1, 0], [1, 1]]
score = [0, 0, 0]  # записывается количество очков каждого игрока

# сравниваем соседние клетки для вычисления штрафных очков
for y in range(height):  # пробегаемся по строкам первого игрового поля
    for x in range(width):  # пробегаемся по столбцам первого игрового поля
        for i in range(len(dxy)):  # пробегаемся по новому двумерномц массиву
            kx, ky = x + dxy[i][0], y + dxy[i][1]  # задаем новым переменным координаты соседней переменной
            if 0 <= kx < 5 and 0 <= ky < 4:  # если координаты соответствуют всем правилам
                if table[y][x] == table[ky][
                    kx]:  # если значение переменной одного игрового поля равна значению соседней переменной другого игрового поля
                    score[int(table[y][x]) - 1] += 1  # у игрока, делающего ход увеличивается количество штрафны очков

# Теперь в score удвоенное количество штрафных очков каждого игрока
# Так что их все нужно поделить на 2
score = [i // 2 for i in score]
for i in range(
        len(players)):  # пробегаемся по всем массиву с номером игроков и выводим количество штрафных очков каждого игрока
    print(f'Игрок {i + 1} получил {score[i]} штрафных очков')

if score[0] < score[1] and score[0] < score[
    2]:  # если у 2 игрока штрафных очков больше, чем у 1, и у 3 игрока больше, чем у 1
    print(f'Победил 1-ый игрок')  # 1 игрок побеждает
elif score[1] < score[0] and score[1] < score[
    2]:  # если у 1 игрока штрафных очков больше, чем у 2, и у 3 игрока больше, чем у 2
    print(f'Победил 2-ой игрок')  # 2 игрок побеждает
elif score[2] < score[0] and score[2] < score[
    1]:  # если у 1 игрока штрафных очков больше, чем у 3, и у 2 игрока больше, чем у 3
    print(f'Победил 3-ий игрок')  # 3 игрок побеждает
elif (score[0] == score[1]) and score[0] < score[2] and score[1] < score[
    2]:  # если у 1 игрока столько же штрафных очков, как  у 2, и у 3 игрока больше, чем у 1 игрока, также у 3 игрока больше, чем у 2
    print(f'Победили два игрока 1 и 2')  # побеждает 1 и 2 игрок
elif (score[1] == score[2]) and score[1] < score[0] and score[2] < score[
    0]:  # если у 3 игрока столько же штрафных очков, как у 2, и у 1 игрока больше, чем у 2 игрока, также у 1 игрока больше, чем у 3
    print(f'Победили два игрока 2 и 3 ')  # 2 и 3 игрок побеждают
elif (score[0] == score[2]) and score[0] < score[1] and score[2] < score[
    1]:  # если у 3 игрока столько же штрафных очков, как у 1, и у 2 игрока больше, чем у 1 игрока, также у 2 игрока больше, чем у 3
    print(f'Победили два игрока 1 и 3')  # 1 и 3 игрок побеждают
elif score[0] == score[1] == score[2]:  # если у 1, 2 и 3 игрока одинаковое число штрафных очков
    print(f'Полная ничья!')  # ничья
