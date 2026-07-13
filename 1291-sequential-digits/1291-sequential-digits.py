class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        nums = []
        for length in range(2, 10):
            for i in range(10 - length):
                num = int(sample[i : i + length])
                if low <= num <= high:
                    nums.append(num)
        return nums

# Time Complexity   : O(1)
# Space Complexity  : O(1)
# by ar-sayeem [July 13, 2026]