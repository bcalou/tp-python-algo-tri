def sort_by_selection(input_list: list[int]) -> list[int]:
    for validated_count in range(len(input_list)):
        min_value = input_list[validated_count]
        min_value_index = validated_count

        for i in range(validated_count, len(input_list)):

            current_value = input_list[i]

            if current_value < min_value:
                min_value = current_value
                min_value_index = i

        # print(
        #     f"{input_list[min_value_index]} -> {input_list[validated_count]}")
        input_list[validated_count], input_list[min_value_index] = input_list[min_value_index], input_list[validated_count]

    return input_list
