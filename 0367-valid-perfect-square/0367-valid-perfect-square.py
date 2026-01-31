class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            m = l + ((r - l) // 2)  # run till half way, safer than "(l+m) // 2"
            sq = m**2

            if sq < num:
                l = m + 1
            elif sq > num:
                r = m - 1
            else:
                return True
        return False


# Time Complexity: O(logn)
# Space Complexity: O(1)
# by ar-sayeem [January 31, 2026]
