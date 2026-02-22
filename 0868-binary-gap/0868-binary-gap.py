class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_position = -1
        position = 0

        while n > 0:
            if n & 1:
                if last_position != -1:
                    max_gap = max(max_gap, position - last_position)
                last_position = position
            n >>= 1
            position += 1

        return max_gap


# Time Complexity: O(log n)
# Space Complexity: O(1)
# by ar-sayeem [February 22, 2026]
