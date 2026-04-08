// Last updated: 08/04/2026, 12:39:50


int fib(int n){
    if (n == 0) return 0;
    if (n == 1) return 1;

    return fib(n - 1) + fib(n - 2);
}