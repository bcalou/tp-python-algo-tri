def factorial(number: int):
    if number == 1:
        return 1
    return number * factorial(number - 1)


# print(factorial(5))
# -> 120
