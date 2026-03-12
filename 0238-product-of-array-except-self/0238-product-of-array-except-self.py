class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n          # output array, prefilled with 1s

        left = 1
        for i in range(n):     # left to right
            ans[i] *= left     # store left product at current index
            left *= nums[i]    # update left product to include current element

        right = 1
        for i in range(n - 1, -1, -1):  # right to left-> range(start, stop, step)
            ans[i] *= right             # multiply existing left product by right product
            right *= nums[i]            # update right product to include current element

        return ans  # each ans[i] now holds left_product × right_product = product of all except self


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 12, 2026]