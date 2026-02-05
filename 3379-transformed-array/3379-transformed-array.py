class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # [0 if nums[i] == 0 else nums[(i + nums[i]) % n] for i in range(n)]
        result = []

        for i in range(N):
            if nums[i] == 0:
                result.append(0)  # no movement needed
            else:
                j = (i + nums[i]) % N
                result.append(nums[j])
                # i = current index
                # j = new index
                # nums[i] → number of steps to move
                # + → move left or right
                # % n → wrap around the array (circular behavior)
        return result


# Time Complexity: O(n)
# Space Complexity: O(n)
# by ar-sayeem [February 5, 2026]
