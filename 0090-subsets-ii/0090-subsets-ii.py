from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        allSubSets = []
        ans = []
        n = len(nums)
        nums.sort()                             # group duplicates together

        def getAllSubSets(i):
            if i == n:
                allSubSets.append(ans[:])       # copy of ans
                return

            # include
            ans.append(nums[i])
            getAllSubSets(i + 1)                # dive next

            # backtrack
            ans.pop()                           # popping last element

            # skip all twins before the exclude-dive
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1                          # same element, go next

            getAllSubSets(i + 1)                # exclude-dive

        getAllSubSets(0)                        # start from index 0
        return allSubSets
        

# Time Complexity   : O(n * 2^n)
# Space Complexity  : O(n * 2^n)
# by ar-sayeem [May 17, 2026]