// Last updated: 08/04/2026, 12:40:03
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    int *new_array = malloc(2 * sizeof(int));
    
    // 0(n^2) time complexity
    // Do a double for loop, check target - nums[i], if that value exists in nums, those are your two inputs,
    // otherwise move to next i.    

    for (int i = 0; i < numsSize; i++) {
        int subtract = target - nums[i];
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[j] == subtract) {
                *returnSize = 2;
                new_array[0] = i;
                new_array[1] = j;
                return new_array;
            }
        }
    }
    *returnSize = 0;
    free(new_array);
    return 0;
}