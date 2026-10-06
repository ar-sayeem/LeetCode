class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        waiting = 0
        added = 0

        for i in s:
            if i == '(':
                waiting += 1
            else:                   # ')' arrives
                if waiting > 0:
                    waiting -= 1    # ')' paired with '('
                else:               # '(' needed for ')'
                    added += 1

        return waiting + added

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Oct 06, 2026]