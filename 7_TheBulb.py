'''
There is an infinite series of bulbs indexed from 1. And there are 40 switches indexed from 1 to 40. Switch with index x is connected to the bulbs with indexes that are multiple of x. i.e switch 2 is connected to bulb 4, 6, 8 ....

You can easily observe that some bulbs are connected to multiple switches and some are not connected to any switch.

Chotu is playing with these switches, he wants to know the Kth glowing bulb from the start if certain switches are in ON state. If any of the switch is ON, connected to any bulb then bulb starts glowing. But chotu has special fond of prime numbers so he only puts prime indexed switches ON.

Input Format

First line contains number of test cases (T). Each test case contains two lines- First line contains a string S of length 40 containing 0s and 1s that represents the state of bulbs. 1 is ON , 0 is OFF. Second line contains one integer k. Atleast One switch is in ON condition.

Constraints

1 <= T <= 500

S contains only 0s and 1s. 1s are only at prime positions.

1 <= k <= 10^15

1 is not prime

Output Format

Output one integer per test case representing kth glowing bulb.

Sample Input 0

1
0110000000000000000000000000000000000000
5
Sample Output 0

8
Sample Input 1

1
0010000000000000000000000000000000000000
5
Sample Output 1

15

'''
s=input()
    res=[]
    k=int(input())
    for i in range(len(s)):
        if (s[i]=='1'):
            for j in range(1,k+1):
                res.append(j*(i+1))
    res=sorted(list(set(res)))
    print(res[k-1])
