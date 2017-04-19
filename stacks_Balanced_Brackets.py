# Input Format:
# The first line contains a single integer, , denoting the number of strings. 
# Each line  of the  subsequent lines consists of a single string, , denoting a sequence of brackets.

# Constraints:
# , where  is the length of the sequence.
# Each character in the sequence will be a bracket (i.e., {, }, (, ), [, and ]).

# Output Format:
# For each string, print whether or not the string of brackets is balanced on a new line. If the brackets are balanced, print YES; otherwise, print NO.

# Sample Input:
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}

# Sample Output:
# YES
# NO
# YES

# Explanation:
# The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
# The string {[(])} is not balanced, because the brackets enclosed by the matched pairs [(] and (]) are not balanced. Thus, we print NO on a new line.
# The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.

# http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

def is_matched(expression):
    half = int(len(expression)/2)
    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    print(expression)
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")