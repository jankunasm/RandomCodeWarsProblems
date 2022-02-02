# numlist = [19, 5, 42, 2, 77]
# newlist = []
# newlist.append(min(numlist))
# print(min(numlist))
# print(newlist)

def sum_two_smallest_numbers(numbers):
    # newlist = []
    # newlist.append(min(numbers))
    sortedlist = sorted(numbers)
    return sortedlist[0] + sortedlist[1]
        
    # newlist.append(sortedlist[1])


print(sum_two_smallest_numbers([19, 5, 8, 3, 2, 20]))