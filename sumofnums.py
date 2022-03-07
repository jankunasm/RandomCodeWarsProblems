# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def get_sum(a,b):
    list_to_sum = []
    if a > b:
        a == b and b == a
    for num in range(a,b + 1):
        if a == b:
            return a
        else:
            list_to_sum.append(num)
    return sum(list_to_sum)

print(get_sum(0,-1))

# rand_list = [0,-1]

# print(sum(rand_list))
