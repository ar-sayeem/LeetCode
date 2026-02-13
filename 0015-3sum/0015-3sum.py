class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)

        if n < 3:
            return ans

        nums.sort()

        for i in range(n - 2):

            # Early stopping optimization
            if nums[i] > 0:
                break

            # Skip duplicate i values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans


# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding output)
# by ar-sayeem [February 13, 2026]
