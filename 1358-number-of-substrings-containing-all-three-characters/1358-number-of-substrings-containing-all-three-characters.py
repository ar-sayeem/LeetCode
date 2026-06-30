class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        left = 0
        count = [0, 0, 0]

        for right in range(n):
            count[ord(s[right]) - ord("a")] += 1
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                ans += n - right
                count[ord(s[left]) - ord("a")] -= 1
                left += 1
        return ans

# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [June 30, 2026]
