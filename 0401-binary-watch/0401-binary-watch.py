class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for hours in range(12):
            for minutes in range(60):
                if (bin(hours) + bin(minutes)).count('1') == turnedOn:   # count total 1s in hour & min
                    # time = '%d:%02d' % (hour, minute)
                    # result.append(time)
                    answer.append(f"{hours}:{minutes:02d}")
        
        return answer

# Time Complexity: O(1)
# Space Complexity: O(1)
# by ar-sayeem [February 20, 2026]
