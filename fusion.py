import random
import time

def sort(tab:list[int])-> list[int]:
    if(len(tab) > 1):
        middle_tab_cut:int = len(tab)//2
        tab_first_part = tab[:middle_tab_cut+(len(tab)%2)]
        tab_second_part = tab[-middle_tab_cut:]
        sort_tab_left = sort(tab_first_part)
        sort_tab_right = sort(tab_second_part)
        tab_merge = merge(sort_tab_left,sort_tab_right)
        return tab_merge
    else:
        return tab

def merge(tab_first_part:list[int],tab_second_part:list[int])-> list[int]:
    left_index:int = 0
    right_index:int = 0
    merge_tab: list[int] = []

    while left_index < len(tab_first_part) and right_index < len(tab_second_part):
        if tab_first_part[left_index] < tab_second_part[right_index]:
            merge_tab.append(tab_first_part[left_index])
            left_index+=1
        else :
            merge_tab.append(tab_second_part[right_index])
            right_index+=1


    while left_index < len(tab_first_part):
        merge_tab.append(tab_first_part[left_index])
        left_index+=1


    while right_index < len(tab_second_part):
        merge_tab.append(tab_second_part[right_index])
        right_index+=1

    return merge_tab    



def fusion_sort():
    for i in range(1,11):
        tab = [random.randint(0, 100) for i in range(1_000*i)]
        start: float = time.time()
        tab_fusion = sort(tab)
        end : float = time.time()
        print("Temps écoulé pour " + str(1_000 * i) + ":", end - start, "s")

fusion_sort()