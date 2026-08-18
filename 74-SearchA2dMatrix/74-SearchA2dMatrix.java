// Last updated: 18/08/2026, 14:57:56
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int mLeft = 0;
        int mRight = matrix.length - 1;

        while (mLeft <= mRight) {
            int middle = (mLeft + mRight) / 2;

            if (target > matrix[middle][0]) {
                mLeft = middle + 1;
            } else if (target < matrix[middle][0]) {
                mRight = middle - 1;
            } else {
                return true;
            }
        }

        if (mRight < 0) {
            return false;
        }

        int nLeft = 0;
        int nRight = matrix[mRight].length - 1;

        while (nLeft <= nRight) {
            int middle = (nLeft + nRight) / 2;

            if (target > matrix[mRight][middle]) {
                nLeft = middle + 1;
            } else if (target < matrix[mRight][middle]) {
                nRight = middle - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}