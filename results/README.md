# Bộ dữ liệu benchmark

Các file trong thư mục này được sinh tự động bằng:

```bash
python3 scripts/benchmark_suite.py 3
python3 scripts/generate_charts.py
```

## Dữ liệu gốc

- `raw_runs.csv`: từng lần đo riêng biệt, dùng để kiểm tra lại số liệu.

## Dữ liệu tổng hợp

- `benchmark_result.csv`: benchmark cơ bản trên một giá trị `N`.
- `n_size_results.csv`: ảnh hưởng của `N = 10^6, 10^7, 10^8, 10^9`.
- `strong_scaling_results.csv`: strong scaling tại `N = 10^8`.
- `weak_scaling_results.csv`: weak scaling với `N = 10^7 × workers`.
- `openmp_mpi_comparison.csv`: so sánh trực tiếp OpenMP và MPI.

## Bảng đưa vào báo cáo

- `table_strong_scaling.csv`
- `table_error_by_n.csv`
- `table_weak_scaling.csv`
