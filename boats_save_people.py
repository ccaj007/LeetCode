'''
https://leetcode.com/problems/boats-to-save-people/

You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight
of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

'''
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people.sort()

        l = 0
        r = (len(people)) - 1
        while (l <= r):
            if ( l == r):
                boat += 1
                break

            if (people[l] + people[r] <= limit):
                l += 1

            boat += 1
            r -= 1
        return boat

b = Solution()
boats = b.numRescueBoats([7, 3, 2], 8)
print(boats)
