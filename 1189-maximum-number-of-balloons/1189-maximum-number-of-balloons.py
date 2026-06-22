from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textCount = Counter(text)
        balloon = Counter("balloon")

        ans = len(text)
        for c in balloon:
            ans = min(ans, textCount[c] // balloon[c])
        return ans

# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [June 22, 2026]