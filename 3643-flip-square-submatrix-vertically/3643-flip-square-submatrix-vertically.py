from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # top = first row of the submatrix
        top, bot = x, x + k -1
        # bot = last row of the submatrix

        while top < bot:
            # swap two rows within the submatrix
            grid[top][y : y + k], grid[bot][y : y + k] = grid[bot][y : y + k], grid[top][y : y + k]
            top += 1
            bot -= 1

        return grid


# Time Complexity:  O(k²)
# Space Complexity: O(k)
# by ar-sayeem [March 21, 2026]


#       🌙✨ Eid ul-Fitr Mubarak ✨🌙
#
#      ╔══════════════════════════════╗
#      ║      🌙 Eid Mubarak 🌙      ║
#      ║   May your heart be filled   ║
#      ║   with joy, your home with   ║
#      ║   laughter, and your life    ║
#      ║   with endless blessings.    ║
#      ║                              ║
#      ║   Celebrate love, kindness,  ║
#      ║    and togetherness today!   ║
#      ╚══════════════════════════════╝
#
# 🕌 Wishing you peace, happiness, and prosperity!
# 🌟 Eid ul-Fitr Mubarak to you and your family! 🌟