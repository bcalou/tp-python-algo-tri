import sort.range as srange
import sort.selection as selection
import sort.insertion as insertion
import sort.fusion as fusion
import time


def main():
    for i in range(10000):
        array: list[int] = srange.generate_array_of_number(i)
        start: float = time.time()
        print(fusion.sort(array) == sorted(array))
        end: float = time.time()
        print(str(end - start).replace(".", ","))


main()
