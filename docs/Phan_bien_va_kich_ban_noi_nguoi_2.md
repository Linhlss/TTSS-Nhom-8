# Phản biện và kịch bản nói cho Người 2

## 1. Kịch bản nói ngắn

### Phần MPI

Phiên bản MPI chia tập chỉ số theo kiểu round-robin. Mỗi process tính một `local_sum` độc lập, sau đó dùng `MPI_Reduce` với phép cộng để đưa kết quả về `rank 0`. Chỉ `rank 0` in kết quả cuối. Điểm cần nhấn mạnh là MPI minh họa mô hình message passing, khác với OpenMP dùng shared memory.

### Phần benchmark

Mỗi cấu hình chạy ba lần và lấy trung bình. Strong scaling giữ `N = 10^8`, thay đổi số worker `1,2,4,8`. Weak scaling dùng `N = 10^7 × số worker`. Ba phiên bản đều chạy đúng đến `N = 10^9`.

### Phần kết quả

OpenMP và MPI đều tăng tốc rõ đến bốn worker. Tại tám worker, speedup vẫn tăng nhưng efficiency giảm còn khoảng `50%`. Kết quả phù hợp với giới hạn phần cứng Apple M1 gồm bốn performance core và bốn efficiency core, cộng với overhead reduction và lập lịch.

## 2. Câu hỏi phản biện bắt buộc

### Vì sao chọn tích phân số?

Phương pháp tích phân số theo quy tắc điểm giữa đủ đơn giản để tập trung vào decomposition, reduction, speedup và efficiency. Mỗi khoảng chia gần như độc lập nên phù hợp với cả OpenMP và MPI.

### Vì sao không chọn Chudnovsky làm lõi chính?

Chudnovsky phù hợp khi mục tiêu là tính rất nhiều chữ số Pi, nhưng dễ kéo đề tài sang số học độ chính xác tùy ý và thư viện GMP/MPFR. Scope của đề tài là đánh giá mô hình lập trình song song, không phải lập kỷ lục số chữ số Pi.

### Vì sao `schedule(static)` hợp lý?

Mỗi vòng lặp thực hiện gần như cùng lượng phép tính. `schedule(static)` chia việc từ đầu với overhead thấp; `dynamic` hoặc `guided` không phải trọng tâm và thường không cần thiết cho workload đồng đều này.

### Vì sao speedup không tuyến tính?

Khi tăng worker, chương trình phải chịu overhead tạo thread hoặc process, reduction, lập lịch và tranh chấp tài nguyên phần cứng. Trên Apple M1, tám core không hoàn toàn đồng nhất vì gồm performance core và efficiency core.

### OpenMP và MPI khác nhau thế nào?

OpenMP dùng thread trong shared memory nên code ngắn và phù hợp một máy đa lõi. MPI dùng process tách biệt và trao đổi dữ liệu qua message passing, có thể mở rộng sang cluster nhiều node nhưng có thêm chi phí giao tiếp.

### Hạn chế của benchmark trên máy cá nhân là gì?

MPI hiện được chạy trên một máy, nên chưa đo được chi phí mạng giữa nhiều node. Kết quả còn có thể dao động theo ứng dụng nền, trạng thái hệ điều hành và đặc điểm CPU không đồng nhất.

### Vì sao sai số không giảm đơn điệu tuyệt đối khi N tăng?

Sai số phương pháp tích phân giảm khi tăng `N`, nhưng phép cộng số thực hữu hạn gây rounding error tích lũy. Thứ tự cộng khác nhau giữa Serial, OpenMP và MPI cũng làm chữ số cuối dao động. Trong thí nghiệm, sai số vẫn chỉ cỡ `10^-14` đến `10^-13`.
