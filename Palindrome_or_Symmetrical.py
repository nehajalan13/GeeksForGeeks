"""Author : Neha Jalan
 Date : 26 July 2023
WAP to check weather the given string is palindrome or Symmetrical"""

str = input("enter a string: ")
def palin(str):
    l = len(str)
    start = 0
    flag = 0
    end = l - 1
    mid = l//2
    while (start < mid):
        if str[start] == str[end]:
            start += 1
            end -= 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")


def symmetrical(str):
    flag = 0
    start = 0
    flag = 0
    l = len(str)

    if l % 2 == 0:
        mid = (l // 2)
    else:
        mid = (l // 2) + 1

    start2 = mid

    while (start < mid and start2 < l):
        if str[start] == str[start2]:
            start += 1
            start2 += 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")

palin(str)
symmetrical(str)
