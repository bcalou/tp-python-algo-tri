import time

import matplotlib.pyplot as plt

import fusion
import insertion
import range as list_range
import selection


def benchmark(name: str, count: int, debug=False, multiplier: int = 10 ** 3):
    durations: list[float] = []
    list_sizes: list[int] = []

    for i in range(count):
        list_size = (i + 1) * multiplier

        start: float = time.time()
        if name == 'range':
            list_range.generate_random_list(list_size)
        elif name == 'selection':
            random_list = list_range.generate_random_list(list_size)
            selection.sort_by_selection(random_list)
        elif name == 'insertion':
            random_list = list_range.generate_random_list(list_size)
            insertion.sort_by_insertion(random_list)
        elif name == 'fusion':
            random_list = list_range.generate_random_list(list_size)
            fusion.sort_by_fusion(random_list)
        elif name == 'sort':
            random_list = list_range.generate_random_list(list_size)
            random_list.sort()
        end: float = time.time()
        duration: float = end - start

        durations.append(duration)
        list_sizes.append(list_size / 10 ** 3)

        if debug:
            print(f"Itération: {i}, Temps écoulé :{end - start}")

    plt.plot(list_sizes, durations)
    plt.ylabel("Temps d'éxécution")
    plt.xlabel("Taille de la liste (en millier)")
    plt.show()


# benchmark("range", 10, True, 10**3)
# benchmark("selection", 10, True)
# benchmark("insertion", 10, True)
# benchmark("fusion", 10, True)
benchmark("sort", 100, True)
