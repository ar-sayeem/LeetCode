# Binary Search on Height | O(log²N) Time · O(log N) Space | Beginner Friendly

# 🌳 Count Complete Tree Nodes | Left=Right Height Trick | O(log²N) | Beginner Friendly

# Intuition
Imagine you're a building inspector counting apartments in a perfectly symmetric skyscraper.
If every floor is fully packed — you don't walk into every room. You just use a formula:
**floors = 3 → total rooms = 2³ - 1 = 7**. Done in one second!

But if the top floor is only partially filled, you split the building into a left wing and a right wing,
and check each wing the same way — again hoping one of them is perfectly packed.

- 🏗️ Building = the binary tree
- 📐 Left spine height = how deep the left wing goes
- 📐 Right spine height = how deep the right wing goes
- ✅ Left height == Right height → fully packed wing → use the formula
- 🔁 Otherwise → split and check each wing separately

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is a Complete Binary Tree?**
→ A tree where every level is fully filled EXCEPT possibly the last level,
  and the last level is filled from LEFT to RIGHT with no gaps.
→ Think of it like filling seats in a cinema row by row, always left first.

**What is a Perfect Binary Tree?**
→ A special complete tree where ALL levels are completely full — no missing seats anywhere.
→ A perfect tree of height h has exactly **2^h - 1** nodes.
```
h=1 → 1 node      (2¹ - 1 = 1)
h=2 → 3 nodes     (2² - 1 = 3)
h=3 → 7 nodes     (2³ - 1 = 7)
```

**What is Recursion?**
→ A function that calls itself on a smaller version of the same problem.
→ Like Russian dolls — open one, find a smaller one inside, repeat until empty.

**What is the Left/Right Spine?**
→ The left spine = keep going left from root until you fall off.
→ The right spine = keep going right from root until you fall off.
→ If both spines have the same height → the tree is perfect!

---

## Step 1 — Handle the empty tree

```python3
if not root:
    return 0
```
💡 If someone gives you an empty tree (root is None), there are 0 nodes. Always handle this first —
it's also what stops the recursion when we reach a null child later.

---

## Step 2 — Measure both spines

```python3
left_height = self.getLeftHeight(root)
right_height = self.getRightHeight(root)
```
We dive all the way down the left side and count levels → `left_height`.
We dive all the way down the right side and count levels → `right_height`.
Each of these walks takes O(log N) steps because the tree's height is log N.

```python3
def getLeftHeight(self, node):
    height = 0
    while node:       # keep going until we fall off the tree
        height += 1
        node = node.left
    return height

def getRightHeight(self, node):
    height = 0
    while node:       # same idea, but go right
        height += 1
        node = node.right
    return height
```
⚠️ We start counting from the root itself (height starts at 0, becomes 1 on first node).
So a single-node tree returns height = 1 from both functions.

---

## Step 3 — Check if it's a perfect tree

```python3
if left_height == right_height:     # perfect binary tree
    return (2 ** left_height) - 1
```
This is the **magic line**. If left spine = right spine in length → the tree is perfectly packed.
We don't visit a single extra node — we just use the formula and return instantly!

💡 Why does left == right mean perfect?
In a complete binary tree, the left side always fills first. So if right caught up to left in depth,
every single slot must be filled. No gaps possible.

```
left_height = right_height = 3
→ return 2³ - 1 = 7 nodes ✅ (never visited the 7 nodes individually!)
```

---

## Step 4 — Recurse when it's NOT perfect

```python3
return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```
If heights don't match → last level isn't full → we can't use the formula for the whole tree.
So we:
- Count the current root itself → the `1`
- Count the entire left subtree → `self.countNodes(root.left)`
- Count the entire right subtree → `self.countNodes(root.right)`

💡 The beautiful secret: every time we recurse, **one of the two subtrees will ALWAYS be a perfect tree**
and gets answered in O(1) with the formula. We never recurse on both sides wastefully.

---

## 🏗️ Visual: Building Inspector Analogy

```
Tree:
        1          ← root
       / \
      2   3
     / \ /
    4  5 6         ← last level (only 3 of 4 slots filled)
```

```
Call: countNodes(1)
  getLeftHeight(1)  → 1→2→4→None  = height 3
  getRightHeight(1) → 1→3→None    = height 2
  3 ≠ 2 → NOT perfect → recurse

  ┌─────────────────────────────────────────────┐
  │ countNodes(2)                               │
  │   getLeftHeight(2)  → 2→4→None = height 2   │
  │   getRightHeight(2) → 2→5→None = height 2   │
  │   2 == 2 → PERFECT! → 2² - 1 = 3            │
  │   (nodes 4 and 5 never individually visited)│
  └─────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────┐
  │ countNodes(3)                               │
  │   getLeftHeight(3)  → 3→6→None = height 2   │
  │   getRightHeight(3) → 3→None   = height 1   │
  │   2 ≠ 1 → NOT perfect → recurse             │
  │                                             │
  │   countNodes(6)                             │
  │     left=1, right=1 → PERFECT! → 1          │
  │                                             │
  │   countNodes(None) → 0                      │
  │                                             │
  │   = 1 + 1 + 0 = 2                           │
  └─────────────────────────────────────────────┘

Final = 1 + 3 + 2 = 6 ✅
```

```
Node visited individually: 1, 3, 6, None
Nodes answered by formula: subtree(2) = 3 nodes (saved 2 visits!)
```

## 🔁 Approach Comparison Table

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (visit all) | O(N) | O(log N) | Simple recursion, visits every single node |
| Height Trick (this solution) | O(log²N) | O(log N) | Exploits complete tree — skips perfect subtrees instantly |

# Complexity
- Time complexity: $$O(\log^2 N)$$ — we recurse O(log N) levels deep, and each level does O(log N) work to compute heights
- Space complexity: $$O(\log N)$$ — the recursion call stack is as deep as the tree's height

# Code
```python3 []
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.getLeftHeight(root)
        right_height = self.getRightHeight(root)

        if left_height == right_height:     # perfect binary tree
            return (2 ** left_height) - 1

        # not a perfect binary tree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # dive deep to left
    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # dive deep to right
    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height


# Time Complexity   : O(log²N)
# Space Complexity  : O(log N)
# by ar-sayeem [April 30, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀