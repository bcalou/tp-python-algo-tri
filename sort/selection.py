def sort(array: list[int]) -> list[int]:
    '''
        Sort an array using selection sort.
    '''
    for i in range(len(array)):
        compared_element: int = array[i]

        temp_element: int = compared_element
        switch_index: int = i

        for j in range(i + 1, len(array)):

            if (array[j] < temp_element):

                temp_element = array[j]
                switch_index = j

        if compared_element != temp_element:

            array[i] = temp_element
            array[switch_index] = compared_element

    return array
