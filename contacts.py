# Tries: Contacts
# Output Format:
# For each find partial operation, print the number of contact names starting with on a new line.

# Sample Input:
# 4
# add hack
# add hackerrank
# find hac
# find hak

# Sample Output:
# 2
# 0

# Explanation:
# We perform the following sequence of operations:

# 1. Add a contact named hack.
# 2. Add a contact named hackerrank.
# 3. Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
# 4. Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.

# n = int(input().strip())
# contactsList = []
# for a0 in range(n):
#     op, contact = input().strip().split(' ')
#     if op == 'add':
#         contactsList.append(contact)
#         return 0

#     count = 0
#     for i in contactsList:
#         if contact == i[:len(contact)-1]:
#             count += 1
#     print(count)

import bisect
n = int(input().strip())
contacts = []

for _ in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        bisect.insort_left(contacts, contact)

    if op == 'find':
        left = bisect.bisect_left(contacts, contact)
        print("left" ,left)
        prefix_next = contact[:-1] + chr(ord(contact[-1]) + 1)
        print("contact ", contact)
        print("contact[-1]", contact[-1])
        print("ord(contact[-1])", ord(contact[-1]))
        print("chr(ord(contact[-1]) + 1)", chr(ord(contact[-1]) + 1))
        print("contact[:-1] ", contact[:-1])
        print("prefix_next" , prefix_next)
        right = bisect.bisect_left(contacts, prefix_next)
        print("right", right)
        print(right - left)