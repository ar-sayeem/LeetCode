class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow-fast pointer
        slow, fast = 0, 0

        while True:
            slow = nums[slow]           # +1 step
            fast = nums[nums[fast]]     # +2 step
            if slow == fast:            # they met inside the cycle
                break
                
        slow = 0
        while True:
            slow = nums[slow]       # +1 step
            fast = nums[fast]       # +1 step
            if slow == fast:        # met at cycle entrance = duplicate
                break
        return slow


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 13, 2026]
