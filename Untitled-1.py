"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np
def random_predict(number) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число.
    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) 
    count = 0 
    min = 1 
    max = 100 
    while True:
        count += 1
        if predict_number > number:
            max = predict_number - 1
            predict_number = (max + min) // 2
        elif predict_number < number:
            min = predict_number + 1
            predict_number = (max + min) // 2
        else:
            # print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break 
    return(count)
def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  
    random_array = np.random.randint(1, 101, size=(1000)) 
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(random_predict)