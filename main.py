import random as rd

from exercices.range import *
from exercices.selection import basic_list_sort
from exercices.insertion import insertion_sort
from exercices.recursion import factorial
from exercices.fusion import fusion_sort, list_fusion


datas = [
    {'tested_size' : 100_000,
    "tested_function" : generate_randint_list,
    'tested_data' : lambda size : size
    },
    {'tested_size' : 100,
    "tested_function" : basic_list_sort,
    'tested_data' : lambda size : [rd.randint(0,10000) for i in range(size)]
    },
    {'tested_size' : 1000,
    "tested_function" : insertion_sort,
    'tested_data' : lambda size : [rd.randint(0,1000) for i in range(size)]
    },
    {'tested_size' : 10_000,
    "tested_function" : fusion_sort,
    'tested_data' : lambda size : [rd.randint(0,1000) for i in range(size)]
    }
]


class TestedFile():
    RANDINT = 0
    SELECTION_SORT = 1
    INSERTION_SORT = 2
    FUSION_SORT = 3

_file = TestedFile.FUSION_SORT

print("\nQuantitée;Temps exécution(s)")
# fait 10 tests en augmentant la taille d'échantillon par tested_size
for batch_size in range(datas[_file]['tested_size'], datas[_file]['tested_size'] * 11, datas[_file]['tested_size']) :
    
    # fait une moyenne sur 10 lancement de la fonction et retournele temps d'éxécution moyen
    exe_time : float = get_avg_exe_time_for(datas[_file]['tested_function'],
                                            datas[_file]['tested_data'],
                                            batch_size)
    
    # petit print a coller dans un excel
    print(batch_size, ";" + str(exe_time).replace('.', ','))
