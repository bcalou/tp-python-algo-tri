"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:
    '''sort selection algorithm'''

    # left out sort array part
    for iterator in range(len(array)):

        buffer_index: int = iterator
        buffer_value: int = array[iterator]

        for index in range (iterator, len(array)):
            if(array[index] < buffer_value):
                
                buffer_value = array[index]
                buffer_index = index
        
        array[iterator], array[buffer_index] = array[buffer_index], array[iterator]

    return array
