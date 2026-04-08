// Last updated: 08/04/2026, 12:39:45
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int *array = malloc(numsSize * sizeof(int));
    int sum = nums[0];

    for (int i = 0; i < numsSize; i++) {
        if (i == 0) {
            array[0] = nums[0];
        } else {
            sum += nums[i];
            array[i] = sum;
        }
    }
    
    *returnSize = numsSize;
    return array;
}