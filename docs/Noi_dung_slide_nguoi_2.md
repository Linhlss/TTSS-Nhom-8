# Nội dung slide do Người 2 phụ trách

File này là nguồn để ghép vào bộ slide chung sau khi cả nhóm chốt template.

---

## Slide: Phiên bản MPI

- Mỗi process nhận `rank` và `size`.
- Chia chỉ số kiểu round-robin: `i = rank, rank + size, ...`.
- Mỗi process tính `local_sum`.
- Dùng `MPI_Reduce(..., MPI_SUM, root = 0)` để gộp kết quả.
- Chỉ `rank 0` in giá trị Pi, error và thời gian.

Hình dùng: sơ đồ trong [Flowchart_MPI.md](Flowchart_MPI.md).

---

## Slide: Thiết lập benchmark

- Máy: MacBook Pro Apple M1, 8 core, RAM 16 GB.
- Compiler: GCC 15.2.0, `-O3`.
- MPI: Open MPI 5.0.9.
- Mỗi cấu hình chạy 3 lần, lấy trung bình.
- Strong scaling: `N = 10^8`, worker `1,2,4,8`.
- Weak scaling: `N = 10^7 × workers`.

---

## Slide: Strong scaling

Thông điệp chính:

- OpenMP đạt speedup `3.59×` tại `4` thread và `4.39×` tại `8` thread.
- MPI đạt speedup `3.72×` tại `4` process và `4.18×` tại `8` process.
- Efficiency giảm rõ tại `8` worker do overhead và giới hạn phần cứng.

Hình dùng:

- `report/figures/speedup_strong_scaling.png`
- `report/figures/efficiency_strong_scaling.png`

---

## Slide: Weak scaling và sai số

Thông điệp chính:

- Weak efficiency còn khoảng `52.40%` với OpenMP và `48.53%` với MPI tại `8` worker.
- Ba phiên bản đều chạy đúng đến `N = 10^9`.
- Sai số cỡ `10^-14` đến `10^-13`, không giảm đơn điệu tuyệt đối do rounding error.

Hình dùng:

- `report/figures/time_weak_scaling.png`
- `report/figures/error_by_n.png`

---

## Slide: So sánh và kết luận

- OpenMP phù hợp shared memory trên một máy, cú pháp ngắn và overhead thấp.
- MPI minh họa message passing và reduction; có thể mở rộng sang cluster.
- Speedup không tuyến tính hoàn toàn vì overhead, reduction cost và giới hạn CPU.
- Hướng phát triển: chạy MPI trên cluster nhiều node; thử Hybrid MPI + OpenMP nếu còn thời gian.
