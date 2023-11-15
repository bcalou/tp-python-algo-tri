import unittest

from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.fusion import sort as fusion_sort


class TestSort(unittest.TestCase):
    test_arrays = [
        [1, 2, 3, 4, 5],
        [73, 16, 829, 2, 6],
        [-4, -282, 0, 7, 0],
        [1, 1, 1, 1, 1],
        [],
        [8],
    ]

    def test_selection_sort(self):
        for array in self.test_arrays:
            result = selection_sort(array.copy())
            expected = sorted(array)
            self.assertEqual(
                result,
                expected,
                f"Sorting {array} failed. \
                (expected: {expected}, got: {result})"
            )

    def test_insertion_sort(self):
        for array in self.test_arrays:
            result = insertion_sort(array.copy())
            expected = sorted(array)
            self.assertEqual(
                result,
                expected,
                f"Sorting {array} failed. \
                (expected: {expected}, got: {result})"
            )

    def test_fusion_sort(self):
        for array in self.test_arrays:
            result = fusion_sort(array.copy())
            expected = sorted(array)
            self.assertEqual(
                result,
                expected,
                f"Sorting {array} failed. \
                (expected: {expected}, got: {result})"
            )
