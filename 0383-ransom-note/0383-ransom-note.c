bool canConstruct(char* ransomNote, char* magazine) {
    int counter[26] = {0}; // Array to count occurrences of each letter
    
    // Count the frequency of characters in the magazine
    for (int i = 0; magazine[i] != '\0'; i++) {
        counter[magazine[i] - 'a']++;
    }
    
    // Check if ransomNote can be constructed
    for (int i = 0; ransomNote[i] != '\0'; i++) {
        if (counter[ransomNote[i] - 'a'] == 0) {
            return false;
        }
        counter[ransomNote[i] - 'a']--;
    }
    
    return true;
}