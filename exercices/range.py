import time
import random as rd
from typing import List


def get_avg_exe_time_for(func, arg_func,batch_size=10, avg_size = 10) -> float:
    """func is the tested function and arg_func is a function that return func arguments"""
    avg: float = 0
    for i in range(avg_size):
        start : float = time.time()
        func(arg_func(batch_size))
        end : float = time.time()
        avg += end - start
    avg = round(avg / 10, 3)
    return avg


def generate_randint_list(size : int) -> list[int]:
    list : List[int] = [rd.randint(0,100) for i in range(size)]
    return list


if __name__ == "__main__":
    print("Quantitée;Temps exécution(s)")
    for size in range(1_000_000, 10_000_001, 1_000_000):
        avg: float = 0
        for i in range(10):
            avg += get_avg_exe_time_for(generate_randint_list, size)
        avg = round(avg / 10, 3)
        print(size, ";" + str(avg).replace('.', ','))
        