import random
import time

number_entry : int = 10
array : list = [random.randint(0, number_entry) for i in range(number_entry)]

start: float = time.time()

#Function that split the list and return the sorted list.
def sort(table : list) :
    if len(table) <= 1 :
        return table
    #Finding the middle of the list
    cut = len(table) // 2
    #Create two tables (split)
    table1 = table[: cut]
    table2 = table[cut :]
    #Callback of the function to continue spliting
    left = sort(table1)
    right = sort(table2)
    return list(merge(left, right))

#Function that merge the given splited list, while sorting themm into a new sorted list.
def merge(left_table, right_table) :
    result = []
    index_left = index_right = 0
    #Comparing the first numbers of each list to keep the lowest one
    while index_left < len(left_table) and index_right < len(right_table) :
        if left_table[index_left] <= right_table[index_right] :
            #Adding the number into the sorted list
            result.append(left_table[index_left])
            index_left += 1
        else :
            #Adding the number into the sorted list
            result.append(right_table[index_right])
            index_right += 1
    #Adding the rest of the numbers
    result.extend(left_table[index_left :])
    result.extend(right_table[index_right :])
    return result

sort(array)
end: float = time.time()
print("Temps écoulé :", end - start)

