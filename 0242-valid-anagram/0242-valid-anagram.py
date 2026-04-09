from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)       # O(n) time, O(n) space
        # return sorted(s) == sorted(t)         # O(n log n) time, O(n) space

        if len(s) != len(t):
            return False

        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1    # update char frequency
        for c in t:
            if freq.get(c, 0) == 0:         # char not in s, or already used up
                return False
            freq[c] -= 1                    # spend one usage of this char
        return True


# Time Complexity:  O(n)
# Space Complexity: O(1)
# by ar-sayeem [April 09, 2026]