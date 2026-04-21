from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have, required = 0, len(need)
        window = {}

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return "" if min_len == float("inf") else s[min_start : min_start + min_len]

# Time Complexity   : O(N)
# Space Complexity  : O(K)
# by ar-sayeem [April 21, 2026]