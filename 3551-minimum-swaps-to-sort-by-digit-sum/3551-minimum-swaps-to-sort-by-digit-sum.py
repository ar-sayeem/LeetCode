from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums, key = lambda x: (sum(int(d) for d in str(x)), x))
        # 18 -> (1 + 8, 18) -> (9, 18) | (7, 43) | (7, 34) | (7, 16)
        # sorted_nums = [16, 34, 43, 18]
        pos = {v: i for i, v in enumerate(sorted_nums)}
        # (0, 16), (1, 34), (2, 43), (3, 18)
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i]:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps

# Time Complexity  : O(nlogn)
# Space Complexity : O(n)
# by ar-sayeem [Oct 17, 2026]