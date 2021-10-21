import time
import range
import selection
import insertion
import fusion

list_size: int = 10000
print("List size :", list_size)
print("--------------------------------------")

start: float = time.time()
array: list[int] = range.create_list(list_size)
end: float = time.time()

print("Create List \t- " + '%.2f' % (end - start) + "s")

selection_array: list[int] = array[:]
start = time.time()
selection.sort(selection_array)
end = time.time()

print("Selection sort \t- " + '%.2f' % (end - start) + "s")

insertion_array: list[int] = array[:]
start = time.time()
insertion.sort(insertion_array)
end = time.time()

print("Insertion sort \t- " + '%.2f' % (end - start) + "s")

fusion_array: list[int] = array[:]
start = time.time()
fusion.sort(insertion_array)
end = time.time()

print("Merge sort \t- " + '%.2f' % (end - start) + "s")

python_array: list[int] = array[:]
start = time.time()
python_array.sort()
end = time.time()

print("Python sort \t- " + '%.2f' % (end - start) + "s")
