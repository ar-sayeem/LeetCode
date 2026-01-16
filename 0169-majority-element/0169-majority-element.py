class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0
        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)
        #     if n == result:
        #         count += 1
        #     else:
        #         count -= 1
        return result

# by ar-sayeem [January 16, 2026]