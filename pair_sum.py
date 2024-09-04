def pair_sum(lst, num):
    new_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == num:
                pair = (lst[i], lst[j])
                new_lst.append(pair)
    return set(new_lst)

num = 8
lst = [1, 2, 3, 3, 4, 5, 5, 4, 6, 8, 9]
print(pair_sum(lst, num))