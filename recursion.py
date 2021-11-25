import random
import time


def factorial(number : int) -> int:
    return 1 if number == 1 else number*factorial(number-1)


print(factorial(5))