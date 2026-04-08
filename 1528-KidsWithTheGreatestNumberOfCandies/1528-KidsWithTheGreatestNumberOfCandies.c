// Last updated: 08/04/2026, 12:39:49
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    bool *array = malloc(sizeof(bool) * candiesSize);
    for (int i = 0; i < candiesSize; i++) {
        array[i] = true;
    }

    for (int i = 0; i < candiesSize; i++) {
        for (int j = 0; j < candiesSize; j++) {
            if ((candies[i] + extraCandies) < candies[j]) {
                array[i] = false;
            }
        }
    }

    *returnSize = candiesSize;
    return array;
}