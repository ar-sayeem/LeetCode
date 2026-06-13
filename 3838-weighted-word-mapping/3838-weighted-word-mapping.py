from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            s = 0

            for c in word:
                s += weights[ord(c) - ord("a")]
            ans.append(chr(ord("z") - s % 26))

        return "".join(ans)


# Time Complexity: O(N)  — N = total characters across all words
# Space Complexity: O(1)  — auxiliary space only, not counting output
# by ar-sayeem [June 13, 2026]