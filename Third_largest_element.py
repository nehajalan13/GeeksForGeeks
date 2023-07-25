"""Author : Neha Jalan
 Date : 24 July 2023
Given an array of distinct elements. Find the third largest element in it.

Suppose you have A[] = {1, 2, 3, 4, 5, 6, 7}, its output will be 5 because it is
the 3 largest element in the array A.
N = 5
A[] = {2,4,1,3,5}
Output: 3"""

a = [1,2,3,5,6,7,8]
def thirdLargest(a):
    a.sort(reverse=True)
    return a[2]

result = thirdLargest(a)
print("Third largest element in the list is:", result)