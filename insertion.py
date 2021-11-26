import time
start: float = time.time()

def tri_insertion(t): 
    # Parcourt de 1 à la taille du tableau t
    for i in range(1, len(t)): 
        k = t[i] 
        j = i-1
        while j >= 0 and k < t[j] : 
                t[j + 1] = t[j] 
                j -= 1
        t[j + 1] = k
# Pour tester le code ci-dessus
t = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(t) 
print ("Le tableau trié est :")
for i in range(len(t)): 
    print ("%d" % t[i])

end: float = time.time()
print("Temps écoulé :", end - start)