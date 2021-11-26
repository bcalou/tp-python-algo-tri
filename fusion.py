import time
start: float = time.time()

#Tri fusion function of division of tab
def tri_fusion(tab):
    if  len(tab) <= 1: 
        return tab
    pivot = len(tab)//2
    tab1 = tab[:pivot]
    tab2 = tab[pivot:]
    gauche = tri_fusion(tab1)
    droite = tri_fusion(tab2)
    flr = fusion(gauche,droite)
    return flr


#Tri fusion function of fusion of 2 lists
def fusion(tab1,tab2):
    i_tab1 = 0
    i_tab2 = 0    
    size_tab1 = len(tab1)
    size_tab2 = len(tab2)
    tab_flr = []
    while i_tab1<size_tab1 and i_tab2<size_tab2:
        if tab1[i_tab1] < tab2[i_tab2]:
            tab_flr.append(tab1[i_tab1])
            i_tab1 += 1
        else:
            tab_flr.append(tab2[i_tab2])
            i_tab2 += 1
    while i_tab1<size_tab1:
        tab_flr.append(tab1[i_tab1])
        i_tab1+=1
    while i_tab2<size_tab2:
        tab_flr.append(tab2[i_tab2])
        i_tab2+=1
    return tab_flr

tab = [11, 222, 3, 899, 24, 5, 46, 67]
print(tab)
tab_trie = tri_fusion(tab)
print(tab_trie)

end: float = time.time()
print("Temps écoulé :", end - start)