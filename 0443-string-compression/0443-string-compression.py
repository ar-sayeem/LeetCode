
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, write = 0, 0
        n = len(chars)

        while i < n:
            count = 0
            char = chars[i]

            while i < n and chars[i] == char:
                i += 1
                count += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write

# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [April 14, 2026]