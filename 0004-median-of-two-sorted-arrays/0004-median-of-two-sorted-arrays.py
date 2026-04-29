from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = (m + n + 1) // 2 - mid1

            maxLeft1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            minRight1 = nums1[mid1] if mid1 < m else float("inf")

            maxLeft2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            minRight2 = nums2[mid2] if mid2 < n else float("inf")

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1


# Time Complexity:  O(log(MIN(M, N)))
# Space Complexity: O(1)
# by ar-sayeem [April 29, 2026]
