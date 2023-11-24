import time
import matplotlib.pyplot as plt
from sort.range import generate_array_of_number
import sort.selection as selection
import sort.insertion as insertion
import sort.fusion as fusion


def main():

    tests: list[list[int]] = []

    plt.figure()
    plt.xlabel("Array Size")
    plt.ylabel("Compute Time")
    plt.title("Faisons le tri - Hugo JEUDY")

    array_sizes: list[int] = []
    generation_times: list[float] = []
    selection_times: list[float] = []
    insertion_times: list[float] = []
    fusion_times: list[float] = []
    sort_times: list[float] = []

    for i in range(100000, 2000001, 50000):

        print(f"Doing it with {i}")

        array_sizes.append(i)

        # compute array completion

        timer_start: float = time.time()
        rand_numbers_array: list[int] = generate_array_of_number(i)
        timer_end: float = time.time()
        generation_times.append(timer_end - timer_start)

        # compute array selection sort

        # selection_array = rand_numbers_array.copy()
        # timer_start = time.time()
        # selection.sort(selection_array)
        # timer_end: float = time.time()
        # selection_times.append(timer_end - timer_start)

        # compute array insertion sort

        # insertion_array = rand_numbers_array.copy()
        # timer_start = time.time()
        # insertion.sort(insertion_array)
        # timer_end: float = time.time()
        # insertion_times.append(timer_end - timer_start)

        # compute array fusion sort

        # fusion_array = rand_numbers_array.copy()
        # timer_start = time.time()
        # fusion.sort(fusion_array)
        # timer_end: float = time.time()
        # fusion_times.append(timer_end - timer_start)

        # compute array sort from python

        sort_array = rand_numbers_array.copy()
        timer_start = time.time()
        sort_array.sort()
        timer_end: float = time.time()
        sort_times.append(timer_end - timer_start)

    plt.plot(array_sizes, generation_times, "-",
             color='lightgrey', label='Array Generation')
    # plt.plot(array_sizes, selection_times, "-",
    #         color='darkolivegreen', label='Selection')
    # plt.plot(array_sizes, insertion_times, "-",
    #         color='mediumslateblue', label='Insertion')
    # plt.plot(array_sizes, fusion_times, "-", color='peru', label='Fusion')
    plt.plot(array_sizes, sort_times, "-", color='coral', label="Sort")

    plt.legend()
    plt.show()


main()
