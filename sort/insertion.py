def sort(array: list[int]) -> list[int]:
    """sort a given list by comparing values 2 per 2,
    placing the lowest value to the left"""

    for index, value in enumerate(array):
        for i in range(1, len(array[:index])+1):
            #Can't compare a value with nothing before
            if index == 0:
                break
            if value < array[index-i]:
                array[index-i], array[index-i+1] = value, array[index-i]
            else:
                break

    return array
