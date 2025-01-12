/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    char** result = malloc(numsSize * sizeof(char*));
    *returnSize = 0;
    int i = 0;

    while (i < numsSize) {
        int start = nums[i];
        while (i < numsSize - 1 && nums[i] + 1 == nums[i + 1]) {
            i++;
        }
        
        int len;
        if (start != nums[i]) {
            len = snprintf(NULL, 0, "%d->%d", start, nums[i]) + 1;
            result[*returnSize] = malloc(len);
            snprintf(result[*returnSize], len, "%d->%d", start, nums[i]);
        } else {
            len = snprintf(NULL, 0, "%d", start) + 1;
            result[*returnSize] = malloc(len);
            snprintf(result[*returnSize], len, "%d", start);
        }
        
        (*returnSize)++;
        i++;
    }

    return result;
}
