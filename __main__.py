import sort.range
import sort.selection as selection
import matplotlib.pyplot as plt
import sort.insertion as insertion
import time
import sort.fusion as fusion


def get_1k_10k_arrays_execution_times(sorting_method) -> tuple[list[float],
                                                               list[int]]:
    """Returns the execution times and array sizes of
    generated arrays of 1k to 10k numbers with a step of 1k."""

    times: list[float] = []
    sizes: list[int] = []

    for i in range(1, 11):
        array_size: int = 1000*i
        array: list[int] = sort.range.generate_array_of_number(array_size)
        execution_time: float = get_execution_time(array, sorting_method)
        print(f"Execution time for {array_size} numbers: {execution_time} s")
        sizes.append(array_size)
        times.append(execution_time)

    return times, sizes


def get_execution_time(array: list[int], sorting_method) -> float:
    """Returns the execution time for sorting the given array
    with given sorting method."""

    start: float = time.time()
    sorting_method(array)
    end: float = time.time()
    return end - start


def draw_graph(sizes: list[int], times: list[float], title: str):
    """Draws a graph with the given input sizes and execution times."""

    plt.plot(sizes, times, 'ro-')
    plt.xlabel('Input size')
    plt.ylabel('Execution time (s)')
    plt.title(title)
    plt.show()


def main():
    """Main function."""

    sort.range.execution_time_for_array_of_numbers()

    sizes: list[int] = []
    times: list[float] = []

    # Selection sort
    times, sizes = get_1k_10k_arrays_execution_times(selection.sort)
    draw_graph(sizes, times, "Selection sort")

    # Insertion sort
    times, sizes = get_1k_10k_arrays_execution_times(insertion.sort)
    draw_graph(sizes, times, "Insertion sort")

    # Fusion sort
    times, sizes = get_1k_10k_arrays_execution_times(fusion.sort)
    draw_graph(sizes, times, "Fusion sort")

    # Python built-in sort
    times, sizes = get_1k_10k_arrays_execution_times(sorted)
    draw_graph(sizes, times, "Python built-in sort")


main()
