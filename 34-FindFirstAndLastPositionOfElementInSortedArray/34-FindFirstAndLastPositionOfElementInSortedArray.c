// Last updated: 08/04/2026, 12:40:01
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int *array = malloc(2 * sizeof(int));

    *returnSize = 2;
    array[0] = -1;
    array[1] = -1;

    int last;

    if (sizeof(nums) == 0) {
        return array;
    }
    bool found = false;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == target && found == false) {
            array[0] = i;
            last = i;
            found = true;
        } else if (nums[i] == target && found == true) {
            last = i;
        }
    }

    if (found == true) {
        array[1] = last;
    } 

    return array;
    
}