import random


def binary_search(user_list, start, end, objective):
    print(f'buscando {objective} entre {user_list[start]} y {user_list[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if user_list[middle] == objective:
        return True
    elif user_list[middle] < objective:
        return binary_search(user_list, middle + 1, end, objective)
    else:
        return binary_search(user_list, start, middle - 1, objective)


if __name__ == '__main__':
    list_size = int(input('De que tamaño es la lista? '))
    objective = int(input('Que número quieres encontrar? '))

    user_list = sorted([random.randint(0, 100) for i in range(list_size)])
    founded = binary_search(user_list, 0, len(user_list), objective)

    print(user_list)
    print(f'El elemento {objective} {"esta" if founded else "no esta"} en la lista')
