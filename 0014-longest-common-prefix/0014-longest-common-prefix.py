from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""

        for i in range(len(strs[0])):
            for s in strs[1:]:      # skip strs[0]
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

# Time Complexity: O(S)
# Space Complexity: O(1)
# by ar-sayeem [April 17, 2026]