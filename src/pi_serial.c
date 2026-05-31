#include "pi_common.h"

int main(int argc, char **argv) {
    long long n = parse_long_long_arg(argc, argv, 1, 100000000LL, "N");

    double step = 1.0 / (double)n;
    double sum = 0.0;

    double start = wall_time_seconds();

    for (long long i = 0; i < n; ++i) {
        double x = ((double)i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x);
    }

    double pi_value = step * sum;
    double end = wall_time_seconds();

    print_csv_result("serial", n, 1, pi_value, end - start);
    return 0;
}
