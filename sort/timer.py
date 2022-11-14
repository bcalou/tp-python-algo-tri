"""
Timer functions
"""

from typing import Callable
import time
from sort.range import generate_array_of_number


def test_array_generation_function(step: int):
    """Test the array generation 10 times with increasing array sizes"""
    for array_size in range(step, step * 11, step):
        execution_time: float = get_execution_time(
            lambda size=array_size: generate_array_of_number(size)
        )
        print(f"{array_size} entrées : {execution_time}s")


def test_sort_function(function: Callable, step: int):
    """Test the given sort function 10 times with increasing array sizes"""
    for array_size in range(step, step * 11, step):
        execution_time: float = get_execution_time(
          lambda size=array_size: function(generate_array_of_number(size))
        )
        print(f"{array_size} entrées : {execution_time}s")


def get_execution_time(function: Callable) -> float:
    """Get the time it takes to execute the given function"""
    # Start the timer
    start: float = time.time()

    # Call the function to be tested
    function()

    # Stop the timer
    end: float = time.time()

    # Return the ellapsed time
    return end - start
