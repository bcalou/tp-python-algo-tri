import time
from typing import Callable

from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.fusion import sort as fusion_sort
from sort.range import tab_list


def test_sort_function(sort_function: Callable, label: str):
    """Test of a sort function"""
    print(f"{label}\n")
    for tab in tab_list:
        start: float = time.time()
        # print(f"{tab_list.index(tab)}")
        sort_function(tab.copy())
        end: float = time.time()
        print("Temps écoulé :", end - start)


def test_python_sort_function():
    """test of python sort function"""
    print(f"Python Sort\n")
    for tab in tab_list:
        start: float = time.time()
        # print(f"{tab_list.index(tab)}")
        tab.copy().sort()
        end: float = time.time()
        print("Temps écoulé :", end - start)


test_sort_function(selection_sort, "Test par sélection")
test_sort_function(insertion_sort, "Test par insertion")
test_sort_function(fusion_sort, "Test par fusion")
test_python_sort_function()
