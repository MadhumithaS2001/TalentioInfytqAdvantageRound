'''
Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

Matrix [r+1] [c] Matrix [r+1] [c-1] Matrix [r+1] [c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input Format

First line of input contains 'N', the size of N*N matrix.Next N line contains N integers each which are the eements of matrix.

Constraints

1 ≤ N ≤ 100 1 ≤ Matrix[i][j] ≤ 1000

Output Format

Print the highest maximum path sum.

Sample Input 0

2
348 391
618 193
Sample Output 0

1009
Sample Input 1

2
2 2
2 2
Sample Output 1

4
'''

