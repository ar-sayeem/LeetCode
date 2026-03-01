class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0

        # iterate until the second last attack
        for i in range(len(timeSeries) - 1):
            # add only the non-overlapping poison time from the current attack
            total += min(timeSeries[i + 1] - timeSeries[i], duration)

        # last attack always contributes its full duration
        return total + duration


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 01, 2026]
