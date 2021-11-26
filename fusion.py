final_test: list[int] = [10,5,1,3,4,2,7]

def merge(list1: list[int], list2: list[int]) -> list[int]:
    final_list: list[int] = []
    size_list1 = len(list1)
    size_list2 = len(list2)

    while len(final_list) < size_list1 + size_list2:
        if list1 == []:
            final_list.extend(list2)
        elif list2 == []:
            final_list.extend(list1)
        elif list1[0] <= list2[0]:
            final_list.append(list1[0])
            list1.pop(0)
        else:
            final_list.append(list2[0])
            list2.pop(0)
    return final_list

def sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    middle_index: int = len(array)//2
    left_array: list[int] = sort(array[middle_index:])
    right_array: list[int] = sort(array[:middle_index])

    return merge(right_array, left_array)

print(sort(final_test))
