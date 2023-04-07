import pandas as pd
import numpy as np


chat_id = 720721680 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = (x + 36).mean() / 10
    return a
