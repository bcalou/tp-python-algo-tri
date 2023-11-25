import random


def generate_array_of_number(array_size: int) -> list[int]:
    '''
        Return a random numbers (0 to 100 both included) array
        with the given size
    '''
    return [random.randint(0, 100) for i in range(array_size)]
