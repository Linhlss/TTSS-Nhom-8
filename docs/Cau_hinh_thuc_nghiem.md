# Cấu hình thực nghiệm và quy tắc benchmark

## 1. Cấu hình máy

Các số liệu hiện tại được đo trên máy:

| Thành phần | Giá trị |
|---|---|
| Thiết bị | MacBook Pro |
| Chip | Apple M1 |
| CPU | 8 core: 4 performance core và 4 efficiency core |
| RAM | 16 GB |
| Hệ điều hành | macOS 26.0 |
| Trình biên dịch C | Homebrew GCC 15.2.0 |
| MPI runtime | Open MPI 5.0.9 |
| Python | Python 3.13.5 |

## 2. Cờ biên dịch

Ba phiên bản được biên dịch thống nhất với:

```text
-O3 -Wall -Wextra -std=c11 -Iinclude
```

Phiên bản OpenMP bổ sung:

```text
-fopenmp
```

## 3. Quy tắc đo

- Mỗi cấu hình chạy `3` lần.
- Giá trị thời gian trong bảng là trung bình cộng.
- `time_std` là độ lệch chuẩn giữa các lần đo.
- Thời gian chỉ bao quanh phần tính toán chính.
- MPI dùng `MPI_Barrier` trước khi đo và chỉ `rank 0` in kết quả.
- Strong scaling dùng cùng `N = 10^8`.
- So sánh trực tiếp OpenMP và MPI dùng cùng `N` và cùng số worker.
- Weak scaling dùng `N = 10^7 × số worker`.
- Khi lấy số liệu chính thức nên đóng ứng dụng nền nặng và không chạy nhiều benchmark đồng thời.

## 4. Công thức đánh giá

```text
Error      = |pi_computed - pi_reference|
Speedup    = T_serial / T_parallel
Efficiency = Speedup / số worker
```

Với weak scaling, efficiency được tính:

```text
Weak efficiency = T_1 / T_p
```

trong đó lượng công việc trên mỗi worker được giữ gần như không đổi.
