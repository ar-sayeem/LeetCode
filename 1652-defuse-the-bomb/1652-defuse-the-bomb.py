from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        l = 0
        currSum = 0
        abs_k = abs(k)

        for r in range(n + abs_k):
            currSum += code[r % n]      # expand window to right

            if r - l + 1 > abs_k:       # bigger window, remove leftmost element from sum
                currSum -= code[l % n]
                l += 1

            if r - l + 1 == abs_k:      # window exactly right size
                if k > 0:
                    ans[(l - 1) % n] = currSum      # window's left neighbor owns this sum
                else:
                    ans[(r + 1) % n] = currSum      # window's right neighbor owns this sum

        return ans


# Time Complexity: O(N)
# Space Complexity: O(N)
# by ar-sayeem [April 16, 2026]
