import time
import numpy as np
import matplotlib.pyplot as plt
from sort.fusion import sort as fusion_sort
from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.range import generate_array


def measure_time(algo_func, array):
    """Mesurer la durée d'exécution d'une fonction de tri"""
    start_time = time.time()
    algo_func(array)
    end_time = time.time()
    return end_time - start_time


def main():
    """Fonction principale"""
    max_tab_size = int(input("Enter the maximum size of the array: "))
    num_sizes = int(input("Enter the number of array sizes to generate: "))
    critical_time = float(input("Enter the critical time for stopping the \
                                execution (in seconds): "))

    # Choix de l'échelle avec par défaut la logarithmique
    scale_choice = input("Choose scale (linear/log): ").lower()
    if scale_choice not in ['linear', 'log']:
        # Utilisation de l'échelle logarithmique par défaut
        scale_choice = 'log'

    # Générer des tableaux intermédiaires de taille croissante
    if scale_choice == 'log':
        sizes = np.logspace(0, np.log10(max_tab_size), num=num_sizes,
                            endpoint=True, base=10, dtype=int)
    else:
        sizes = np.linspace(1, max_tab_size, num=num_sizes, dtype=int)

    selection_times = []
    insertion_times = []
    fusion_times = []

    # Variables de contrôle pour arrêter la mesure du temps pour chaque algo
    stop_selection = False
    stop_insertion = False
    stop_fusion = False

    for size in sizes:
        tab = generate_array(size)

        # Mesurer la durée d'exécution du tri par SELECTION
        if not stop_selection:
            selection_time = measure_time(selection_sort, tab.copy())
            selection_times.append(selection_time)
            if size < max_tab_size and selection_time > critical_time:
                print(f"Selection Sort exceeded critical time ({critical_time}\
                      seconds) for size {size}. Stopping.")
                stop_selection = True

        # Mesurer la durée d'exécution du tri par insertion
        if not stop_insertion:
            insertion_time = measure_time(insertion_sort, tab.copy())
            insertion_times.append(insertion_time)
            if size < max_tab_size and insertion_time > critical_time:
                print(f"Insertion Sort exceeded critical time ({critical_time}\
                      seconds) for size {size}. Stopping.")
                stop_insertion = True

        # Mesurer la durée d'exécution du tri par FUSION
        if not stop_fusion:
            fusion_time = measure_time(fusion_sort, tab.copy())
            fusion_times.append(fusion_time)
            if size < max_tab_size and fusion_time > critical_time:
                print(f"Fusion Sort exceeded critical time ({critical_time}\
                      seconds) for size {size}. Stopping.")
                stop_fusion = True

        # Vérifier si tous les algorithmes ont atteint le seuil critique
        if stop_selection and stop_insertion and stop_fusion:
            break

    # Créer un graphique avec la légende à gauche
    plt.plot(sizes[:len(selection_times)], selection_times,
             label='Selection Sort', marker='o')
    plt.plot(sizes[:len(insertion_times)], insertion_times,
             label='Insertion Sort', marker='o')
    plt.plot(sizes[:len(fusion_times)], fusion_times, label='Fusion Sort',
             marker='o')

    if scale_choice == 'log':
        # Utiliser échelle logarithmique pour l'axe des x
        plt.xscale('log')

    # Paramètres du graph
    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend(loc='upper left')
    plt.show()


main()
