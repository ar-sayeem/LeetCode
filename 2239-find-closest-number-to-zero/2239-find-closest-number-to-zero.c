int findClosestNumber(int* nums, int numsSize) {
    int closest = nums[0];
    for (int i = 1; i < numsSize; i++) {
        int current = abs(nums[i]);
        int best = abs(closest);
        if (current < best || (current == best && nums[i] > closest)) {
            closest = nums[i];
        }
    }
    return closest;
}
