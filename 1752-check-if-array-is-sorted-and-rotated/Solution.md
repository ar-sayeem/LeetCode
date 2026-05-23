# One-Pass Check | O(N) Time · O(1) Space | Beginner Friendly

# 🔄 Is It Rotated? Just Count the Drops!

# Intuition

Imagine you have a scoreboard that's supposed to go up — 1, 3, 5, 8, 10.
Now someone "rotated" it: 5, 8, 10, 1, 3.
It still goes up... but wraps around once.

The key insight: a sorted-then-rotated array can only "drop" (go from bigger to smaller) **exactly once**.
If it drops more than once, it's not a valid rotated sorted array.

We call that drop a `decend` (descent = going down).
Our job is just to count how many times the sequence goes downhill.

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is a "descent" in an array?**
→ A descent is when a number is *smaller* than the one before it.
→ Example: `[5, 8, 10, 1, 3]` — going from `10` to `1` is a descent. That's the only one here, so it's valid!

**Why do we also check `nums[0]` vs `nums[n-1]`?**
→ In a circular array, the last element "connects back" to the first.
→ Example: `[5, 8, 10, 1, 3]` — the last element `3` connects back to first element `5`. Since `5 > 3`, that's NOT a descent. Good.
→ But `[3, 1, 5, 8, 10]` — last element `10` connects back to `3`. Since `3 < 10`, that IS a descent wrapping around.

---

## Step 1 — Handle the edge case: tiny arrays

```python3
n = len(nums)
if n <= 1:
    return True
```

💡 An array with 0 or 1 element is always trivially sorted and rotated. Nothing to check!

---

## Step 2 — Set up the descent counter

```python3
decend = 0
```

We start with zero drops seen so far.
Every time we see the sequence go downhill, we'll add 1 to `decend`.

---

## Step 3 — Walk through the array and count descents

```python3
for i in range(1, n):
    if nums[i] < nums[i - 1]:
        decend += 1
    if decend > 1:
        return False
```

We compare each element to the one before it.
If `nums[i]` is *smaller* than `nums[i-1]`, the sequence just dropped — increment `decend`.

⚠️ We bail out early (`return False`) the moment we find a 2nd drop.
No need to keep checking — the array is already invalid.

---

## Step 4 — Check the "wrap-around" connection

```python3
if nums[0] < nums[n - 1]:
    decend += 1
```

This is the circular part. In a rotated array, the last element connects back to the first.
If `nums[0]` is *smaller* than `nums[n-1]`, that wrap-around is a descent too.

Example:
- `[3, 1, 5]` → last=`5`, first=`3` → `3 < 5` → descent! decend becomes 2 → ❌
- `[5, 1, 3]` → last=`3`, first=`5` → `5 > 3` → no descent here → ✅

---

## Step 5 — Final answer

```python3
return decend <= 1
```

If we saw 0 or 1 descent total (including the wrap-around), the array is a valid rotated sorted array. 🎉

---

## 🛣️ Visual: The Scoreboard Drop Counter

Let's trace through `nums = [5, 8, 10, 1, 3]`

```
Index:    0    1    2    3    4
Values:   5 → 8 → 10 → 1 → 3
                    ↓
                  DROP! (10 → 1)
```

| Step | Comparing       | Drop? | decend |
|------|-----------------|-------|--------|
| i=1  | 8 vs 5   (8>5)  | No    | 0      |
| i=2  | 10 vs 8  (10>8) | No    | 0      |
| i=3  | 1 vs 10  (1<10) | ✅ Yes | 1      |
| i=4  | 3 vs 1   (3>1)  | No    | 1      |

Now check wrap-around:
`nums[0]=5` vs `nums[4]=3` → `5 > 3` → NOT a descent → decend stays 1

Final check: `1 <= 1` → **True** ✅

---

Now let's trace an invalid one: `nums = [2, 1, 3, 4]`

| Step | Comparing     | Drop? | decend |
|------|---------------|-------|--------|
| i=1  | 1 vs 2 (1<2)  | ✅ Yes | 1      |
| i=2  | 3 vs 1 (3>1)  | No    | 1      |
| i=3  | 4 vs 3 (4>3)  | No    | 1      |

Check wrap-around:
`nums[0]=2` vs `nums[3]=4` → `2 < 4` → YES descent → decend becomes 2

Final check: `2 <= 1` → **False** ❌

---

## 🔁 Approach Comparison Table

| Approach       | Time   | Space | Notes                                      |
|----------------|--------|-------|--------------------------------------------|
| Brute Force    | O(N²)  | O(1)  | Try every rotation, check if sorted        |
| One-Pass Count | O(N)   | O(1)  | Just count descents — clean and fast ✅    |

# Complexity
- Time complexity: $$O(N)$$ — we visit each element exactly once in a single loop
- Space complexity: $$O(1)$$ — we only use one integer counter `decend`, nothing grows

# Code

```python3 []
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True

        decend = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                decend += 1
            if decend > 1:
                return False
        
        # 1st element > than last element, so it's a decend
        if nums[0] < nums[n - 1]:
            decend += 1

        return decend <= 1


# Time Complexity   : O(N)
# Space Complexity  : O(1)
# by ar-sayeem [May 23, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀