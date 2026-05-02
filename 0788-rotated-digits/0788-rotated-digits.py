class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0

        for i in range(1, n + 1):
            s = str(i)

            # bad number 3/4/7
            if "3" in s or "4" in s or "7" in s:
                continue
            # good number 2/5/6/9
            if "2" in s or "5" in s or "6" in s or "9" in s:
                good += 1

            # skipped 0/1/8, produce same number

        return good


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 02, 2026]
