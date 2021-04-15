#Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


def summation(num):
    newnum = 0
    while num != 0:
        newnum = newnum + num
        num -= 1
    return newnum

def summation1(num):
    return sum(range(num + 1))

print(summation1(3))