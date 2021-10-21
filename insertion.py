def sort(array: list[int]) -> list[int]:
    """
    Sorting a list by insertion (O(n²) complexity)
    """
    for start in range(len(array)):
        current_number: int = array[start]
        for i in range(start-1, -1, -1):
            # Move number until it's placed well
            if current_number < array[i]:
                temp: int = array[i]
                array[i] = current_number
                array[i+1] = temp
            else:
                break
    return array

if __name__ == "__main__":
    array: list[int] = [5, 8, -12, 4, 7, 0]
    print("Before sort :", array)
    print("After sort :", sort(array))
