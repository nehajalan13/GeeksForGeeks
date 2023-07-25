"""Author : Neha Jalan
 Date : 24 July 2023
You are given an integer N. You need to convert all zeroes of N to 5.
Input:
N = 1004
Output: 1554"""
n = int(input("enter the number: "))
def convertFive(n):
    # Code here
    if n == 0:
        return 5
    else:
        temp =0
        while (n>0):
            d = n % 10
            if (d == 0):
                d = 5
            temp = (temp*10) + d
            n = n//10
    while (temp>0):
        d = temp % 10
        n = (n*10) + d
        temp = temp//10
    return n

result = convertFive(n)
print(result)
