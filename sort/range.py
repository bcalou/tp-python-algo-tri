import time
import random

def generate_array_of_number(array_size: int) -> list[int]:

    start: float = time.time()

    random_numbers: list[int] = [random.randint(0, 100) for i in range(array_size)]

    end: float = time.time()

    print(f"Génération de {array_size} nombres aléatoires en {end-start:.2f}s")

    return random_numbers

# Résultats
# Génération de 1000000 nombres aléatoires en 1.42s
# Génération de 2000000 nombres aléatoires en 3.20s
# Génération de 3000000 nombres aléatoires en 3.96s
# Génération de 4000000 nombres aléatoires en 5.15s
# Génération de 5000000 nombres aléatoires en 6.32s
# Génération de 6000000 nombres aléatoires en 7.66s
# Génération de 7000000 nombres aléatoires en 8.97s
# Génération de 8000000 nombres aléatoires en 10.20s
# Génération de 9000000 nombres aléatoires en 11.47s
# Génération de 10000000 nombres aléatoires en 13.51s