import time
from typing import Callable
from typing import TypedDict

from sort.fusion import sort as fusion_sort
from sort.insertion import sort as insertion_sort
from sort.range import generate_array_of_number
from sort.selection import sort as selection_sort

algorithms = (
    insertion_sort,
    selection_sort,
    fusion_sort,
)

array_sizes = (1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)
array_sizes_generate_array = (1_000_000, 2_000_000, 3_000_000, 4_000_000,
                              5_000_000, 6_000_000, 7_000_000, 8_000_000,
                              9_000_000, 10_000_000)


class FunctionMetrics(TypedDict):
    """Function metrics"""
    name: str
    sort_metrics: dict[int, float]


def get_metrics(sort_function: Callable) -> dict[int, float]:
    """Get metrics for sort functions"""
    time_metric: dict[int, float] = {}
    for array_size in array_sizes:
        start_time = time.time()
        print(f"Testing for array size: {array_size}")
        sort_function(generate_array_of_number(array_size))
        end_time = time.time()
        time_metric[array_size] = end_time - start_time
    return time_metric


def main():

    # Used to test the time it takes to sort lists using python sort function
    for array_size in array_sizes:
        start_time = time.time()
        generate_array_of_number(array_size).sort()
        end_time = time.time()
        print(end_time - start_time)

    # Used to test the time it takes to sort lists using the fusion sort,
    # selection sort and insertion sort algorithms
    metrics: list[FunctionMetrics] = []
    for algorithm in algorithms:
        metrics.append({
            "name": algorithm.__name__,
            "sort_metrics": get_metrics(algorithm)
        })

    # Print metrics
    for metric in metrics:
        print(f"Metrics for {metric['name']}")
        for array_size, time_metric in metric["sort_metrics"].items():
            print(f"Array size: {array_size} - Time: {time_metric}")


main()
