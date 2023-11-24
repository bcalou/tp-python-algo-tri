from sort.range import generate_array_of_number
from sort.insertion import sort
import time

def main():
    array_list: list[list[int]] = []
    array_size: int = 1000
    for i in range (10):
        array_list.append(generate_array_of_number(array_size))
        array_size += 1000

    for i in range (10):
        start: float = time.time()
        sort(array_list[i])
        end: float = time.time()
        print(f"Temps écoulé pour {len(array_list[i])} :", end - start)
    #sort([5,2,1])

main()
