class MinStack {
public:
    stack<long long int> s;
    long long int minVal;

    MinStack() {}

    void push(int val) {
        if (s.empty()) {
            s.push(val);
            minVal = val;
        } else {
            if (val < minVal) {
                s.push((long long)2 * val - minVal);
                minVal = val;
            } else {
                s.push(val);
            }
        }
    }

    void pop() {
        if (s.top() < minVal) {
            minVal = 2 * minVal - s.top();
        }
        s.pop();
    }

    int top() {
        if (s.top() < minVal) {
            return minVal;
        }
        return s.top();
    }

    int getMin() { return minVal; }
};

// Time Complexity  : O(1)
// Space Complexity : O(N)
// by ar-sayeem [June 14, 2026]