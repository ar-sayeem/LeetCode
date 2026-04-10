class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());

        string ans = "";
        int i = 0, n = s.size();

        while (i < n) {
            string word = "";

            // build word
            while (i < n && s[i] != ' ') {
                word += s[i];
                i++;
            }

            // reverse word back
            reverse(word.begin(), word.end());

            // add to answer
            if (word.size() > 0) {
                ans += " " + word;
            }

            i++;    // skip space
        }

        // remove leading space
        return ans.substr(1);
    }
};

// Time Complexity: O(N)
// Space Complexity: O(N)
// by ar-sayeem [April 10, 2026]