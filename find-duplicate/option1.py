# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    numbers = set()
    for i in range(len(input)):
        if input[i] in numbers:
            return input[i]
        numbers.add(input[i])
# The time complexity of the above solution is O(n), while the space 
# complexity is also O(n).
# Some test cases are below
print(findDuplicate([1,3,4,2,2]))
print(findDuplicate([3,1,3,4,2]))
print(findDuplicate([3,3,3,3,3]))

def findDuplicate2(input: List[int]) -> int:
    slow = 0
    fast = 0 
    while True: 
        slow = input[slow]
        fast = input[input[fast]]
        if slow == fast:
            break
    slow2 = 0
    while True:
        slow = input[slow]
        slow2 = input[slow2]
        if slow == slow2:
            return slow2

# The time complexity of the above solution is O(n), while the space 
# complexity is improved to O(1) since no hash set is used. 
# Test cases below
print(findDuplicate2([1,3,4,2,2]))
print(findDuplicate2([3,1,3,4,2]))
print(findDuplicate2([3,3,3,3,3]))

#Credit to Leetcode for the test cases used in both solutions. 
