from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        # clockwise and anticlockwise pointers both start from startIndex
        c, a = startIndex, startIndex

        for dist in range(n):
            if words[c] == target:  # check clockwise
                return dist
            if words[a] == target:  # check anticlockwise
                return dist

            c = (c + 1) % n         # move right (next element)
            a = (a - 1 + n) % n     # move left (previous element)

        return -1  # no match found


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [April 15, 2026]
