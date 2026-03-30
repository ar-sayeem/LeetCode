class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # index 0,2,4... from both → sort → check if same
        even_match = sorted(s1[0::2]) == sorted(s2[0::2])
        # grab index 1,3,5... from both → sort → check if same
        odd_match = sorted(s1[1::2]) == sorted(s2[1::2])

        return even_match and odd_match


# Time: O(n log n)
# Space: O(n)
# by ar-sayeem [March 30, 2026]
