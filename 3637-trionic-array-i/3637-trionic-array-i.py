class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        N = len(nums)
        i = 1

        # first strictly increasing segment
        while i < N and nums[i-1] < nums[i]:
            i += 1
        p = i - 1       # peak of 1st segment (increasing)

        # strictly decreasing segment
        while i < N and nums[i-1] > nums[i]:
            i += 1
        q = i - 1       # bottom of 2nd segment (decreasing)

        # final strictly increasing segment
        while i < N and nums[i-1] < nums[i]:        # again increasing till end
            i += 1
        
        flag = i - 1    # last index reached

        return (p != 0) and (q != p) and (flag == N-1 and flag != q)
        # p != 0 ensures first increasing segment exists
        # q != p ensures a valid decreasing segment exists
        # flag == N-1 ensures traversal reaches the end
        # flag != q ensures final increasing segment exists


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [February 3, 2026]