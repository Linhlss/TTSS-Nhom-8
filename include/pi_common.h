#ifndef PI_COMMON_H
#define PI_COMMON_H

#ifndef _WIN32
#ifndef _POSIX_C_SOURCE
#define _POSIX_C_SOURCE 200809L
#endif
#endif

#include <errno.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#if defined(_WIN32)
#include <windows.h>
static inline double wall_time_seconds(void) {
    LARGE_INTEGER freq;
    LARGE_INTEGER counter;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&counter);
    return (double)counter.QuadPart / (double)freq.QuadPart;
}
#else
#include <time.h>
static inline double wall_time_seconds(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec * 1e-9;
}
#endif

static inline long long parse_long_long_arg(int argc, char **argv, int index, long long default_value, const char *name) {
    if (argc <= index) {
        return default_value;
    }

    errno = 0;
    char *endptr = NULL;
    long long value = strtoll(argv[index], &endptr, 10);

    if (errno != 0 || endptr == argv[index] || *endptr != '\0' || value <= 0) {
        fprintf(stderr, "Invalid %s: %s\n", name, argv[index]);
        fprintf(stderr, "Usage example: %s 100000000\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    return value;
}

static inline int parse_int_arg(int argc, char **argv, int index, int default_value, const char *name) {
    if (argc <= index) {
        return default_value;
    }

    errno = 0;
    char *endptr = NULL;
    long value = strtol(argv[index], &endptr, 10);

    if (errno != 0 || endptr == argv[index] || *endptr != '\0' || value <= 0 || value > 1024) {
        fprintf(stderr, "Invalid %s: %s\n", name, argv[index]);
        fprintf(stderr, "Usage example: %s 100000000 4\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    return (int)value;
}

static inline double pi_reference(void) {
    return acos(-1.0);
}

static inline void print_csv_result(const char *mode, long long n, int workers, double pi_value, double elapsed_seconds) {
    double reference = pi_reference();
    double error = fabs(pi_value - reference);

    printf("mode,N,workers,pi,error,time_sec\n");
    printf("%s,%lld,%d,%.15f,%.15e,%.9f\n", mode, n, workers, pi_value, error, elapsed_seconds);
}

#endif
