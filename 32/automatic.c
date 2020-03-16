#include <stdio.h>

static const double five_ninths = 5.0/9.0;

double celsius(double fahrenheit){
    double c = (fahrenheit - 32) * five_ninths;
    return c;
}

int main() {
    double f = 100;
    printf("%f F is %f C\n", f, celsius(f));
    return 0;
}