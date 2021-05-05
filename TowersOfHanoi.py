'''
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves. Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc.

Input Format

A single integer N.

Constraints

1 <= N <= 16

Output Format

Refer the sample test cases for output format.

Sample Input 0

2
Sample Output 0

move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
Sample Input 1

3
Sample Output 1

move disk 1 from rod 1 to rod 3
move disk 2 from rod 1 to rod 2
move disk 1 from rod 3 to rod 2
move disk 3 from rod 1 to rod 3
move disk 1 from rod 2 to rod 1
move disk 2 from rod 2 to rod 3
move disk 1 from rod 1 to rod 3
7

'''

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("move disk 1 from rod",source,"to rod",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("move disk",n,"from rod",source,"to rod",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
n = int(input())
TowerOfHanoi(n,'1','3','2')
print("No.of steps: ".format((2**n)-1))
