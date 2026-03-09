class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in nums:      # iterate over every value
            index = abs(i) - 1      # converting the value into a 0-based index
            if nums[index] > 0:
                nums[index] = -nums[index]      # mark existing as negative
            
        result = []

        for j in range(n):      # iterate over every index from 0 to n-1
            if nums[j] > 0:
                result.append(j + 1)

        return result

# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 09, 2026]




        # n = len(nums)
        # listIt = []
        # setNums = set(nums)
        # for i in range(1, n + 1):
        #     if i not in setNums:
        #         listIt.append(i)
        # return listIt


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 09, 2026]