class MinStack {
public:
    stack<pair<int, int>> s;
    MinStack() {}

    void push(int val) {
        if (s.empty()) {
            s.push({val, val});
        } else {
            int minVal = min(val, s.top().second);
            s.push({val, minVal});
        }
    }

    void pop() { return s.pop(); }

    int top() { return s.top().first; }

    int getMin() { return s.top().second; }
};

// Time Complexity  : O(1)
// Space Complexity : O(N)
// by ar-sayeem [June 14, 2026]