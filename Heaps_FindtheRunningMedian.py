# Input Format:
# The first line contains a single integer, , denoting the number of integers in the data stream. 
# Each line  of the  subsequent lines contains an integer, , to be added to your list.

# Output Format:
# After each new integer is added to the list, print the list's updated median on a new line as a single double-precision number scaled to  decimal place (i.e.,  format).

# Sample Input:
# 6
# 12
# 4
# 5
# 3
# 8
# 7

# Sample Output:
# 12.0
# 8.0
# 5.0
# 4.5
# 5.0
# 6.0

##############################4/20/2017
#!/bin/python3

import bisect

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(a,a_t)
    index = len(a)//2
    if len(a)%2 == 0:
        num1 = a[index-1]
        num2 = a[index]
        print(float((num1+num2)/2))
    else:
        print(float(lists[index]))