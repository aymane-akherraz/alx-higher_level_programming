def divisible_by_2(my_list=[]):
    res = []
    for i in my_list:
        if i % 2:
            res.append(0)
        else:
            res.append(1)
    return res
