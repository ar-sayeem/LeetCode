# Prefix Sum | O(n) Time · O(1) Space | Beginner Friendly

# ⚖️ Prefix Sum Trick | O(N) Time · O(1) Space | Beginner Friendly

# Intuition
Imagine a seesaw. You want to find the exact spot to place your finger underneath so that the weight on the **left side** perfectly balances the weight on the **right side**. That balance point is the **pivot index**.

Now instead of doing this by trial and error (checking every single spot from scratch), you're smart about it — you already know the **total weight** of the entire seesaw. So at any position, the right side weight is just:
```
right = total - current - left
```

No need to re-sum the right side every time. That's the key insight.

# Approach

**Step 1 — Calculate the total sum once**

Before looping, get the sum of the entire array. This lets us calculate the right side instantly at any index without an extra loop.
```python
totalSum = sum(nums)
```

---

**Step 2 — Start walking through the array**

We track `leftSum` as we go — it starts at `0` because nothing is to the left of index `0` yet.
```python
leftSum = 0
```

**Why `enumerate` instead of `range(len(nums))`?**

Both work, but `enumerate` is cleaner. Instead of writing:
```python
for i in range(len(nums)):
    num = nums[i]   # extra line needed
```
We can write:
```python
for i, num in enumerate(nums):   # index and value together
```
It gives us both the index `i` and the value `num` at the same time — less code, easier to read.

---

**Step 3 — At each index, calculate the right sum**

At any index `i`, the right sum is everything except the current element and everything to the left:
```python
rightSum = totalSum - num - leftSum
```

Example with `nums = [1, 7, 3, 6, 5, 6]`, `totalSum = 28`:

| i | num | leftSum | rightSum = 28 - num - leftSum | Equal? |
|---|-----|---------|-------------------------------|--------|
| 0 | 1   | 0       | 27                            | ❌ |
| 1 | 7   | 1       | 20                            | ❌ |
| 2 | 3   | 8       | 17                            | ❌ |
| 3 | 6   | 11      | 11                            | ✅ pivot! |

---

**Step 4 — Check if left equals right**
```python
if leftSum == rightSum:
    return i
```

If they're equal, `i` is our pivot index — return it immediately.

---

**Step 5 — Accumulate left sum AFTER the check**

This is a tricky but important detail. We add `num` to `leftSum` **after** the check, not before. Why? Because at index `i`, the current element is **not** part of the left side — it's the pivot itself.
```python
leftSum += num
```

---

**Step 6 — No pivot found**

If we finish the loop without finding a balance point, return `-1`.
```python
return -1
```

---

**Comparison with other approaches:**

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Re-sum left and right at every index |
| Prefix Sum Array | O(n) | O(n) | Store all prefix sums in an array first |
| **This approach** | **O(n)** | **O(1)** | Calculate on the fly, no extra array needed |

This approach is the best — one pass after computing total sum, zero extra memory.

# Complexity
- Time complexity: $$O(n)$$ — we compute `sum()` once in O(n), then loop once through the array in O(n).

- Space complexity: $$O(1)$$ — only three variables used (`totalSum`, `leftSum`, `rightSum`), no extra array.

# Code
```python3 []
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0     # nothing to the left at the start

        for i, num in enumerate(nums):
            rightSum = totalSum - num - leftSum     # right = total - current - left
            if leftSum == rightSum:                 # balance found!
                return i
            leftSum += num                          # accumulate left sum AFTER check
        return -1                                   # no pivot found


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 17, 2026]
```

---

> 💡 **Friendly suggestion:** Please don't just copy-paste the code! Read through the explanation, make sure you truly understand *why* `leftSum` is updated **after** the check and *why* `rightSum = totalSum - num - leftSum` works. Then close the tab and try to write it from scratch on your own. That small struggle is where the real learning happens. You got this! 🙌
```