# Flowchart MPI

Sơ đồ này mô tả luồng xử lý của phiên bản `src/pi_mpi.c`.

```mermaid
flowchart TD
    A["Bắt đầu"] --> B["MPI_Init"]
    B --> C["Lấy rank và số process"]
    C --> D["Đọc N, tính step = 1 / N"]
    D --> E["MPI_Barrier và bắt đầu đo thời gian"]
    E --> F["Mỗi rank xử lý i = rank, rank + size, ..."]
    F --> G["Tính local_sum trên từng process"]
    G --> H["MPI_Reduce: cộng local_sum về rank 0"]
    H --> I{"rank == 0?"}
    I -- "Có" --> J["Tính Pi, error, thời gian và in CSV"]
    I -- "Không" --> K["Bỏ qua bước in kết quả"]
    J --> L["MPI_Finalize"]
    K --> L
    L --> M["Kết thúc"]
```

## Điểm cần trình bày

- Mỗi process xử lý một tập chỉ số độc lập theo kiểu round-robin.
- Không có ghi đồng thời vào cùng một biến giữa các process.
- `MPI_Reduce` thực hiện phép cộng các tổng cục bộ và trả kết quả về `rank 0`.
- Chỉ `rank 0` in kết quả để output không bị lặp.
