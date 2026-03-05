class Solution:
    def minOperations(self, s: str) -> int:
        count = 0  # oparations if s starts with 0

        for i in range(len(s)):
            if i % 2:  # expecting odd
                count += 1 if s[i] == "0" else 0
            else:  # expecting even
                count += 1 if s[i] == "1" else 0

        # min flips between starting with '0' and starting with '1'
        return min(count, len(s) - count)


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [March 05, 2026]
