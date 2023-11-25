import random
import time

def main():
    '''Function to evaluate the algorithm complexity'''
    for size in range(1, 11):
        start_time = time.time()
        array_size = size * 1_000_000
        generate_array_of_number(array_size)
        end_time = time.time()
        print("Taille de tableau : ", array_size,
              " Temps écoulé :", end_time - start_time)

def generate_array_of_number(array_size: int) -> list[int]:
    """Generate an array of random numbers."""
    return [random.randint(0, 100) for _ in range(array_size)]

if __name__ == "__main__":
    main()
