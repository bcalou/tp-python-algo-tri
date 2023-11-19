import sort.insertion as insertion
import time

def sort(array: list[int]) -> list[int]:
    '''
        Return the array by using fusion sort
    '''
    if len(array) <= 1 :
        return array
    else :
        half = len(array) // 2
        return merge(sort(array[:half]), sort(array[half:]))
        #return insertion.sort(sort(array[:half]) + sort(array[half:]))
    
def merge(array: list[int], array2: list[int]) -> list[int] :
    '''
        Merge two arrays by sorting them
    '''

    return insertion.sort(array + array2)