'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input Format

First line of input contains integer n. Next line of input contains n space separated integers which are the elements of the array.

Constraints

1 ≤ N ≤ 106 -10^7 ≤ A[i] <= 10^7

Output Format

Print the sum of subarray with maximum sum.

Sample Input 0

5
1 2 3 -2 5
Sample Output 0

9
Sample Input 1

4
-1 -2 -3 -4
Sample Output 1

-1
'''

x=int(input())
a=list(map(int,input().split()))
s=0
l=[]
for i in a:
    l.append(int(i))
for i in range(x):
    s=a[i]+s
    l.append(s)
print(max(l))
