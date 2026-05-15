# Recursive DFS | O(n²) Time · O(n²) Space | Beginner Friendly

# 🐴 Tracing the Knight's Path with Recursion — Step by Step

# Intuition
Imagine a tour guide leading you through a museum, room by room, in a specific order.
Each room has a number on the wall (0, 1, 2, ...) telling you the order you visited it.
The tour guide always moves in an "L-shape" (like a chess knight).

Your job? Start at room 0 (top-left corner) and check:
- Are you always standing in the right room (matching the expected number)?
- Are all your moves valid knight moves?

In the code: `grid[r][c]` = the room you're in, `expVal` = the room you *should* be in.

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is Recursion?**
→ A function that calls *itself* to solve a smaller version of the same problem.
→ Like asking "did I reach room 5?" by first checking "did I reach room 4?" and so on.
```cpp
// Tiny example:
int countdown(int n) {
    if (n == 0) return 0;   // base case — stop here
    return countdown(n - 1); // recursive call
}
```
> Think of it as peeling an onion — each call removes one layer until you hit the core.

**What is a Knight's Move in chess?**
→ A knight moves in an "L" shape: 2 squares in one direction, then 1 square sideways (or vice versa).
→ From any position `(r, c)`, there are exactly 8 possible destinations.
```
    . X . X .
    X . . . X
    . . ♞ . .
    X . . . X
    . X . X .
```
> The knight is the only chess piece that can "jump over" other pieces — it's special!

---

## Step 1 — Validate the current cell before doing anything

```cpp
if (r < 0 || c < 0 || r >= n || c >= n || grid[r][c] != expVal) {
    return false;
}
```
💡 **Why this line?**
Before checking anything else, make sure:
- We haven't walked off the board (bounds check).
- The cell we're standing on has the value we *expected* (`expVal`).

If either condition fails, this path of the tour is invalid — return `false` immediately.

---

## Step 2 — Check if we've successfully visited every cell

```cpp
if (expVal == (n * n - 1)) {
    return true;
}
```
💡 **Why this line?**
An `n×n` board has `n*n` cells numbered `0` to `n*n - 1`.
If `expVal` has reached the last cell number and we're standing on it (checked in Step 1), the tour is complete!

---

## Step 3 — Try all 8 possible knight moves from here

```cpp
int ans1 = isValid(grid, r - 2, c + 1, n, expVal + 1);
int ans2 = isValid(grid, r - 1, c + 2, n, expVal + 1);
int ans3 = isValid(grid, r + 1, c + 2, n, expVal + 1);
int ans4 = isValid(grid, r + 2, c + 1, n, expVal + 1);
int ans5 = isValid(grid, r + 2, c - 1, n, expVal + 1);
int ans6 = isValid(grid, r + 1, c - 2, n, expVal + 1);
int ans7 = isValid(grid, r - 1, c - 2, n, expVal + 1);
int ans8 = isValid(grid, r - 2, c - 1, n, expVal + 1);
```
💡 **Why 8 calls?**
From any square, a knight has exactly 8 possible "L-shaped" jumps.
We try *every* one of them, asking: "Does the *next* expected cell (`expVal + 1`) sit in this direction?"

⚠️ **Important:** Most of these calls will return `false` — either the move goes off the board, or the destination doesn't hold `expVal + 1`. That's fine! We just need *one* of them to succeed.

---

## Step 4 — Return true if ANY one move continues the valid tour

```cpp
return ans1 || ans2 || ans3 || ans4 || ans5 || ans6 || ans7 || ans8;
```
💡 **Why `||` (OR)?**
We don't care *which* direction works — as long as one of the 8 paths leads to a valid next step, the tour so far is valid.

---

## Step 5 — Entry point: always start at (0, 0) expecting value 0

```cpp
bool checkValidGrid(vector<vector<int>>& grid) {
    return isValid(grid, 0, 0, grid.size(), 0);
}
```
💡 **Why start here?**
The problem says the knight *must* start at the top-left corner (row 0, column 0), and that cell must hold the value `0`. This call kicks off the whole recursive chain.

---

## 🛣️ Visual: The Museum Tour

Let's trace a small 3×3 example:
```
grid = [
  [0, 3, 6],
  [7, 2, 5],
  [4, 1, 8]
]
n = 3, so we need to visit cells 0 through 8.
```

| Step | (r, c) | grid[r][c] | expVal | Valid? | Next move tried |
|------|--------|------------|--------|--------|-----------------|
| 1    | (0, 0) | 0          | 0      | ✅     | look for 1      |
| 2    | (2, 1) | 1          | 1      | ✅     | look for 2      |
| 3    | (1, 1) | 2          | 2      | ✅     | look for 3      |
| 4    | (0, 1) | 3          | 3      | ✅     | look for 4      |
| 5    | (2, 0) | 4          | 4      | ✅     | look for 5      |
| 6    | (1, 2) | 5          | 5      | ✅     | look for 6      |
| 7    | (0, 2) | 6          | 6      | ✅     | look for 7      |
| 8    | (1, 0) | 7          | 7      | ✅     | look for 8      |
| 9    | (2, 2) | 8          | 8      | ✅     | expVal == n²-1  |

Answer = **true** ✅

Each recursive call peels off one more room from the tour, until the whole museum is visited!

---

## 🔁 Approach Comparison Table

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (regenerate all tours) | O(8^(n²)) | O(n²) | Try all possible knight paths — way too slow |
| Recursive DFS (this solution) | O(n²) | O(n²) | Each cell visited at most once via its `expVal` |

# Complexity
- Time complexity: $$O(n^2)$$ — we visit each of the `n×n` cells exactly once along the valid path
- Space complexity: $$O(n^2)$$ — the recursion stack can go as deep as `n×n` calls (one per cell)

# Code
```cpp []
#include <vector>
using namespace std;

class Solution {
public:
    bool isValid(vector<vector<int>>& grid, int r, int c, int n, int expVal) {
        if (r < 0 || c < 0 || r >= n || c >= n || grid[r][c] != expVal) {
            return false;
        }
        if (expVal == (n * n - 1)) {
            return true;
        }
        // 8 possible moves
        int ans1 = isValid(grid, r - 2, c + 1, n, expVal + 1);
        int ans2 = isValid(grid, r - 1, c + 2, n, expVal + 1);
        int ans3 = isValid(grid, r + 1, c + 2, n, expVal + 1);
        int ans4 = isValid(grid, r + 2, c + 1, n, expVal + 1);
        int ans5 = isValid(grid, r + 2, c - 1, n, expVal + 1);
        int ans6 = isValid(grid, r + 1, c - 2, n, expVal + 1);
        int ans7 = isValid(grid, r - 1, c - 2, n, expVal + 1);
        int ans8 = isValid(grid, r - 2, c - 1, n, expVal + 1);
        return ans1 || ans2 || ans3 || ans4 || ans5 || ans6 || ans7 || ans8;
    }
    bool checkValidGrid(vector<vector<int>>& grid) {
        return isValid(grid, 0, 0, grid.size(), 0);
    }
};
// Time Complexity: O(n²)
// Space Complexity: O(n²)
// by ar-sayeem [May 15, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀