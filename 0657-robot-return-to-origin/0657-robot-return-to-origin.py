class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == "L":
                x -= 1
            elif move == "R":
                x += 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
        return x == 0 and y == 0


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [April 05, 2026]
