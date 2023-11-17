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


# Résultats
# Trie par insertion: taille tableau=1000, temps=0.10017824172973633s
# Trie par insertion: taille tableau=2000, temps=0.2648162841796875s
# Trie par insertion: taille tableau=3000, temps=0.5844788551330566s
# Trie par insertion: taille tableau=4000, temps=1.1860754489898682s
# Trie par insertion: taille tableau=5000, temps=1.6009154319763184s
# Trie par insertion: taille tableau=6000, temps=2.032719135284424s
# Trie par insertion: taille tableau=7000, temps=2.8216004371643066s
# Trie par insertion: taille tableau=8000, temps=3.711418867111206s
# Trie par insertion: taille tableau=9000, temps=4.674601316452026s
# Trie par insertion: taille tableau=10000, temps=5.86929988861084s
