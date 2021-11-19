import random
import time
from plot import plot_graph

# Sort a table by merging
# Complexity seems to be o(n*log(n))
def merge_sort(table: list[int]):
    if len(table) > 1:
        middle = len(table) // 2
        left = table[:middle]
        right = table[middle:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        main = 0
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
              table[main] = left[l]
              l += 1
            else:
                table[main] = right[r]
                r += 1
            main += 1

        while l < len(left):
            table[main] = left[l]
            l += 1
            main += 1

        while r < len(right):
            table[main]=right[r]
            r += 1
            main += 1
    return table

entries = []
time_per_entry = []

for i in range(1, 11):
    number_of_entries = 1000 * i
    table = [random.randint(0, 10000) for i in range(number_of_entries)]
    start: float = time.time()
    merge_sort(table)
    end: float = time.time()
    time_elpased = end - start
    entries.append(number_of_entries)
    time_per_entry.append(time_elpased)
    print(str(number_of_entries) + " entries sorted.")

plot_graph(entries, time_per_entry, "fusion.png")