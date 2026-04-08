// Last updated: 08/04/2026, 12:39:48
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int richest = 0;
    
    for (int i = 0; i < accountsSize; i++) {
        int sum = 0;
        for (int j = 0; j < accountsColSize[i]; j++) {
            sum += accounts[i][j];
        }

        if (sum > richest) {
            richest = sum;
        }
    }
    return richest;
}