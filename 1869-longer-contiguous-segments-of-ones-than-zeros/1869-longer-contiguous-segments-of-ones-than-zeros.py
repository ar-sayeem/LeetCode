class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOne = maxZero = 0
        one = zero = 0

        for ch in s:
            if ch == "1":
                one += 1
                zero = 0    # reset zero counting
            else:
                zero += 1
                one = 0     # reset one counting

            maxOne = max(maxOne, one)
            maxZero = max(maxZero, zero)

        return maxOne > maxZero


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 07, 2026]
