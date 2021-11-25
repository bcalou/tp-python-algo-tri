import time
import random

def tri_insertion(table: list[int]) -> list[int]:
    table_length: int = len(table)

    for i in range(table_length):
        value_to_sort = table[i]
        current_index = i-1
        while current_index >= 0 and value_to_sort < table[current_index]:
            table[current_index + 1] = table[current_index]
            current_index -= 1
        table[current_index + 1] = value_to_sort
    return table

table = [random.randint(0, 100) for i in range(30000)]

start: float = time.time()
#tri_insertion(table)
table.sort()
end: float = time.time()
print("Temps écoulé :", end - start)