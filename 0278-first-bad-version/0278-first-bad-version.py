# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid =  left + (right - left) // 2
            if isBadVersion(mid):
                right = mid     # keep bad version
            else:
                left = mid + 1  # move next

        return right

# Time Complexity   : O(logN)
# Space Complexity  : O(1)
# by ar-sayeem [May 09, 2026]