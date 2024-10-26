class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min = nums[0]
        for i in nums:
            if abs(i) < abs(min):
                min = i
        if min < 0 and abs(min) in nums:
            return abs(min)
        else:
            return min