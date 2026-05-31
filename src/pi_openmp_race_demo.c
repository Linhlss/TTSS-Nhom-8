#include "pi_common.h"
#include <omp.h>

/*
   File này chỉ dùng để minh họa lỗi race condition.
   Không dùng file này làm kết quả chính trong báo cáo.

   Lỗi nằm ở dòng: sum += ...
   Nhiều thread cùng cập nhật biến sum chung nên kết quả có thể sai hoặc không ổn định.
*/
int main(int argc, char **argv) {
    long long n = parse_long_long_arg(argc, argv, 1, 10000000LL, "N");
    int threads = parse_int_arg(argc, argv, 2, 4, "threads");

    omp_set_num_threads(threads);

    double step = 1.0 / (double)n;
    double sum = 0.0;

    double start = wall_time_seconds();

    #pragma omp parallel for schedule(static)
    for (long long i = 0; i < n; ++i) {
        double x = ((double)i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x); /* race condition */
    }

    double pi_value = step * sum;
    double end = wall_time_seconds();

    print_csv_result("openmp_race_demo", n, threads, pi_value, end - start);
    return 0;
}
