# Selection sort
def sort(arr) -> list[int]:
    """Sorts the given array using selection sort."""

    for i in range(len(arr)):
        min_idx: int = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
