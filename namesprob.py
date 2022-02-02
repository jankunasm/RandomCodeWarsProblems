def filter_list(l):
    newlist = []
    for i in l:
        if i == str:
            pass
        elif i == int:
            newlist.append(i)
    return newlist

print(filter_list([1,2,'aasf','1','123',123]))