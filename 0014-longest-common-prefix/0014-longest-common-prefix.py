from typing import List

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs[0])):    # loop through 1st word
            # flow -> 0, 1, 2, 3
            ch = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or word[i] != ch: # too short or diff word
                    return strs[0][:i]
        return strs[0]      # full word

# Time Complexity: O(S)
# Space Complexity: O(1)
# by ar-sayeem [Oct 20, 2026]