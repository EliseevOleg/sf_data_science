from random import random
import numpy as np



def random_predict(number:int = 1) -> int:
    """AI is creating summary for randem_predict

    Args:
        number (int, optional): [description]. Defaults to 1.

    Returns:
        int: [description]
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if predict_number == number:
            break
        
    return count
    
    
def score_game(random_predict) -> int:
    """AI is creating summary for score_game

    Args:
        random_predict ([type]): [description]

    Returns:
        int: [description]
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000) )

    for number in random_array:
        count_ls.append( random_predict(number) )
        
    score = int( np.mean(count_ls))
    print( f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
if __name__ == '__main':
    score_game( random_predict )


