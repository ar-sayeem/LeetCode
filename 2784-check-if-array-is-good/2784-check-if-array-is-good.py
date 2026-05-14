from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        freq = Counter(nums)

        # numbers 1 to n-2 should appear once
        for i in range(1, n - 1):
            if freq[i] != 1:
                return False
        
        # n-1 should appear twice
        return freq[n - 1] == 2     # if not return False


# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [May 14, 2026]

        # nums.sort()  # sorted nums List
        # n = len(nums)

        # return nums == list(range(1, n)) + [n - 1]
        #             [1, 2, ..., n - 1] + [n - 1]
        # O(N log N) | O(N)