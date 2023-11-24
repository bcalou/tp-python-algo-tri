import sort.range as srange
import sort.selection as selection
import sort.insertion as insertion
import sort.fusion as fusion
import time


def main():
    """This is the main function !"""

    # Array Generation
    """for i in range(1000000, 1100000, 100000):
        start: float = time.time()
        array: list[int] = srange.generate_array_of_number(i)
        end: float = time.time()
        print(str(end - start).replace(".", ","))"""

    # Selection Sort
    """for i in range(10000, 100000, 10000):
        array: list[int] = srange.generate_array_of_number(i)
        start: float = time.time()
        selection.sort(array)
        end: float = time.time()
        print(str(end - start).replace(".", ","))"""

    # Insertion Sort
    """for i in range(10000, 100000, 10000):
        array: list[int] = srange.generate_array_of_number(i)
        start: float = time.time()
        insertion.sort(array)
        end: float = time.time()
        print(str(end - start).replace(".", ","))"""

    # Fusion Sort
    """for i in range(100000, 3100000, 100000):
        array: list[int] = srange.generate_array_of_number(i)
        start: float = time.time()
        fusion.sort(array)
        end: float = time.time()
        print(str(end - start).replace(".", ","))"""

    # Python Sort
    for i in range(100000, 3100000, 100000):
        array: list[int] = srange.generate_array_of_number(i)
        start: float = time.time()
        array.sort()
        end: float = time.time()
        print(str(end - start).replace(".", ","))


main()
