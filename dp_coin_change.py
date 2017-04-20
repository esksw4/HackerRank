# Input Format:
# The first line contain two space-separated integers describing the respective values of  and . 
# The second line contains  space-separated integers describing the respective values of , where each integer denotes the dollar value of a distinct coin available in an infinite quantity.

# Constraints:
# The list of coins contains  distinct integers where each integer denotes the dollar value of a coin available in an infinite quantity.

# Output Format:
# Print a single integer denoting the number of ways we can make change for  dollars using an infinite supply of our  types of coins.

# Sample Input 0
# 4 3
# 1 2 3 

# Sample Output 0
# 4
# Explanation 0 
# {1,1,1,1}, {1,1,2}. {2,2}, {1,3}
# Thus, we print  on a new line.

# Sample Input 1
# 10 4
# 2 5 3 6
# Sample Output 1
# 5
# Explanation 1 
# {2,2,2,2,2} {2,2,3,3} {2,2,6} {2,3,5} {5,5}
# Thus, we print  on a new line.

# https://www.youtube.com/watch?v=jaNZ83Q3QGc
# Dynamic programming: the process of solving easier-to-solve sub-problems and building up the answers from that
# value stored in the array will be the total count of combinations for different amounts

#https://www.hackerrank.com/challenges/ctci-coin-change?h_r=next-challenge&h_v=zen
#####################################################4/20/2017
#!/bin/python3

import sys

def make_change(coins, n):
    comb = [0 for j in range(n+1)]
    comb[0] = 1
    while len(coins) != 0:
        currCoin = coins[0]
        if currCoin == 1:
            comb = [1 for j in range(n+1)]
            coins.pop(0)
        else: 
            #print(currCoin)
            for i in range(currCoin, n+1):
                #print('amount: ', i)
                #print('currCoin: ', currCoin)
                #print('comb: ', comb)
                if i >= currCoin:
                    comb[i] += comb[i-currCoin]
            coins.pop(0)
                    
    return comb[n]
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
