class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

# Time Complexity: O(n) <- Built-in methods are amortized linear
# Space Complexity: O(1)
# by ar-sayeem [January 27, 2026]


        if needle == "":
            return 0
        
        lh, ln = len(haystack), len(needle)

        for i in range(lh - ln + 1):
            match = True
            for j in range(ln):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
                
        return -1

# Time Complexity: O(n * m)
# Space Complexity: O(1)
# by ar-sayeem [January 27, 2026]

# """