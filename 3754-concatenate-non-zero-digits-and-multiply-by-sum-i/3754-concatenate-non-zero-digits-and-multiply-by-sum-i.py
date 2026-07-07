class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0
        pow10 = 1

        while n > 0:
            d = n % 10
            total += d
            if d > 0:
                x += d * pow10
                pow10 *= 10
            n //= 10

        return x * total

# Time Complexity: O(logN)
# Space Complexity: O(1)
# by ar-sayeem [July 07, 2026]