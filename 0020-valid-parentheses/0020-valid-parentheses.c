bool isValid(char* s) {
    char stack[strlen(s)];
    int top = -1;
    
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        } else {
            if (top == -1) return false;
            char topElement = stack[top--];
            if ((s[i] == ')' && topElement != '(') ||
                (s[i] == '}' && topElement != '{') ||
                (s[i] == ']' && topElement != '[')) {
                return false;
            }
        }
    }
    
    return top == -1;
}

// Time : O(n)
// Space: O(n)