def factorial (number : int) -> int :
    result = 1 if number == 1 else number * factorial(number - 1)
    return result

print(factorial(100))