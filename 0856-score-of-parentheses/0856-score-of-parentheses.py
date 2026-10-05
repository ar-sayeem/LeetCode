class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == "(":
                    score += 2**depth  # nested '( () )'

        return score

# Time Complexity  : O(N)
# Space Complexity : O(1)
# by ar-sayeem [Oct 05, 2026]