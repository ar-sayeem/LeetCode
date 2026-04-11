class Solution {
public:
    string removeOccurrences(string s, string part) {
        while (s.length() > 0 && s.find(part) < s.length()) {
            s.erase(s.find(part), part.length());   // erase(start, size)
        }
        return s;
    }
};

// Time Complexity: O(N² / M)  — find() + erase() repeated N/M times
// Space Complexity: O(1)
// by ar-sayeem [April 11, 2026]