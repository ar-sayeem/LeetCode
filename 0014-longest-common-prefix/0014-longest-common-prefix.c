char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        return "";
    }
    
    char* prefix = strs[0];
    for (int i = 1; i < strsSize; i++) {
        while (strncmp(prefix, strs[i], strlen(prefix)) != 0) {
            prefix[strlen(prefix) - 1] = '\0';
            if (strlen(prefix) == 0) {
                return "";
            }
        }
    }
    return prefix;
}
