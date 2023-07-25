"""Author : Neha Jalan
 Date : 24 July 2023
Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero.

Note: Return 1, if there is at least one triplet following the condition else return 0.
Input: n = 5, arr[] = {0, -1, 2, -3, 1}
Output: 1
Explanation: 0, -1 and 1 forms a triplet
with sum equal to 0.
"""

a = [-1,0,1,2,-2]
n = 5
def findTriplets(arr, n):
    # code here
    counter = 0
    arr.sort()
    for i in range(n - 2):
        if (arr[i] + arr[i + 1] + arr[i + 2]) == 0:
            counter += 1
    print(counter)

findTriplets(a,n)