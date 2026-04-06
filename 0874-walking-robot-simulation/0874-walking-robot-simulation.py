from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0     # origin (0, 0)
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]     # clockwise: N, E, S, W
        d = 0       # facing North
        ans = 0
        obstacle_set = set(map(tuple, obstacles))     # convert obstacle list to set for O(1) lookup

        for c in commands:
            if c == -1:
                d = (d + 1) % 4     # turn right, wraps around
            elif c == -2:
                d = (d - 1) % 4     # turn left, wraps around
            else:
                dx, dy = direct[d]  # move forward with d value
                for _ in range(c):
                    nx, ny = x + dx, y + dy     # calculate next position
                    if (nx, ny) in obstacle_set:   # obstacle found, stay at (x, y)
                        break
                    x, y = nx, ny       # no obstacle, commit the move
                    ans = max(ans, x*x + y*y)   # track max distance²
        
        return ans

# Time Complexity: O(N + M)   N = commands, M = obstacles
# Space Complexity: O(M)      obstacle set
# by ar-sayeem [April 06, 2026]