# Direct Row Construction | O(m·n) Time · O(m·n) Space | Beginner Friendly

# 🐸 One Frog, One Path: Build the Grid in a Single Line!

# Intuition
- Imagine a pond. `.` is a 🪷 lily pad (frog can stand) and `#` is a 🪨 rock (frog can't).
- The frog starts at the top-left and must reach the bottom-right, hopping only **right** or **down**.
- We want the frog to have **exactly one** route.
- Trick: if the lily pads form **one single chain** and everything else is rocks, there is only one way to go!
- Our chain: hop **all the way right** along the top row, then hop **all the way down** the last column. It looks like an upside-down L: "⅂".
- Mapping to code: top row → `'.' * n`, lower rows → `'#' * (n - 1) + '.'`.

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is string multiplication?**
→ In Python, `'.' * 4` repeats the string 4 times.
```python
'.' * 4      # "...."
'#' * 0      # ""  (empty!)
```
> "Multiply a letter, and you get a row of it." 🧱

**What is a list comprehension?**
→ A short way to build a list with a loop.
```python
[x for _ in range(3)]   # same as: repeat x three times
```
`_` just means "I don't need the counter, I only want to repeat."
> "A one-line loop that builds a list." 🔁

**What does `+` do for lists?**
→ It joins two lists into one.
```python
["a"] + ["b", "c"]   # ["a", "b", "c"]
```
> "Glue two trains together into one longer train." 🚂

## Step 1: Make the top row
```python
'.' * n
```
Row 0 is all lily pads, so the frog can hop right across the whole top.
For `n = 4` → `"...."`

💡 We wrap it in `[ ... ]` so it becomes a **list** holding one row.

## Step 2: Make one lower row
```python
'#' * (n - 1) + '.'
```
Every lower row has rocks everywhere **except the last cell**, so the frog can only drop down the right edge.
For `n = 4` → `"###."`

⚠️ Don't forget the brackets around `(n - 1)`! Writing `'#' * n - 1` crashes, because you can't subtract from a string.

## Step 3: Repeat the lower row `m - 1` times
```python
[... for _ in range(m - 1)]
```
We already made row 0, so we need `m - 1` more rows.
For `m = 3` → 2 lower rows → `["###.", "###."]`

⚠️ If `m = 1`, then `range(0)` runs **zero** times. That's fine, the answer is just the top row!

## Step 4: Glue and return
```python
return ['.' * n] + [ ... ]
```
Top row list + lower rows list = the final grid. 🎉

## 🛣️ Visual: The Frog and the Lily Pads

Example: `m = 3, n = 4`

```
 🐸 → → →        row 0:  . . . .
 #  #  #  ↓      row 1:  # # # .
 #  #  #  🏁     row 2:  # # # .
```

Building it step by step:

| Step | What we build | Value | Grid so far |
|---|---|---|---|
| 1 | top row `'.' * 4` | `"...."` | `["...."]` |
| 2 | lower row `'#' * 3 + '.'` | `"###."` | (ready to repeat) |
| 3 | repeat `m - 1 = 2` times | `["###.", "###."]` | – |
| 4 | glue the lists | – | `["....", "###.", "###."]` |

**Why only one path?** From any top-row cell, going down is blocked by `#`, except in the last column. So the frog must go across the top, then down the right side. No other choice exists!

Answer = `["....", "###.", "###."]` ✅

## 🔁 Approach Comparison Table

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force (try every grid, count paths) | $$O(2^{m \cdot n} \cdot m \cdot n)$$ | $$O(m \cdot n)$$ | Way too slow 🐢 |
| Walk a path with a loop (mark `.` cells) | $$O(m \cdot n)$$ | $$O(m \cdot n)$$ | Easy to understand 🚶 |
| **Direct row construction (this post)** | $$O(m \cdot n)$$ | $$O(m \cdot n)$$ | Shortest code, no loop bugs ⭐ |

# Complexity
- Time complexity: $$O(m \cdot n)$$. We create `m` rows, each with `n` characters.
- Space complexity: $$O(m \cdot n)$$. The grid we return has `m * n` characters.

# Code
```python3 []
from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        return ['.' * n] + ['#' * (n - 1) + '.' for _ in range(m - 1)]

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# by ar-sayeem [Oct 17, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀