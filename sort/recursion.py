def get_factorial_iterative(number: int) -> int:
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
