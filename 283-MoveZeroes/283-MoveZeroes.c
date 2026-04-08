// Last updated: 08/04/2026, 12:39:56
void moveZeroes(int* nums, int numsSize) {
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) continue;
        nums[j] = nums[i];
        j++;
    }

    for (; j < numsSize; j++) {
        nums[j] = 0;
    }
}