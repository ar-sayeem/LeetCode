class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num: (num.bit_count(), num))


# Time Complexity: O(N log N)
# Space Complexity: O(N)
# by ar-sayeem [February 25, 2026]