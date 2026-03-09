class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        listIt = []
        setNums = set(nums)
        for i in range(1, n + 1):
            if i not in setNums:
                listIt.append(i)
        return listIt


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 09, 2026]