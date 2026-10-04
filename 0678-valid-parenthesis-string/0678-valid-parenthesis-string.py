class Solution:
    def checkValidString(self, s: str) -> bool:
        min_waiting = 0
        max_waiting = 0

        for guest in s:
            if guest == "(":
                min_waiting += 1
                max_waiting += 1
            elif guest == ")":
                min_waiting -= 1
                max_waiting -= 1
            else:                   # '*'
                min_waiting -= 1
                max_waiting += 1

            if max_waiting < 0:     # even with all '*' as '(' we can't keep up, too much ')'
                return False

            if min_waiting < 0:
                min_waiting = 0

        return min_waiting == 0

# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [Oct 04, 2026]