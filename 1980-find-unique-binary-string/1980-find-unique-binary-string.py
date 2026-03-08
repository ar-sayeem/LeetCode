class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor Diagonal approach
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [March 08, 2026]
