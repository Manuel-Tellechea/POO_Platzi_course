import random


def insertion_sort(original_list):

    for index in range(1, len(original_list)):
        actual_value = original_list[index]
        actual_position = index

        while actual_position > 0 and original_list[actual_position - 1] > actual_value:
            original_list[actual_position] = original_list[actual_position - 1]
            actual_position -= 1

        original_list[actual_position] = actual_value

    return original_list


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista?: '))
    original_list = [random.randint(0, 100) for i in range(list_size)]
    print(original_list)

    sorted_list = insertion_sort(original_list)
    print(sorted_list)
