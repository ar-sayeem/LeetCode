from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left, l_count = merge_sort(left)
            right, r_count = merge_sort(right)

            count = 0
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j

            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr += left[i:]
            sorted_arr += right[j:]

            return sorted_arr, l_count + r_count + count

        _, answer = merge_sort(nums)
        return answer


# Time Complexity: O(n log n)
# Space Complexity: O(n)
# by ar-sayeem [April 04, 2026]
