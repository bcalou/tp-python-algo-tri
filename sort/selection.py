"""
Selection sort
"""

import time as t
import rd_list_generator as rg

def main():
    """Main function
    """
    array = rg.generate_array_of_number(1000)

    start: float = t.time()
    sort(array)
    print("Sorted :", t.time()-start, "s")

def sort(array: list[int]) -> list[int]:
    """Sorts an array using the selection sort algorithm
    """
    for index_to_move in range(len(array)):
        #On ne revérifie pas les éléments déjà triés
        min_index = index_to_move
        for index_to_check in range(min_index + 1, len(array)):
            #On cherche l'index du plus petit élément
            if array[index_to_check] < array[min_index]:
                min_index = index_to_check
                
        #On échange l'élément le plus petit avec l'élément à sa place
        array[index_to_move], array[min_index] = array[min_index], array[index_to_move]

    return array


if __name__ == "__main__":
    main()