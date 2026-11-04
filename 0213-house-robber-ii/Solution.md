# Two Variables (Circle → Two Straight Lines) | O(n) Time · O(1) Space | Beginner Friendly

# 🏠 Round Table Thief: Turn the Circle into 2 Straight Streets 🔁

# Intuition
- Imagine friends sitting around a **round dinner table 🍽️**, each with a plate of candy (`nums[i]`).
- You can take candy from a plate, but **not** from the plates right next to it.
- Because the table is round, the **first friend and the last friend are neighbours too**!
- So you can never take from both the first and the last plate.
- That gives only **two choices**: skip the **last** plate, or skip the **first** plate. Each choice is just a normal straight line.
- We solve both lines with two sticky notes: `prev` (best loot from 2 houses back) and `curr` (best loot up to the last house). We keep the bigger answer.

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is a circle of houses?**
→ A street where the last house touches the first house.
→ `[2,3,2]` on a circle: the two `2`s are neighbours, so you can't rob both!
> "On a round table, everyone has two neighbours. Nobody sits at the end." 🍽️

**What are `prev` and `curr`?**
→ Two sticky notes that remember the best loot so far.
```python
prev = 0   # best loot from two houses back
curr = 0   # best loot up to the previous house
```
> "You don't need the whole diary, just the last two pages." 📒

**What is tuple assignment?**
→ Python calculates the **right side first**, then fills the left side.
```python
a, b = 1, 2
a, b = b, a + b   # a = 2, b = 3
```
> "Pick up both new values first, then put the old ones down." 🤲

**What is `range(start, end + 1)`?**
→ `range` stops **before** the last number, so we add `+ 1` to include `end`.
```python
list(range(1, 4))      # [1, 2, 3]   ← 4 is missing!
list(range(1, 4 + 1))  # [1, 2, 3, 4]
```

**What is a function inside a function?**
→ `rob_line` lives inside `rob`, and it can use `nums` directly. It's a small helper that solves one straight street.

## Step 1: Count the houses and handle one house
```python
n = len(nums)
if n == 1:
    return nums[0]
```
- `n` is the number of houses.
- With **one** house there are no neighbours, so we just rob it.
- ⚠️ **Common mistake:** forgetting this! With `n == 1`, the two lines become `rob_line(0, -1)` and `rob_line(1, 0)`. Both are empty and return `0`, which is wrong.

## Step 2: Make a helper for a straight street
```python
def rob_line(start, end):
```
- It solves a normal (non-circle) street from house `start` to house `end`.
- 💡 We use indices instead of slicing (`nums[1:]`) because slicing makes a copy and costs extra memory.

## Step 3: Set up the sticky notes
```python
prev = 0
curr = 0
```
- At the start no houses are visited, so the loot is `0`.

## Step 4: Walk the street, skip or rob
```python
for i in range(start, end + 1):
    prev, curr = curr, max(curr, prev + nums[i])
return curr
```
- At house `i` we have two choices:
  - **Skip it:** loot stays `curr`.
  - **Rob it:** `prev + nums[i]`. We use `prev` (not `curr`) because the last house is our neighbour!
- We keep the bigger one, then slide the notes forward.
- ⚠️ **Warning:** don't write `prev = curr` and then `curr = max(...)` on two separate lines. The old `curr` is lost! Tuple assignment solves this. 🎯

## Step 5: Break the circle into two streets
```python
return max(rob_line(0, n - 2), rob_line(1, n - 1))
```
- `rob_line(0, n - 2)` → **skip the last house**.
- `rob_line(1, n - 1)` → **skip the first house**.
- The bigger one wins. 💡 This is the whole trick of the problem!

## 🛣️ Visual: The Round Table 🍽️

`nums = [1, 2, 3, 1]`

```
      H0(1) --- H1(2)
        |         |
      H3(1) --- H2(3)
```

The first and last houses (H0 and H3) are neighbours, so we split into two lines:

```
Street 1 (skip last):   [1, 2, 3]  1 ── 2 ── 3     (H3 ignored)
Street 2 (skip first):  [2, 3, 1]  2 ── 3 ── 1     (H0 ignored)
```

**Street 1: `rob_line(0, 2)`**

| i | money | prev before | curr before | max(curr, prev + money) | prev after | curr after |
|---|---|---|---|---|---|---|
| start | | | | | 0 | 0 |
| 0 | 1 | 0 | 0 | max(0, 0+1) = 1 | 0 | 1 |
| 1 | 2 | 0 | 1 | max(1, 0+2) = 2 | 1 | 2 |
| 2 | 3 | 1 | 2 | max(2, 1+3) = 4 | 2 | 4 |

→ Street 1 gives **4**

**Street 2: `rob_line(1, 3)`**

| i | money | prev before | curr before | max(curr, prev + money) | prev after | curr after |
|---|---|---|---|---|---|---|
| start | | | | | 0 | 0 |
| 1 | 2 | 0 | 0 | max(0, 0+2) = 2 | 0 | 2 |
| 2 | 3 | 0 | 2 | max(2, 0+3) = 3 | 2 | 3 |
| 3 | 1 | 2 | 3 | max(3, 2+1) = 3 | 3 | 3 |

→ Street 2 gives **3**

max(4, 3) → **Answer = 4** ✅ (rob H0 and H2: 1 + 3)

## 🔁 Approach Comparison Table

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force (recursion, take or skip) | $$O(2^n)$$ | $$O(n)$$ | Easy idea, but far too slow for big inputs |
| DP Table (`dp` array, run on 2 streets) | $$O(n)$$ | $$O(n)$$ | Remembers answers in a notebook |
| **Two Variables (this post)** ⭐ | $$O(n)$$ | $$O(1)$$ | Only the last two answers matter |

# Complexity
- Time complexity: $$O(n)$$ — we walk the houses twice (two streets), which is about $$2n$$ steps, still linear.
- Space complexity: $$O(1)$$ — only `prev`, `curr`, and a few counters, no extra list.

# Code
```python3 []
from typing import List

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:      # one house = rob it
            return nums[0]
        
        def rob_line(start, end):
            prev = 0
            curr = 0

            for i in range(start, end + 1):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr
        
        return max(rob_line(0, n - 2), rob_line(1, n - 1))

# Time Complexity  : O(n)
# Space Complexity : O(1)
# by ar-sayeem [Nov 04, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀