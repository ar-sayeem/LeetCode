class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        # update top 3
        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

            # update bot 3
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, min1 * min2 * max1)

# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [July 26, 2026]
