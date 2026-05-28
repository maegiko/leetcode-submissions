// Last updated: 28/05/2026, 15:34:10
1class Solution {
2    public boolean searchMatrix(int[][] matrix, int target) {
3        int mLeft = 0;
4        int mRight = matrix.length - 1;
5
6        while (mLeft <= mRight) {
7            int middle = (mLeft + mRight) / 2;
8
9            if (target > matrix[middle][0]) {
10                mLeft = middle + 1;
11            } else if (target < matrix[middle][0]) {
12                mRight = middle - 1;
13            } else {
14                return true;
15            }
16        }
17
18        if (mRight < 0) {
19            return false;
20        }
21
22        int nLeft = 0;
23        int nRight = matrix[mRight].length - 1;
24
25        while (nLeft <= nRight) {
26            int middle = (nLeft + nRight) / 2;
27
28            if (target > matrix[mRight][middle]) {
29                nLeft = middle + 1;
30            } else if (target < matrix[mRight][middle]) {
31                nRight = middle - 1;
32            } else {
33                return true;
34            }
35        }
36
37        return false;
38    }
39}