# import range as list_range


def sort_by_fusion(input_list: list[int]) -> list[int]:
    def sort(sort_input: list[int]) -> list[int]:
        if len(sort_input) <= 1:
            return sort_input
        first_part = sort(sort_input[:len(sort_input) // 2])
        second_part = sort(sort_input[len(sort_input) // 2:])
        return merge(first_part, second_part)

    def merge(merge_input1: list[int], merge_input2: list[int]) -> list[int]:
        output = []
        while len(merge_input1) > 0 and len(merge_input2) > 0:
            input1_value = merge_input1[0]
            input2_value = merge_input2[0]

            if (input1_value < input2_value):
                output.append(merge_input1.pop(0))
            else:
                output.append(merge_input2.pop(0))

        if len(merge_input1) > 0:
            output += merge_input1
        else:
            output += merge_input2
        return output

    return sort(input_list)


# random_list = list_range.generate_random_list(100000)
# print(random_list)
# print(sort_by_fusion(random_list))
