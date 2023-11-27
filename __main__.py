from sort.range import generate_array_of_number
from sort.selection import sort

def main():
    arr = generate_array_of_number(100)
    sortarr = sort(arr)
    print(sortarr)

main()
