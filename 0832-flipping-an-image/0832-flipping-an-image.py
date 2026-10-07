class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left = 0
            right = len(row) - 1
            while left <= right:
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image

# Time Complexity   : O(n²)
# Space Complexity  : O(1)
# by ar-sayeem [Oct 07, 2026]