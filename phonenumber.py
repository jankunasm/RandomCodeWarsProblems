def create_phone_number(n):
    # formattedstring = []
    for i in n:
        # formattedstring.append(i)
        return f'({i[0]} {i[1]} {i[2]}) {i[3]} {i[4]} {i[5]}-{i[6]} {i[7]} {i[8]} {i[9]})'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))