import time
import random

def tri_insertion(table: list) -> list:
    table_length: int = len(table)

    for i in range(table_length):
        for j in range(i,0,-1):
            if table[j] < table[j-1] and j != 0:
                table[j], table[j-1] = table[j-1], table[j]
    return table

table = [random.randint(0, 100) for i in range(20000)]

start: float = time.time()
tri_insertion(table)
end: float = time.time()
print("Temps écoulé :", end - start)