def solution(number):
    sums_list = []
    for i in range(number):
        if i % 3 == 0:
            sums_list.append(i)
        elif i % 5 == 0:
            sums_list.append(i)
    return sum(sums_list)

print(solution(4))
            
# number = 10
              
# for i in range(number):
#     if i % 3 == 0:
#         print(i)