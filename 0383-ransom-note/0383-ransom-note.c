bool canConstruct(char* ransomNote, char* magazine) {
    int counter[26] = {0};
    
    for (int i = 0; magazine[i] != '\0'; i++) {
        counter[magazine[i] - 'a']++;
    }
    
    for (int i = 0; ransomNote[i] != '\0'; i++) {
        if (counter[ransomNote[i] - 'a'] == 0) {
            return false;
        }
        counter[ransomNote[i] - 'a']--;
    }
    
    return true;
}