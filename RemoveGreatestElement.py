"""Author : Neha Jalan
 Date : 24 July 2023
 Given an array of N distinct elements, the task is to find all elements in array
 except two greatest elements in sorted order.
 Input :
 a[] = {2, 8, 7, 1, 5}
 Output :
 1 2 5 """

a = [1,2,3,4,5]
n = len(a)
def findElements(a,n):
    a.sort()
    return a[:n-2]

result = findElements(a,n)
print(result)