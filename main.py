import random as rd

from Exercices.range import *
from Exercices.selection import basic_list_sort
from Exercices.insertion import insertion_sort



print("Quantitée;Temps exécution(s)")

datas = [
    {'tested_size' : 100_000,
    "tested_function" : generate_randint_list,
    'tested_data' : lambda size : size
    },
    {'tested_size' : 100,
    "tested_function" : basic_list_sort,
    'tested_data' : lambda size : [rd.randint(0,10000) for i in range(size)]
    },
    {'tested_size' : 3,
    "tested_function" : insertion_sort,
    'tested_data' : lambda size : [rd.randint(0,100) for i in range(size)]
    }
    ]

class TestedFile():
    RANDINT = 0
    SELECTION_SORT = 1
    INSERTION_SORT = 2

_file = TestedFile.INSERTION_SORT

print("\nQuantitée;Temps exécution(s)")
# fait 10 test en augmentant la taille d'échantillon par tested_size
for batch_size in range(datas[_file]['tested_size'], datas[_file]['tested_size']*11, datas[_file]['tested_size']) :
    
    # fait une moyenne sur 10 lancement de la fonction et retournele temps d'éxécution moyen
    exe_time : float = get_avg_exe_time_for(datas[_file]['tested_function'],
                                            datas[_file]['tested_data'],
                                            batch_size)
    
    # petit print a coller dans un excel
    print(batch_size, ";" + str(exe_time).replace('.', ','))
