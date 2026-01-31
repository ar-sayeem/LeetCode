class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)      # run till half way, safer than " (l+m) // 2 "
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res
    
# Time Complexity: O(logn)
# Space Complexity: O(1)
# by ar-sayeem [January 31, 2026]