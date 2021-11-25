import time
import random

def tri_selection(table: list) -> list:
    smallest_number: int = 0
    smallest_number_index: int = 0
    table_length: int = len(table)

    for number in range(table_length):
        for compared_number in range(number,table_length):
            if smallest_number > table[compared_number]:
                smallest_number = table[compared_number]
                smallest_number_index = compared_number
        table[number], table[smallest_number_index] = table[smallest_number_index], table[number]
    return table


table = [random.randint(0, 100) for i in range(30000)]

start: float = time.time()
tri_selection(table)
end: float = time.time()
print("Temps écoulé :", end - start)
