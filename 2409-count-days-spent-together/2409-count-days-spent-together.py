class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def toDayNumber(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return sum(daysInMonth[:month - 1]) + day

        start = max(toDayNumber(arriveAlice), toDayNumber(arriveBob))
        end = min(toDayNumber(leaveAlice), toDayNumber(leaveBob))

        return max(0, end - start + 1)

# Time Complexity  : O(1)
# Space Complexity : O(1)
# by ar-sayeem [Oct 24, 2026]