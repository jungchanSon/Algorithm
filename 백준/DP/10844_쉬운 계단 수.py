import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]
    
for i in range(0, 10):
    dp[1][i] = 1
dp[1][0] = 0
if n == 1:
    print(9)
else :
    for i in range(2, n+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[n]) % 1000000000)

""" case 2
12  121 
23  232 234
34  343 345
45  456 457
56  
67
78
89
10  101 
21  212 210
32  321 323 
43
54
65
76
87
98

"""
                
""" 2개         3 3개                   4 3+ 1개
1개             
1   10 12       101 123 121             1010 1012 1232 1234 1210 1212
2   21 23       212 210. 232 234        2121 2123 2101 2321 2323 2345 2343
3   32 34       323 321 345 343         3234 3232 3210 3212 3456 3454 3432 3434
4   45 43       456 454 432 434         4567 4565 4543 4545 4321 4343 4323 4345
5   56 54       567 565 543 545         567 565 543 545 567 565 543 545         
6   65 67       654 656 676 678         567 565 543 545 567 565 543 545
7   76 78       765 767 789 787         567 565 543 545 567 565 543 545
8   87 89       876 878 898             567 565 543 545 8989 8987
9   98          989. 987                9898 9878 9876

"""