"""
Subcarrier Conflict Detection using Sets
Author: Pujan Thapa Magar

Practicing Python sets using a real OFDMA resource allocation problem.
In 5G NR, subcarriers must be assigned without conflict between users.
"""

user1 = [10, 15, 20, 25, 30, 35, 40, 45]
user2 = [25, 30, 35, 40, 50, 55, 60, 65]

set1 = set(user1)
set2 = set(user2)

conflicts = set1 & set2          # & means common elements in both sets
total_occupied = set1 | set2     # | means all elements from both sets combined
only_user1 = set1 - set2         # - means remove set2 elements from set1
freed = set1 & set2              # same as conflicts — subcarriers used by both

print("conflicting subcarriers:", conflicts)
print("total occupied:", total_occupied)
print("only user1:", only_user1)
print("can be freed:", freed)