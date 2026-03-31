class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS2T = {}     # maps char of s → char of t
        mapT2S = {}     # maps char of t → char of s

        for cs, ct in zip(s, t):    # cs = char s, ct = char t
            if ((cs in mapS2T and mapS2T[cs] != ct) or
                (ct in mapT2S and mapT2S[ct] != cs)):
                return False

            mapS2T[cs] = ct
            mapT2S[ct] = cs

        return True


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [March 31, 2026]
