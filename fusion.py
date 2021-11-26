import time
import random

# Méthodes qui ne fonctionne pas.
# Essaie.

def sort(table: list[int]) -> list[int]:
    if len(table) <= 1:
        return table
    middle: int = len(table) // 2
    first_part: list[int] = table[:middle]
    second_part: list[int] = table[middle:]
    first_part = sort(first_part)
    second_part = sort(second_part)
    #print(first_part, second_part)
    final = merge(first_part, second_part)
    return final 

def merge(table1: list[int], table2: list[int]) -> list[int]:
    final_table : list[int] = []
    for i in table1:
        for j in table2: 
            if i > j:
                final_table.append(j)
                final_table.append(i)
            else:
                final_table.append(i)
                final_table.append(j)
    
    return final_table

array = [2, 11, 5, 3, 6, 4, 10, 9]

print(sort(array))
