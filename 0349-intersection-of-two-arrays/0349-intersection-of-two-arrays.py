class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Time Complexity   : O(N + M)
# Space Complexity  : O(N + M)
# by ar-sayeem [July 02, 2026]
