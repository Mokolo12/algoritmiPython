from random import randint
from timeit import Timer

def bubble_sort1(n):
    lst = [randint(-100, 100) for i in range(n)]

    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return


def bubble_sort2(n):
    lst = [randint(-100, 100) for i in range(n)]

    for i in range(len(lst)-1):
        is_move = False
        for j in range(len(lst)-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_move = True

        if not is_move:
            break

    return


n = 10
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_1', t.timeit(number=10))

n = 100
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_2', t.timeit(number=10))

n = 1000
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_3', t.timeit(number=10))

n = 10
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_1', t.timeit(number=10))

n = 100
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_2', t.timeit(number=10))

n = 1000
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_3', t.timeit(number=10))


"""
t1_1 0.00014439999358728528
t1_2 0.0074124999810010195
t1_3 0.8171751999761909
t2_1 0.00012550002429634333
t2_2 0.0066074999631382525
t2_3 0.8001458999933675485299
"""