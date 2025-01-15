int numJewelsInStones(char* jewels, char* stones) {
    int count = 0;
    char jewelSet[128] = {0};

    for (int i = 0; jewels[i] != '\0'; i++) {
        jewelSet[(int)jewels[i]] = 1;
    }

    for (int i = 0; stones[i] != '\0'; i++) {
        if (jewelSet[(int)stones[i]]) {
            count++;
        }
    }

    return count;
}
