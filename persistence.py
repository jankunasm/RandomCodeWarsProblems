# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

# My solution.... have the right idea but need practice

def persistence(n):
    counter = 0
    temp = 1
    t = 1
    while n > 9:
        temp = str (n)
        for j in range(len(temp)):
            t *= int(temp[j])
        counter += 1
        n = t
        t = 1
    return counter

print(persistence(999))