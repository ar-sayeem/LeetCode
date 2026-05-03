class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        return goal in (s + s)      # abcdeabcde    (double string)
                                    #   ^^^^^       (goal)

# Time Complexity   : O(N)
# Space Complexity  : O(N)
# by ar-sayeem [May 03, 2026]