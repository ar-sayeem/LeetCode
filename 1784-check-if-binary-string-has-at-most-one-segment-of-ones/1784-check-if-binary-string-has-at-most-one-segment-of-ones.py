class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
        # checks if binary string contains only one continuous segment of '1's (no "01" pattern)


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [March 06, 2026]
