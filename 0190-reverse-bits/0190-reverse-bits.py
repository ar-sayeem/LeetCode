class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)

# Time Complexity: O(1)
# Space Complexity: O(1)
# by ar-sayeem [February 19, 2026]