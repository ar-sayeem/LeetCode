# Floyd's Cycle Detection | O(n) time | O(1) space | Beginner Friendly

# 🐢🐇 Finding the Duplicate — Floyd's Cycle Detection (Tortoise & Hare)

# Intuition
Imagine you have an array like `[1, 3, 4, 2, 2]`. The values are all between `1` and `n`, which means every value can be used as an **index** to jump to the next position — just like a linked list where each node points to the next.

Because there is a duplicate, two different indices will point to the **same next index**, creating a **loop (cycle)**. Our job is simply to find where that loop begins — because that's the duplicate number.

# Approach
We use **Floyd's Cycle Detection Algorithm**, also known as the **Tortoise and Hare** algorithm. Here's how it works in plain English:

---

**Step 1 — Treat the array like a linked list**

Instead of thinking about the array normally, think of it as a chain of jumps:
- You start at index `0`
- The value at index `0` tells you where to jump next
- The value at that index tells you where to jump after that
- ...and so on

Example with `[1, 3, 4, 2, 2]`:
```
index: 0 → 1 → 3 → 2 → 4 → 2 → 4 → ... (stuck in a loop!)
value: 1    3    2    4    2
```
See how it gets stuck looping between index `2` and `4`? That loop exists **because** `2` is the duplicate.

---

**Phase 1 — Find the meeting point (detect the cycle)**

We send two "runners" through the chain:
- 🐢 **Slow** moves **1 step** at a time: `slow = nums[slow]`
- 🐇 **Fast** moves **2 steps** at a time: `fast = nums[nums[fast]]`

Since fast is moving twice as fast, it will eventually **lap** slow inside the cycle and they will meet at the same index. We stop as soon as they meet.
```python
slow, fast = 0, 0
while True:
    slow = nums[slow]           # 1 step
    fast = nums[nums[fast]]     # 2 steps
    if slow == fast:            # they met inside the cycle
        break
```

> ⚠️ Both start at `0` and we use `while True` so they move **before** being compared — otherwise they'd be equal at the start and the loop would never run.

---

**Phase 2 — Find the cycle entrance (= the duplicate)**

The meeting point from Phase 1 is somewhere **inside** the cycle, not necessarily at the start of it. To find the exact entrance:

- Reset 🐢 slow back to index `0`
- Keep 🐇 fast at the meeting point
- Now move **both one step at a time**

Due to the math of how cycles work, they are guaranteed to meet **exactly at the cycle entrance** — which is the duplicate number.
```python
slow = 0
while True:
    slow = nums[slow]       # 1 step
    fast = nums[fast]       # 1 step
    if slow == fast:        # met at the duplicate!
        break
return slow
```

---

**Why is this better than other approaches?**

| Approach | Time | Space | Modifies array? |
|---|---|---|---|
| Sorting | O(n log n) | O(1) | ✅ Yes |
| Hash Set | O(n) | O(n) | No |
| **Floyd's (this)** | **O(n)** | **O(1)** | **No** |

Floyd's is the only approach that satisfies all three constraints of the problem: no sorting, no extra space, no modifying the input.

# Complexity
- Time complexity: $$O(n)$$ — both phases traverse the array at most once.

- Space complexity: $$O(1)$$ — only two pointers are used, no extra array or hash set.

# Code
```python3 []
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow-fast pointer
        slow, fast = 0, 0

        while True:
            slow = nums[slow]           # +1 step
            fast = nums[nums[fast]]     # +2 step
            if slow == fast:            # they met inside the cycle
                break
                
        slow = 0
        while True:
            slow = nums[slow]       # +1 step
            fast = nums[fast]       # +1 step
            if slow == fast:        # met at cycle entrance = duplicate
                break
        return slow


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 13, 2026]
```