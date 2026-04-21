# Hash Table | 3 Ways Shown | O(n) Time · O(1) Space | Beginner Friendly

# 📊 Learn Every Way to Solve Valid Anagram | Hash Table Focus | Beginner

# Intuition
Imagine you and your friend each have a bag of Scrabble tiles.
You want to check if both bags contain the exact same letters.

Your plan: count your tiles first, write them in a notebook.
Then go through your friend's bag — cross off one tile at a time.
If you ever try to cross off a tile that's already at zero (or doesn't exist) — the bags are different!
If you finish crossing everything off cleanly — they match. Anagram confirmed. ✅

Mapping to code:
- `s` → your bag of tiles
- `t` → your friend's bag
- `freq` → your notebook (letter → count)

# Approach

## 🧰 Quick Concepts for Beginners (read this first!)

**What is a Hash Table (Dictionary)?**
→ A notebook where every word has a value next to it. Like: `"a" → 3` means "I've seen 'a' three times."
→ In Python we call it a `dict`. Example: `freq = {}` starts a blank notebook. `freq["a"] = 2` writes in it.
→ Looking something up in a dict is O(1) — instant, no matter how big it gets. That's why we love it!

**What is `.get(key, default)`?**
→ Safely reads from a dictionary. If the key doesn't exist yet, returns the default value instead of crashing.
→ Example: `freq.get("z", 0)` → returns `0` if `"z"` was never added. Saves you from a KeyError!

**What is `sorted()`?**
→ Rearranges a string into alphabetical order. If two strings are anagrams, their sorted versions must be identical.
→ Example: `sorted("rat")` → `['a','r','t']` and `sorted("tar")` → `['a','r','t']` → equal → anagram! ✅
→ But sorting takes O(n log n) time — slower than the hash table approach.

**What is `Counter`?**
→ A built-in Python tool that counts everything in a string automatically — like doing our manual loop in one line.
→ `Counter("rat")` → `{'r':1, 'a':1, 't':1}`. Clean and powerful, but uses O(n) space.

---

## 💡 Method 1 — Sorting (simplest to understand)

```python3
return sorted(s) == sorted(t)         # O(n log n) time, O(n) space
```

Sort both strings alphabetically and compare.
If they're anagrams, the sorted result will always be identical.
⚠️ This is the easiest to understand but slowest — sorting costs O(n log n).
Great for interviews when you want to show you know multiple approaches!

---

## 💡 Method 2 — Counter (most Pythonic)

```python3
return Counter(s) == Counter(t)       # O(n) time, O(n) space
```

`Counter` builds a frequency dictionary for both strings automatically, then compares them.
One line, very readable — but it creates two full dictionaries so space is O(n).
Perfect when you want clean, short code and space isn't a concern.

---

## 💡 Method 3 — Hash Table (best overall) ⬅️ main approach

This is the main solution. Faster than sorting, more memory efficient than Counter.
Let's go step by step.

---

## Step 1 — Early exit if lengths differ

```python3
if len(s) != len(t):
    return False
```

If `s = "rat"` and `t = "rats"`, they can't possibly be anagrams — one has an extra letter.
Checking lengths first saves us from doing unnecessary work.
⚠️ Always add this guard — it's a free O(1) speed boost.

---

## Step 2 — Build the frequency notebook from `s`

```python3
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1    # update char frequency
```

We go through every character `c` in `s` and tally it up.
`freq.get(c, 0)` reads the current count (0 if never seen before), then we add 1.

After looping `s = "rat"`:
```
freq = {'r': 1, 'a': 1, 't': 1}
```
This is our "budget" — how many times each letter is allowed to appear in `t`.

---

## Step 3 — Spend the budget using `t`

```python3
for c in t:
    if freq.get(c, 0) == 0:         # char not in s, or already used up
        return False
    freq[c] -= 1                    # spend one usage of this char
```

Now we loop through `t` and "spend" one usage of each character.

**The check:** `freq.get(c, 0) == 0` catches two situations:
- The character was never in `s` at all → budget doesn't exist → returns `0`
- We already spent all copies of it → budget ran out → returns `0`

Either way → `t` is using something `s` doesn't have → `return False` immediately.

**The deduction:** `freq[c] -= 1` crosses off one tile from the notebook.
If `freq['a']` was `2`, it becomes `1`. See it again → `0`. See it a third time → caught! ✅

💡 We check *before* decrementing — so we never go negative.

---

## Step 4 — All clear

```python3
return True
```

If we looped all of `t` without hitting `False`, every character was found and accounted for.
The budgets balanced out perfectly. They're anagrams!

---

## 🛣️ Visual: The Scrabble Tile Notebook

**Example:** `s = "anagram"`, `t = "nagaram"`

**After Step 2 — notebook built from `s`:**
```
freq = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
```

**Step 3 — spending the budget, one char at a time from `t = "nagaram"`:**

| Turn | char `c` | freq.get(c,0) | Zero? | Action          | freq after                            |
|------|----------|---------------|-------|-----------------|---------------------------------------|
| 1    | 'n'      | 1             | No    | freq['n'] → 0   | {'a':3, 'n':0, 'g':1, 'r':1, 'm':1} |
| 2    | 'a'      | 3             | No    | freq['a'] → 2   | {'a':2, 'n':0, 'g':1, 'r':1, 'm':1} |
| 3    | 'g'      | 1             | No    | freq['g'] → 0   | {'a':2, 'n':0, 'g':0, 'r':1, 'm':1} |
| 4    | 'a'      | 2             | No    | freq['a'] → 1   | {'a':1, 'n':0, 'g':0, 'r':1, 'm':1} |
| 5    | 'r'      | 1             | No    | freq['r'] → 0   | {'a':1, 'n':0, 'g':0, 'r':0, 'm':1} |
| 6    | 'a'      | 1             | No    | freq['a'] → 0   | {'a':0, 'n':0, 'g':0, 'r':0, 'm':1} |
| 7    | 'm'      | 1             | No    | freq['m'] → 0   | {'a':0, 'n':0, 'g':0, 'r':0, 'm':0} |

All values → 0. No False triggered.

**Answer = True ✅**

---

## 🔁 All 3 Approaches Compared

| Approach | Time | Space | Pros | Cons |
|---|---|---|---|---|
| `sorted(s) == sorted(t)` | O(n log n) | O(n) | Simplest to understand, no imports | Slowest of the three |
| `Counter(s) == Counter(t)` | O(n) | O(n) | Cleanest one-liner, very readable | Uses more memory (two full dicts) |
| **Hash Table `freq` dict** | **O(n)** | **O(1)** | **Fastest + most memory efficient** | **Slightly more code to write** |

💡 In an interview, mention all three — then explain why you chose the hash table. That's what impresses interviewers!

# Complexity
- Time complexity: $$O(n)$$ — we loop through `s` once and `t` once, where n = length of the strings
- Space complexity: $$O(1)$$ — `freq` holds at most 26 keys (fixed English alphabet), so it never grows with input size

# Code
```python3 []
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)       # O(n) time, O(n) space
        # return sorted(s) == sorted(t)         # O(n log n) time, O(n) space

        if len(s) != len(t):
            return False

        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1    # update char frequency
        for c in t:
            if freq.get(c, 0) == 0:         # char not in s, or already used up
                return False
            freq[c] -= 1                    # spend one usage of this char
        return True


# Time Complexity:  O(n)
# Space Complexity: O(1)
# by ar-sayeem [April 09, 2026]
```

> 💡 **One last thing:** Don't copy-paste this code! Close this post, open a blank editor, and rewrite it from memory. Even if it takes 3 tries — that's how it actually sticks. You've got this! 🚀