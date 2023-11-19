def sort(array: list[int]) -> list[int]:
    '''
        Sort an array using insertion sort.
    '''
    
    for i in range(len(array)) :

        compared_element: int = array[i]

        j: int = i - 1

        while array[j] > compared_element and j >= 0 :

            array[j + 1] = array[j]
        
            j -= 1
        
        array[j + 1] = compared_element

    return array
