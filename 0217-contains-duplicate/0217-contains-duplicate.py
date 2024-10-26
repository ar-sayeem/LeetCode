class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        if len(set(nums)) != len(nums):
                return True
        return False
            