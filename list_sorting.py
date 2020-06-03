def sort_fn(value):
    """일의 자리를 반환하는 함수"""
    return value % 10


print(sort_fn(15))  # 5

list1 = [13, 26, 31, 49, 55]

sorted_list = sorted(list1, key=sort_fn, reverse=True)

print(sorted_list)  # [49, 26, 55, 13, 31]


def sort_fn2(value):
    """순서쌍의 두번째 원소를 반환하는 함수"""
    return value[1]


mylist = [(1, 2, 3), (2, 4, 5), (3, 1, 2), (6, 3, 2)]

sorted_list2 = sorted(mylist, key=sort_fn2, reverse=True)

print(sorted_list2)  # [(2, 4, 5), (6, 3, 2), (1, 2, 3), (3, 1, 2)]
