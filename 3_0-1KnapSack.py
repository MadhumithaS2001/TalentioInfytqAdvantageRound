'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item. In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

Input Format

First line of input contains N. Second line of input contains W. Third line of input contains N integers, elements of val array. Fourth line of input contains N integers elements of wt array,

Constraints

1 ≤ N ≤ 1000 1 ≤ W ≤ 1000 1 ≤ wt[i] ≤ 1000 1 ≤ v[i] ≤ 1000

Output Format

Print the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

Sample Input 0

3
4
1 2 3
4 5 1
Sample Output 0

3
Sample Input 1

3
3
1 2 3
4 5 6
Sample Output 1

0

'''
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))
n=int(input())
W=int(input())
val =list(map(int,input().split()))
wt =list(map(int,input().split()))
print (knapSack(W, wt, val, n))
