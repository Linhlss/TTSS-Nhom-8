#include "pi_common.h"
#include <omp.h>

int main(int argc, char **argv) {
    long long n = parse_long_long_arg(argc, argv, 1, 100000000LL, "N");
    int threads = parse_int_arg(argc, argv, 2, 4, "threads");

    omp_set_num_threads(threads);

    double step = 1.0 / (double)n;
    double sum = 0.0;

    double start = wall_time_seconds();

    /*
       schedule(static): chia đều số vòng lặp cho các thread ngay từ đầu.
       reduction(+:sum): mỗi thread có sum cục bộ, cuối vòng lặp OpenMP tự cộng lại.
       Nhờ đó tránh race condition khi nhiều thread cùng cộng vào biến sum.
    */
    #pragma omp parallel for reduction(+:sum) schedule(static)
    for (long long i = 0; i < n; ++i) {
        double x = ((double)i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x);
    }

    double pi_value = step * sum;
    double end = wall_time_seconds();

    print_csv_result("openmp", n, threads, pi_value, end - start);
    return 0;
}
