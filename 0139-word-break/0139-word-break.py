from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        maxLen = max(len(w) for w in words)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(max(0, i - maxLen), i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]

# Time Complexity  : O(n * L^2)
# Space Complexity : O(n + m)
# by ar-sayeem [Oct 18, 2026]