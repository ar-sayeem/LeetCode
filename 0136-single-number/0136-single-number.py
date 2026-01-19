class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0         # n ^ 0 = n
        for n in nums:
            ans ^= n    # ^ -> XOR
        return ans
        

# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [Jamuary 19, 2026]