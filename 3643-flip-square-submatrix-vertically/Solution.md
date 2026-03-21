# Two Pointer Swap | O(k²) Time · O(k) Space | Beginner Friendly

# 🪞 Flip It Like a Pancake — Two Pointer In-Place Reversal

# Intuition
Imagine a stack of pancakes 🥞
You want to flip only the middle ones — not the whole stack.
You grab the top pancake and the bottom pancake of that middle section,
swap them, then move your hands inward and swap the next pair.
Keep going until your hands meet in the middle.

That's exactly what we do here:
- `top` and `bot` are your two hands
- The submatrix rows are the pancakes
- `y : y + k` makes sure we only touch the columns inside the square — nothing outside!

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is a Two Pointer?**
→ Two variables that start at opposite ends and move toward each other.
→ Super useful when you want to swap or compare things from both sides.
```
top = 0, bot = 4
swap(arr[top], arr[bot]) → top=1, bot=3 → top=2, bot=2 → STOP
```
> Think of it like zipping up a jacket — both sides come toward the middle.

**What is Python Slice Assignment?**
→ `grid[top][y : y+k]` grabs a chunk of a row (like tearing a strip of paper).
→ You can swap two strips in one line — Python reads the right side first, then assigns.
```python
a, b = b, a   # same idea, but for whole row slices!
```
> No temp variable needed — Python handles it cleanly.

**What does In-Place mean?**
→ We modify the original `grid` directly — we don't create a copy.
→ This is why Space is O(k) and not O(k²).

---

## Step 1 — Set up your two pointers
```python
top, bot = x, x + k - 1
```
💡 `top` starts at the first row of the submatrix (`x`).
`bot` starts at the last row (`x + k - 1`).

Example: `x=1, k=3` → `top=1, bot=3`
These are the two "hands" that will swap rows toward each other.

---

## Step 2 — Keep swapping while hands haven't crossed
```python
while top < bot:
```
⚠️ We stop when `top == bot` (middle row of odd-sized square — nothing to swap)
or when `top > bot` (fully done).

---

## Step 3 — Swap only the submatrix columns
```python
grid[top][y : y + k], grid[bot][y : y + k] = grid[bot][y : y + k], grid[top][y : y + k]
```
This is the heart of the solution!
- `y : y + k` → only touches columns INSIDE the square
- Columns outside the square are completely untouched ✅
- Python evaluates the right side first, so no data is lost during the swap

💡 Think of it as: only swap the pancake filling, not the plate around it.

---

## Step 4 — Move both pointers inward
```python
top += 1
bot -= 1
```
Move hands one step closer to the center.
Next iteration will swap the next inner pair of rows.

---

## Step 5 — Return the modified grid
```python
return grid
```
We edited `grid` in-place, so we just return it as-is.

---

## 🛣️ Visual: The Pancake Stack
```
grid (4×4), x=1, y=0, k=3

Original:
Row 0: [ 1,  2,  3,  4]   ← outside submatrix, untouched
Row 1: [ 5,  6,  7,  8]   ← top  (swap target)
Row 2: [ 9, 10, 11, 12]   ← middle (k=3 is odd → never touched)
Row 3: [13, 14, 15, 16]   ← bot  (swap target)

Columns in submatrix: y=0 to y+k=3  →  cols [0, 1, 2] only
Col 3 (value 8, 16) is OUTSIDE → stays unchanged ✅

Pass 1: swap row1[0:3] ↔ row3[0:3]
        [5, 6, 7] ↔ [13, 14, 15]
        top=2, bot=2 → STOP (top is not < bot)

After:
Row 0: [ 1,  2,  3,  4]
Row 1: [13, 14, 15,  8]   ← got row3's submatrix cols
Row 2: [ 9, 10, 11, 12]   ← untouched
Row 3: [ 5,  6,  7, 16]   ← got row1's submatrix cols
```

| Pass | top | bot | Swapped Cols | top after | bot after |
|------|-----|-----|--------------|-----------|-----------|
| 1    | 1   | 3   | [0:3]        | 2         | 2         |
| —    | 2   | 2   | STOP (top not < bot) | — | —      |

Answer = `[[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]` ✅

---

## 🔁 Approach Comparison Table

| Approach         | Time  | Space | Notes                              |
|------------------|-------|-------|------------------------------------|
| Brute Force Copy | O(k²) | O(k²) | Copy submatrix, reverse, paste back|
| Two Pointer ✅   | O(k²) | O(k)  | In-place swap, no extra matrix     |

# Complexity
- Time complexity: $$O(k^2)$$ — k/2 row swaps, each touching k columns
- Space complexity: $$O(k)$$ — only a temporary slice of length k per swap

# Code
```python3 []
from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # top = first row of the submatrix
        top, bot = x, x + k - 1
        # bot = last row of the submatrix

        while top < bot:
            # swap two rows within the submatrix columns only
            grid[top][y : y + k], grid[bot][y : y + k] = grid[bot][y : y + k], grid[top][y : y + k]
            top += 1
            bot -= 1

        return grid


# Time Complexity:  O(k²)
# Space Complexity: O(k)
# by ar-sayeem [March 21, 2026]

```
         ✨🌙 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🌙✨
        ╔═══════════════════════════════════════╗
        ║                                       ║
        ║          Eid ul-Fitr Mubarak          ║
        ║      ═══════════════════════════      ║
        ║                                       ║
        ║     May your heart be filled with     ║
        ║     joy, your home with laughter,     ║
        ║     and your life with endless        ║
        ║               blessings.              ║
        ║                                       ║
        ║    Celebrate love, kindness, and      ║
        ║        togetherness today!            ║
        ║                                       ║
        ║    — from a fellow coder who codes    ║
        ║         between Eid prayers           ║
        ║                                       ║
        ╚═══════════════════════════════════════╝

    🕌  Wishing you peace, happiness & prosperity! 🕌
     🌟  Eid Mubarak to you and your loved ones! 🌟
         ✨🌙 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 🌙✨
```
**💡 Before you leave:** please don't just copy this code. I know it's tempting, but close the tab, open a blank editor, and try writing it yourself. Struggle a little. Get it wrong a few times. That struggle is literally your brain learning. Come back and peek only if you're truly stuck. You'll feel way better when it finally clicks on your own. 🚀