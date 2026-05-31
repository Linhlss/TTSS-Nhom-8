#include "pi_common.h"
#include <mpi.h>

int main(int argc, char **argv) {
    MPI_Init(&argc, &argv);

    int rank = 0;
    int size = 1;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    long long n = parse_long_long_arg(argc, argv, 1, 100000000LL, "N");
    double step = 1.0 / (double)n;

    MPI_Barrier(MPI_COMM_WORLD);
    double start = MPI_Wtime();

    double local_sum = 0.0;

    /*
       Chia chỉ số theo kiểu round-robin:
       process rank r xử lý i = r, r + size, r + 2*size, ...
    */
    for (long long i = rank; i < n; i += size) {
        double x = ((double)i + 0.5) * step;
        local_sum += 4.0 / (1.0 + x * x);
    }

    double global_sum = 0.0;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    double end = MPI_Wtime();

    if (rank == 0) {
        double pi_value = step * global_sum;
        print_csv_result("mpi", n, size, pi_value, end - start);
    }

    MPI_Finalize();
    return 0;
}
