class Solution:
    def mirrorDistance(self, n: int) -> int:
        # return abs(n - int(str(n)[::-1]))

        def reverse(x: int) -> int:
            y = 0
            while x > 0:
                y = y * 10 + x % 10     # append last digit of x to y
                x //= 10                # remove last digit from x
            return y

        return abs(n - reverse(n))


# Time Complexity: O(logN)
# Space Complexity: O(1)
# by ar-sayeem [April 18, 2026]
