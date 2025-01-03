char * mergeAlternately(char * word1, char * word2) {
    int A = strlen(word1), B = strlen(word2);
    int a = 0, b = 0, index = 0, word = 1;
    char* result = (char*)malloc((A + B + 1) * sizeof(char));
    if (!result) return NULL;

    while (a < A && b < B) {
        if (word == 1) {
            result[index++] = word1[a++];
            word = 2;
        } else {
            result[index++] = word2[b++];
            word = 1;
        }
    }

    while (a < A) {
        result[index++] = word1[a++];
    }

    while (b < B) {
        result[index++] = word2[b++];
    }

    result[index] = '\0';
    return result;
}
