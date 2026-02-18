class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # If bits alternate, n ^ (n >> 1) becomes all 1s
        x = n ^ (n >> 1)

        # A number with all 1s satisfies x & (x + 1) == 0
        return (x & (x + 1)) == 0


# Time Complexity: O(1)
# Space Complexity: O(1)
# by ar-sayeem [February 13, 2026]
