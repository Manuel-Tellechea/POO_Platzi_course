import random


def merge_sort(user_list):
    if len(user_list) > 1:
        middle = len(user_list) // 2
        left = user_list[: middle]
        right = user_list[middle:]
        print(left, '*' * 5, right)

        # recursive call
        merge_sort(left)
        merge_sort(right)

        # Iterators to loop through the two sub-lists
        i = 0
        j = 0
        # Iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                user_list[k] = left[i]
                i += 1
            else:
                user_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            user_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            user_list[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}')
        print(user_list)
        print('-' * 50)

    return user_list


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista?: '))

    user_list = [random.randint(0, 100) for i in range(list_size)]
    print(user_list)
    print('-' * 20)

    sorted_list = merge_sort(user_list)
    print(sorted_list)
