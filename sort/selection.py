def sort(array: list[int]) -> list[int]:
    '''
        Sort an array using selection sort.
    '''
    for i in range(len(array)):
        # Checking all element of the array

        compared_element: int = array[i]

        temp_element: int = compared_element
        switch_index: int = i

        for j in range(i + 1, len(array)):
            # checking the rest of the array in search for smaller elements

            if (array[j] < temp_element):

                temp_element = array[j]
                switch_index = j

        if compared_element != temp_element:
            # switching the two elements if a smaller one has been found
            array[i] = temp_element
            array[switch_index] = compared_element

    return array
