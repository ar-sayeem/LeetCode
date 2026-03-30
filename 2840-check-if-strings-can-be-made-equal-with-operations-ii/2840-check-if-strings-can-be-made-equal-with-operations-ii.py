from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # count even index characters from both → check if same
        even_match = Counter(s1[0::2]) == Counter(s2[0::2])
        # count odd index characters from both → check if same
        odd_match = Counter(s1[1::2]) == Counter(s2[1::2])

        return even_match and odd_match


# Time: O(n)
# Space: O(1)   → Counter has at most 26 keys
# by ar-sayeem [March 30, 2026]
