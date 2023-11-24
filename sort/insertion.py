def sort(array: list[int]) -> list[int]:
    """Sort the array using insertion sort"""

    # nombre de nombre trié dans le tableau
    # On commence à 1 puisque qu'un tableau de taille 1 est trié
    number_of_sorted_numbers: int = 1

    # On parcours le tableau dans le sens croissant
    for index in range(1, len(array)):
        number: int = array[index]
        # on parcours la partie trié du tableau dans le sens décroissant
        for sorted_num_index in reversed(range(0, number_of_sorted_numbers)):
            sorted_number = array[sorted_num_index]

            if number < sorted_number and sorted_num_index > 0:
                # Le nombre actuel est plus petit que le nombre trié
                # et on n'est pas encore a la première case
                # On continue de traverser le tableau trié
                continue

            # On insère notre nombre, On vérifie si num<sorted_num
            # Car on peut se trouver dans le cas où index==0
            # On doit donc vérifier où placer le nombre
            array.pop(index)

            # Si number > sorted_number alors insert à l'index 1
            # Sinon insert à l'index 0
            array.insert(number > sorted_number, number)

            # Le nombre de nombre trié augmente
            number_of_sorted_numbers += 1

            # On a placé notre nombre, on quitte cette boucle
            break

    return array
