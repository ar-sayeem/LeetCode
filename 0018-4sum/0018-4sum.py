class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                p, q = j + 1, n - 1
                while p < q:
                    s = nums[i] + nums[j] + nums[p] + nums[q]
                    if s < target:
                        p += 1
                    elif s > target:
                        q -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1

                        while p < q and nums[p] == nums[p - 1]:
                            p += 1
                        while p < q and nums[q] == nums[q + 1]:
                            q -= 1
        return ans


# Time Complexity: O(n³)
# Space Complexity: O(k) where k is the number of unique quadruplets
# by ar-sayeem [February 14, 2026]
