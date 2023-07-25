"""Author : Neha Jalan
 Date : 24 July 2023
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to
that of its index value ( Consider 1-based indexing ).
Note: There can be more than one element in the array which have the same value as its index.
You need to include every such element's index. Follows 1-based indexing of the array.
Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here."""

Arr = [15, 2, 45, 12, 7]
N = len(Arr)
def ValueEqualIndex(a,n):
    li = []
    for i in range(n):
        if a[i] == (i+1):
            li.append(i+1)

    return li

result = ValueEqualIndex(Arr,N)
print(result)
