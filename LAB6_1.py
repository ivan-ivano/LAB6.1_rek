import random


def generate_list(b, n=0):
    if n >= 22:
        return b
    else:
        b.append(random.randint(-40, 50))
        generate_list(b, n + 1)
    return b


def sum_of_elements(lst, i=0, sm=0):
    if i >= len(lst):
        return sm
    else:
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            sm += lst[i]
        return sum_of_elements(lst, i + 1, sm)


def count_elements(lst, i=0, cnt=0):
    if i >= len(lst):
        return cnt
    else:
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            cnt += 1
        return count_elements(lst, i + 1, cnt)


def replace_elements(lst, i=0):
    if i >= len(lst):
        return lst
    else:
        if not (lst[i] > 0 and lst[i] % 5 == 0):
            lst[i] = 0
        return replace_elements(lst, i + 1)


if __name__ == '__main__':
    a = generate_list([])
    print(a)
    print('Сума елементів, які підпадають під критерії:', sum_of_elements(a))
    print('Кількість обчислених елементів:', count_elements(a))
    print(replace_elements(a))
