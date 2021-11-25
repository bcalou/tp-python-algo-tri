import random
import time

def insertion_sort(array: list[int]) -> list[int]:

    for start in range(len(array)):
        current_number: int = array[start]
        for i in range(start-1, -1, -1):
            if current_number < array[i]:
                temp: int = array[i]
                array[i] = current_number
                array[i+1] = temp
            else:
                break
    return array

tableau: list[int] = [random.randint(0, 100) for _ in range(1000)]
start: float = time.time()
insertion_sort(tableau)
end: float = time.time()
print("Temps écoulé pour 1 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(5000)]
start: float = time.time()
insertion_sort(tableau)
end: float = time.time()
print("Temps écoulé pour 5 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(10_000)]
start: float = time.time()
insertion_sort(tableau)
end: float = time.time()
print("Temps écoulé pour 10 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(20_000)]
start: float = time.time()
insertion_sort(tableau)
end: float = time.time()
print("Temps écoulé pour 20 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(50_000)]
start: float = time.time()
insertion_sort(tableau)
end: float = time.time()
print("Temps écoulé pour 50 000 entrées:", end - start)