// Last updated: 08/04/2026, 12:39:47
int numberOfSteps(int num) {
    int steps = 0;

    while (num != 0) {
        if (num % 2 == 0) {
            num = num / 2;
            steps++;
        } else {
            num = num - 1;
            steps++;
        }
    }
    return steps;
}