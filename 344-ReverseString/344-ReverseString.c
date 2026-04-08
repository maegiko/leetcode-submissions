// Last updated: 08/04/2026, 12:39:54
void reverseString(char* s, int sSize) {
    int mid = sSize  / 2;
    int j = sSize - 1;
    
    for (int i = 0; i < mid; i++) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        j--;
    }
}