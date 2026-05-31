# TTSS Nhóm 8 - Tính số Pi song song bằng OpenMP và MPI

Đề tài: **Xây dựng và đánh giá chương trình song song tính số Pi bằng phương pháp tích phân số sử dụng OpenMP và MPI**.

Project này đã được bổ sung phần code cho **Người 1**:

- Thiết kế cấu trúc chương trình.
- Viết bản `Serial` làm baseline.
- Viết bản `OpenMP`.
- Xử lý `reduction`, `race condition`, `shared memory`, `schedule(static)`.
- Thiết lập cách tính `Error`, `Speedup`, `Efficiency` và đo thời gian.

Project hiện tại cũng đã có phần kỹ thuật cần thiết để bạn hoàn thiện nhánh `MPI + benchmark`:

- Có source `MPI` dùng `MPI_Reduce`.
- Có thể benchmark chung `Serial`, `OpenMP`, `MPI`.
- Có thể xuất một file CSV chung để so sánh các phiên bản.

---

## 1. Cấu trúc thư mục

```text
TTSS-Nhom-8-main/
├── docs/
│   ├── Checklist_noi_bo_2_nguoi.md
│   ├── Muc_tieu_tong_the.md
│   ├── Phan_cong_tong_the_2_nguoi.md
│   ├── README_Xay_dung_bao_cao_tinh_Pi_song_song.md
│   ├── Phan_nguoi_1_code_notes.md
│   ├── Cau_hinh_thuc_nghiem.md
│   ├── Flowchart_MPI.md
│   ├── Noi_dung_bao_cao_nguoi_2.md
│   ├── Noi_dung_slide_nguoi_2.md
│   └── Phan_bien_va_kich_ban_noi_nguoi_2.md
│
├── include/
│   └── pi_common.h
│
├── src/
│   ├── pi_serial.c
│   ├── pi_openmp.c
│   ├── pi_openmp_race_demo.c
│   └── pi_mpi.c
│
├── scripts/
│   ├── run_serial.sh
│   ├── run_openmp.sh
│   ├── run_mpi.sh
│   ├── benchmark.py
│   ├── benchmark_suite.py
│   └── generate_charts.py
│
├── results/
│   ├── benchmark_result.csv
│   ├── raw_runs.csv
│   ├── n_size_results.csv
│   ├── strong_scaling_results.csv
│   └── weak_scaling_results.csv
│
├── report/
│   └── figures/
│
├── Makefile
└── README.md
```

---

## 2. Công thức tính Pi

Sử dụng công thức tích phân:

```text
π = ∫[0,1] 4 / (1 + x²) dx
```

Đoạn `[0, 1]` được chia thành `N` khoảng nhỏ:

```text
step = 1.0 / N
x_i = (i + 0.5) * step
pi ≈ step * Σ 4 / (1 + x_i²)
```

---

## 3. Biên dịch

Biên dịch toàn bộ project:

```bash
make all
```

Lệnh này build `Serial`, `OpenMP` và `MPI`.

Biên dịch riêng Serial:

```bash
make serial
```

Biên dịch riêng OpenMP:

```bash
make openmp
```

Biên dịch MPI nếu máy có `mpicc`:

```bash
make mpi
```

Xóa file biên dịch và kết quả:

```bash
make clean
```

---

## 4. Chạy chương trình

Chạy Serial:

```bash
./bin/pi_serial 100000000
```

Chạy OpenMP với 4 thread:

```bash
./bin/pi_openmp 100000000 4
```

Chạy script Serial:

```bash
bash scripts/run_serial.sh 100000000
```

Chạy script OpenMP:

```bash
bash scripts/run_openmp.sh 100000000 4
```

Chạy MPI nếu máy có MPI:

```bash
mpirun -np 4 ./bin/pi_mpi 100000000
```

Hoặc dùng script:

```bash
bash scripts/run_mpi.sh 100000000 4
```

---

## 5. Chạy benchmark

Chạy benchmark với `N = 100000000`, lặp 3 lần, OpenMP với `1, 2, 4, 8` thread và MPI với `1, 2, 4, 8` process:

```bash
python3 scripts/benchmark.py 100000000 3 1,2,4,8 1,2,4,8
```

Hoặc dùng Makefile:

```bash
make benchmark
```

Kết quả được lưu tại:

```text
results/benchmark_result.csv
```

Các cột kết quả gồm:

```text
mode,N,workers,pi,error,time_sec,time_std,speedup,efficiency,efficiency_percent
```

File này sẽ chứa nhiều dòng `mode = serial`, `mode = openmp` và `mode = mpi`, giúp so sánh trực tiếp trên cùng một định dạng dữ liệu.

Để chạy toàn bộ thí nghiệm bắt buộc gồm thay đổi `N`, strong scaling, weak scaling và so sánh OpenMP/MPI:

```bash
make benchmark-suite
make charts
```

Kết quả chi tiết được lưu trong `results/`; biểu đồ được lưu trong `report/figures/`.

---

## 6. Công thức đánh giá

Sai số tuyệt đối:

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

Trong đó `p` là số thread hoặc số process.

---

## 7. Ghi chú phần Người 1

File chính của Người 1:

```text
src/pi_serial.c
src/pi_openmp.c
include/pi_common.h
scripts/benchmark.py
docs/Phan_nguoi_1_code_notes.md
```

File `src/pi_openmp_race_demo.c` chỉ dùng để minh họa lỗi `race condition`, không dùng làm kết quả chính trong báo cáo.
