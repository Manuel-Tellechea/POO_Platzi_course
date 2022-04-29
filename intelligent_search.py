import random


def smart_search(user_list, objective):
    match = False

    for element in user_list:
        if element == objective:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('De que tamaño será la lista? '))
    objetive = int(input('Que número quieres encontrar? '))

    user_list = [random.randint(0, 100) for i in range(list_size)]
    found = smart_search(user_list, objetive)
    print(user_list)
    print(f'El elemento {objetive} {"está" if found else "no está"} en la lista')
