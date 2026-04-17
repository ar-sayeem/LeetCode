# Vertical Scan | O(N) Time · O(1) Space | Beginner Friendly

# 🏁 Column-by-Column: The Vertical Scan Trick for Longest Common Prefix

# Intuition
Imagine you and your friends are all holding signs at a race finish line.
Each sign has a word on it. You want to find the longest "shared start" across ALL signs.

Instead of reading each sign fully, you look at **column by column** — first letter of every sign,
then the second letter of every sign, and so on.

The moment ANY sign has a different letter (or runs out of letters), you stop.
Whatever you've collected so far? That's your answer.

- `strs[0]` → the first sign (your "reference" sign)
- `i` → which column (letter position) you're currently checking
- `res` → the prefix you've collected so far
- `s` → each other sign you're comparing against

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is vertical scanning?**
→ Instead of comparing strings side-by-side (left to right, one full string at a time),
you go **column by column** — checking the same index `i` across ALL strings at once.
```
strs = ["flower", "flow", "flight"]
Index 0 → f, f, f ✅
Index 1 → l, l, l ✅
Index 2 → o, o, i ❌ → STOP
```

**What is `strs[1:]`?**
→ This is Python's list slicing. It gives you every element except the first one.
```python
strs = ["flower", "flow", "flight"]
strs[1:]  →  ["flow", "flight"]
```
We already use `strs[0]` as our reference, so we only need to check the rest.

---

## Step 1 — Handle the empty list edge case
```python
if not strs:
    return ""
```
💡 If someone gives us an empty list `[]`, there's nothing to compare.
We return `""` immediately. Always handle edge cases first — it keeps the rest of your code clean!

---

## Step 2 — Set up our result collector
```python
res = ""
```
This is our "notebook" where we write down each matching letter as we find it.
It starts empty and grows one character at a time.

---

## Step 3 — Loop through each column (letter position)
```python
for i in range(len(strs[0])):
```
We use `strs[0]` (the first string) as our **ruler**.
Why? Because the common prefix can never be *longer* than the first string,
so we only need to check as many columns as `strs[0]` has letters.

---

## Step 4 — Compare every other string at column `i`
```python
for s in strs[1:]:
    if i == len(s) or s[i] != strs[0][i]:
        return res
```
For each other string `s`, we check two things:

- `i == len(s)` → Has string `s` run out of letters? (It's shorter than our reference!)
- `s[i] != strs[0][i]` → Is the letter at column `i` different from our reference?

If **either** is true for **any** string, we've found the end of the common prefix.
We immediately return whatever `res` has collected so far.

⚠️ We check `i == len(s)` **before** `s[i]` on purpose — if `s` has run out of characters,
trying `s[i]` would crash with an IndexError!

---

## Step 5 — Add the matching letter to our result
```python
res += strs[0][i]
```
If ALL strings passed the check at column `i`, that letter is part of the common prefix.
We add `strs[0][i]` (the letter from our reference string) to `res`.

---

## Step 6 — Return the full prefix if we never got stopped
```python
return res
```
If we made it through every column of `strs[0]` without returning early,
it means `strs[0]` itself IS the common prefix (all others start with it).
We return the fully built `res`.

---

## 🛣️ Visual: The Sign-Checking Race

```
strs = ["flower", "flow", "flight"]
Reference string: strs[0] = "flower"
```

| Column `i` | `strs[0][i]` | Checking `"flow"` | Checking `"flight"` | Match? | `res` after step |
|:-----------:|:------------:|:-----------------:|:-------------------:|:------:|:----------------:|
| 0           | `'f'`        | `'f'` ✅          | `'f'` ✅             | Yes    | `"f"`            |
| 1           | `'l'`        | `'l'` ✅          | `'l'` ✅             | Yes    | `"fl"`           |
| 2           | `'o'`        | `'o'` ✅          | `'i'` ❌             | No     | return `"fl"`    |

Answer = `"fl"` ✅

```
Notebook growth:
After i=0 → res = "f"
After i=1 → res = "fl"
At i=2    → "flight"[2] is 'i', not 'o' → STOP → return "fl"
```

---

## 🔁 Approach Comparison Table

| Approach         | Time   | Space  | Notes                                              |
|------------------|--------|--------|----------------------------------------------------|
| Brute Force (compare pairs one by one) | O(N)   | O(1)   | Works, but harder to think about |
| Sorting-based    | O(N log N) | O(1) | Sort first, then compare only first & last string |
| ✅ Vertical Scan (this solution) | O(N)   | O(1)   | Clean, intuitive, no sorting needed               |

*N = total number of characters across all strings*

# Complexity
- Time complexity: $$O(N)$$ — in the worst case, we look at every character across all strings once
- Space complexity: $$O(1)$$ — we only store `res`, which is at most the size of the prefix (no extra data structures)

# Code
```python3 []
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""

        for i in range(len(strs[0])):
            for s in strs[1:]:      # skip strs[0]
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

# Time Complexity: O(S)
# Space Complexity: O(1)
# by ar-sayeem [April 17, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀