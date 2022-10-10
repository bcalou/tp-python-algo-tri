"""
Number generator
"""
import random
import time as t

def main() -> None:
    """Main function
    """
    generate_array_of_number(1)
    generate_array_of_number(2)
    generate_array_of_number(3)
    generate_array_of_number(5)
    generate_array_of_number(10)
    generate_array_of_number(50)
    generate_array_of_number(200)
    generate_array_of_number(1000)
    generate_array_of_number(10000)
    generate_array_of_number(50000)
    generate_array_of_number(100000)
    generate_array_of_number(200000)
    generate_array_of_number(500000)
    generate_array_of_number(1000000)

def generate_array_of_number(array_size: int) -> list[int]:
    """Generates an array of random numbers
    """
    start: float = t.time()
    to_ret: list[int] = [random.randint(0, 100) for _ in range(array_size)]
    print("Generated :", t.time()-start, "s")
    return to_ret


if __name__ == "__main__":
    main()
