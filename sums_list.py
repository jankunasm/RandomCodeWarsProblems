def parts_sums(list):
    sums_list = []
    for num in list:
        print(sum(list))
        sums_list.append(sum)
        if num in list:
            list.pop(0)

ls = [0, 1, 3, 6, 10]
parts_sums(ls)