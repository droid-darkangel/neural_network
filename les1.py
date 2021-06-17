#импорт библиотек
import numpy as np

#функция прогона неиросети
def act(x):
    return 0 if x < 0.5 else 1

#функция неиросети
def go(house, rap, nice):
    x = np.array([house, rap, nice])
    w1 = [0.3, 0.3, 0]
    w2 = [0.4, -0.5, 1]
    weight1 = np.array([w1, w2])
    weight2 = np.array([-1, 1])

    sum = np.dot(weight1, x)

    out_sum = np.array([act(x) for x in sum])

    sum_end = np.dot(weight2, out_sum)
    y = act(sum_end)

    return y
while True:
#ввод данных и исключения
    try:
        house = int(input('Есть дом или нету (1 или 0): '))
        rap = int(input('Слушаешь рэп или нет (1 или 0): '))
        nice = int(input('Ты красивый или нет (1 или 0): '))
    except ValueError:
        print('Введите 0 или 1!')
    if house>1 or house<0:
        print('Введите 0 или 1!')
    if rap>1 or rap<0:
        print('Введите 0 или 1!')
    if nice>1 or nice<0:
        print('Введите 0 или 1!')

    #результат неиросети
    if house in range(0, 2) and rap in range(0, 2) and nice in range(0, 2):
        res = go(house, rap, nice)
        if res == 1:
            print('Ты мне нравишься!')
        else:
            print('Гуляй, мальчик')