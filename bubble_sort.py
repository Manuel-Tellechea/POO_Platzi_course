import random


def bubble_sort(original_list):
    n = len(original_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if original_list[j] > original_list[j + 1]:
                original_list[j], original_list[j + 1] = original_list[j + 1], original_list[j]

    return original_list


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista?: '))
    original_list = [random.randint(0, 100) for i in range(list_size)]
    print(original_list)

    sorted_list = bubble_sort(original_list)
    print(sorted_list)
