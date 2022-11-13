"""
Recursion practice
"""


from webbrowser import get


def get_factorial(number: int) -> int:
    return 1 if number <= 1 else number * get_factorial(number - 1)


print(get_factorial(5))


print(get_factorial(100))
