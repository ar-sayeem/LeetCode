class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest = sorted(nums)[-k:]     # sort asc then slice LAST k numbers
        result = []

        for num in nums:        # looping in original order
            if num in largest:
                result.append(num)      # adding to result list
                largest.remove(num)     # removing from largest list
            if len(result) == k:
                break           # result list length = k, no further iteration need
        
        return result

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# by ar-sayeem [February 26, 26]