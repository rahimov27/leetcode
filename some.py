def move_zeros(lst):
    clean_list = []
    without_zero = []
    second_list = list(lst)
    for e in second_list:
        if e == 0:
            second_list.remove(0)
            without_zero.append(e)
    print(without_zero)
    for i in lst:
        if i == 0:
            clean_list.append(i)
    print(clean_list)


move_zeros(lst=[1, 2, 3, 0, 0, 0, 4, 5, 6])
