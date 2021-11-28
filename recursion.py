import random
import time

#Exemple of a recursive function (here with factorial)
def factorial(number : int) -> int:
    return 1 if number == 1 else number*factorial(number-1)


print(factorial(5))