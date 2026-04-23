from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # securing boundary for mid +- 1
        start = 1
        end = len(arr) - 2

        while start <= end:
            mid = start + (end - start) // 2

            # peak at mid
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            # peak at right side
            elif arr[mid - 1] < arr[mid]:
                start = mid + 1
            # peak at left side
            else:
                end = mid - 1

        return -1

# Time Complexity   : O(log N)
# Space Complexity  : O(1)
# by ar-sayeem [April 23, 2026]