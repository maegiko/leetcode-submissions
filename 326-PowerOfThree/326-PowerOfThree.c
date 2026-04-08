// Last updated: 08/04/2026, 12:39:55
bool isPowerOfThree(int n) {
    if (n == 1) return true;
    if (n % 3 != 0 || n < 1) return false;

    return isPowerOfThree(n / 3);
}