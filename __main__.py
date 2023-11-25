from sort.range import generate_array_of_number, time_to_generate_array
from sort.selection import sort, time_to_sort_selection
from sort.insertion import sort, time_to_sort_insertion

def main():
    """Fonction principle, ici permettra de tester l'efficacité des algos"""
    
    print("---Temps Exec Génération Tableau---")
    time_to_generate_array(1000000)
    time_to_generate_array(2000000)
    time_to_generate_array(3000000)
    time_to_generate_array(4000000)
    time_to_generate_array(5000000)
    time_to_generate_array(6000000)
    time_to_generate_array(7000000)
    time_to_generate_array(8000000)
    time_to_generate_array(9000000)
    time_to_generate_array(10000000)
    
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
