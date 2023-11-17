def sort(array: list[int]) -> list[int]:
    """Sorts the array using selection sort"""

    array_size: int = len(array)

    # `number_of_sorted_numbers` helps keep track of how many value has been
    # sorted so far
    # It tells us where we have to insert the lowest value we found
    for number_of_sorted_numbers in range(array_size):

        # `smallest_number` stores the smallest number found
        # `smallest_number_index` stores its index
        # we intialize them with the first value of the table that
        #  isnt sorted yet
        smallest_number: int = array[number_of_sorted_numbers]
        smallest_number_index: int = number_of_sorted_numbers

        # We go through the part of the table that is not sorted
        # and store the smallest value
        for index in range(number_of_sorted_numbers, array_size):
            number: int = array[index]
            if number < smallest_number:
                smallest_number = number
                smallest_number_index = index

        # We remove the smallest number with its index
        array.pop(smallest_number_index)
        # We insert it back after the other sorted numbers
        array.insert(number_of_sorted_numbers, smallest_number)

    return array
