class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        full_nines = sum // 9
        leftover = sum % 9
        result = "9" * full_nines
        if leftover > 0:
            result += str(leftover)
        result += "0" * (num - len(result))

        return result

# Time Complexity: O(num)
# Space Complexity: O(1)
# by ar-sayeem [Oct 14, 2026]