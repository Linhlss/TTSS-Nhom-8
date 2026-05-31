# Ghi chú phần code của Người 1

## 1. Thiết kế cấu trúc chương trình

Người 1 phụ trách thiết kế cấu trúc project để các phiên bản `Serial`, `OpenMP` và `MPI` dùng chung một công thức tính Pi, cùng định dạng đầu ra và cùng cách đánh giá kết quả. Cấu trúc này giúp việc so sánh thời gian chạy, sai số, speedup và efficiency trở nên rõ ràng hơn.

Các file chính của Người 1 gồm:

```text
include/pi_common.h
src/pi_serial.c
src/pi_openmp.c
src/pi_openmp_race_demo.c
scripts/benchmark.py
```

## 2. Phiên bản Serial

File:

```text
src/pi_serial.c
```

Bản `Serial` chạy tuần tự trên một luồng duy nhất. Đây là baseline để kiểm tra độ đúng của thuật toán và làm mốc tính speedup cho các bản song song.

Ý tưởng:

```text
1. Nhập số khoảng chia N.
2. Tính step = 1.0 / N.
3. Duyệt i từ 0 đến N - 1.
4. Tính x = (i + 0.5) * step.
5. Cộng f(x) = 4 / (1 + x²) vào sum.
6. Tính pi = step * sum.
```

## 3. Phiên bản OpenMP

File:

```text
src/pi_openmp.c
```

Bản `OpenMP` song song hóa vòng lặp tính tổng bằng chỉ thị:

```c
#pragma omp parallel for reduction(+:sum) schedule(static)
```

Trong đó:

- `parallel for`: chia vòng lặp cho nhiều thread.
- `reduction(+:sum)`: tạo biến `sum` cục bộ cho từng thread rồi cộng lại ở cuối.
- `schedule(static)`: chia đều số vòng lặp cho các thread ngay từ đầu.

## 4. Reduction

Trong bài toán tính Pi, biến `sum` là biến cộng dồn. Nếu nhiều thread cùng cập nhật trực tiếp vào một biến `sum` chung thì có thể xảy ra lỗi. Vì vậy, chương trình sử dụng `reduction(+:sum)` để mỗi thread có tổng cục bộ riêng và OpenMP tự gộp kết quả cuối cùng.

## 5. Race condition

File:

```text
src/pi_openmp_race_demo.c
```

File này minh họa cách viết sai khi nhiều thread cùng cập nhật biến `sum` chung mà không dùng `reduction`. Đây là ví dụ để giải thích `race condition`, không phải file kết quả chính.

## 6. Shared memory

OpenMP sử dụng mô hình shared memory. Các thread cùng nằm trong một process nên có thể dùng chung vùng nhớ. Trong code:

- `N` và `step` là dữ liệu dùng chung.
- `sum` là biến cần xử lý bằng `reduction`.
- `x` được khai báo bên trong vòng lặp để mỗi lần lặp có biến riêng.

## 7. Schedule(static)

Bài toán tính Pi có workload đồng đều vì mỗi vòng lặp đều thực hiện lượng tính toán gần giống nhau. Do đó, `schedule(static)` là lựa chọn phù hợp vì chi phí điều phối thấp và dễ đạt cân bằng tải giữa các thread.

## 8. Error, Speedup, Efficiency

Sai số:

```text
Error = |pi_computed - pi_reference|
```

Speedup:

```text
Speedup = T_serial / T_parallel
```

Efficiency:

```text
Efficiency = Speedup / p
```

Trong đó `p` là số thread hoặc process.

## 9. Đo thời gian

Code sử dụng hàm `wall_time_seconds()` trong `include/pi_common.h` để đo thời gian phần tính toán chính. Script `scripts/benchmark.py` chạy nhiều lần, lấy thời gian trung bình và ghi kết quả ra file CSV.
