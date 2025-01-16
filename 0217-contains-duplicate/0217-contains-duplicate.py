class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()
        for num in nums:
            if num in h:
                return True
            h.add(num)
        return False