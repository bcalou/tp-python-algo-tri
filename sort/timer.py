"""
Timer functions
"""

from typing import Callable
import time


def test_function_execution_times(function: Callable, step: int):
    """Test the given function 10 times with increasing values"""
    for input_size in range(step, step * 10, step):
        execution_time: float = get_execution_time(
          lambda size=input_size: function(size)
        )
        print(f"{input_size} entrées : {execution_time}s")


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
