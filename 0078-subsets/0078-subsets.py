from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubSets = []
        ans = []
        n = len(nums)

        def getAllSubSets(i):
            if i == n:
                allSubSets.append(ans[:])   # copy of ans
                return
            
            # include
            ans.append(nums[i])
            getAllSubSets(i + 1)    # dive next

            # backtrack
            ans.pop()               # popping last element
            getAllSubSets(i + 1)    # dive next

        getAllSubSets(0)            # start from index 0
        return allSubSets


# Time Complexity   : O()
# Space Complexity  : O()
# by ar-sayeem [May 16, 2026]