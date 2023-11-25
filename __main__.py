from sort.range import generate_array_of_number
from sort.selection import sort, time_to_sort_selection
from sort.insertion import sort, time_to_sort_insertion

def main():
    
    print("---Temps Exec Tri Selection---")
    time_to_sort_selection(1000)
    time_to_sort_selection(2000)
    time_to_sort_selection(3000)
    time_to_sort_selection(4000)
    time_to_sort_selection(5000)
    time_to_sort_selection(6000)
    time_to_sort_selection(7000)
    time_to_sort_selection(8000)
    time_to_sort_selection(9000)
    time_to_sort_selection(10000)
    
    print("---Temps Exec Tri Insertion---")
    time_to_sort_insertion(1000)
    time_to_sort_insertion(2000)
    time_to_sort_insertion(3000)
    time_to_sort_insertion(4000)
    time_to_sort_insertion(5000)
    time_to_sort_insertion(6000)
    time_to_sort_insertion(7000)
    time_to_sort_insertion(8000)
    time_to_sort_insertion(9000)
    time_to_sort_insertion(10000)


main()
