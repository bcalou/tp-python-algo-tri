import random
import time


def generate_random_list(length: int) -> list[int]:
    """ Generates and returns a list of random numbers and prints the process duration in seconds """
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(length)]
    end: float = time.time()
    print("Temps écoulé :", end - start)
    return array


# for i in range(10):
#     generate_random_list(i * 10 ** 6)

# Result:
# Temps écoulé : 0.0
# Temps écoulé : 0.6792373657226562
# Temps écoulé : 1.4570631980895996
# Temps écoulé : 2.048525810241699
# Temps écoulé : 2.6668732166290283
# Temps écoulé : 3.2839043140411377
# Temps écoulé : 4.026287317276001
# Temps écoulé : 4.99465012550354
# Temps écoulé : 5.200124025344849
# Temps écoulé : 6.073075294494629
