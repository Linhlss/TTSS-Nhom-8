# Phân công tổng thể và chi tiết cho nhóm 2 người

## Mục đích tài liệu

Tài liệu này dùng để mô tả rõ cách chia việc của nhóm 2 người cho đề tài:

> **Xây dựng và đánh giá chương trình song song tính số Pi bằng phương pháp tích phân số sử dụng OpenMP và MPI**

Mục tiêu của cách chia việc là:

- Bảo đảm cả 2 thành viên đều có đóng góp kỹ thuật rõ ràng.
- Tránh tình trạng một người chỉ làm code, người còn lại chỉ làm trình bày.
- Dễ chứng minh phần việc của từng người khi giảng viên hoặc người ngoài xem lại.
- Giữ tiến độ đồng đều từ cài đặt, benchmark, báo cáo đến slide và bảo vệ.

Trong tài liệu này, nhóm được ký hiệu là:

- **Người 1**
- **Người 2**

Có thể thay hai nhãn này bằng tên thật của thành viên sau.

---

## Nguyên tắc phân công

Nhóm áp dụng nguyên tắc:

- Mỗi người phụ trách một nhánh kỹ thuật chính.
- Mỗi người đều phải có phần việc ở cả 3 mảng: kỹ thuật, báo cáo, thuyết trình.
- Mỗi kết quả quan trọng đều có người phụ trách chính và người phối hợp kiểm tra.
- Các phần dùng chung như aim, scope, bộ tham số benchmark, format output và kết luận phải được thống nhất bởi cả nhóm.

---

## Cách chia việc tổng thể

### Người 1: Thuật toán lõi, Serial/OpenMP, thiết kế và cơ sở lý thuyết

Người 1 phụ trách chính các nội dung sau:

- Xây dựng bản tuần tự làm baseline.
- Xây dựng bản song song bằng OpenMP.
- Thiết kế cấu trúc code dùng chung giữa các phiên bản.
- Xử lý các nội dung liên quan đến `reduction`, `race condition`, `shared memory`.
- Viết phần lý thuyết và phần phân tích thiết kế thuật toán.
- Chuẩn bị sơ đồ thuật toán tuần tự và sơ đồ OpenMP.

### Người 2: MPI, benchmark, phân tích thực nghiệm và đánh giá

Người 2 phụ trách chính các nội dung sau:

- Xây dựng bản song song bằng MPI.
- Thiết lập script benchmark và tổ chức lưu kết quả.
- Chạy thực nghiệm và tổng hợp dữ liệu.
- Tính toán và trình bày các bảng `time`, `speedup`, `efficiency`, `error`.
- Viết phần kịch bản thực nghiệm, kết quả và đánh giá.
- Chuẩn bị sơ đồ MPI và các biểu đồ số liệu.

### Phần hai người cùng chịu trách nhiệm

- Chốt aim, scope, tiêu chí hoàn thành.
- Thống nhất bộ tham số đầu vào và định dạng output.
- Kiểm tra tính đúng đắn giữa các phiên bản.
- Viết mở đầu và kết luận.
- Ghép báo cáo hoàn chỉnh.
- Làm slide tổng thể.
- Tập thuyết trình và chuẩn bị trả lời phản biện.

---

## Ma trận phân công chi tiết

| Hạng mục | Người phụ trách chính | Người phối hợp | Kết quả đầu ra |
|---|---|---|---|
| Chốt bài toán, aim, scope, tiêu chí hoàn thành | Cả hai | Cả hai | Bản định hướng thống nhất |
| Thiết kế cấu trúc chương trình | Người 1 | Người 2 | Khung thư mục, khung hàm, format output |
| Cài đặt `Serial` | Người 1 | Người 2 kiểm tra | Chương trình baseline chạy đúng |
| Cài đặt `OpenMP` | Người 1 | Người 2 kiểm tra | Bản OpenMP có `reduction` đúng |
| Cài đặt `MPI` | Người 2 | Người 1 kiểm tra | Bản MPI có `MPI_Reduce` đúng |
| Thiết lập hàm đo thời gian, sai số, speedup, efficiency | Người 1 | Người 2 góp ý và kiểm tra | Công thức và cách đo thống nhất |
| Thiết lập script benchmark | Người 2 | Người 1 góp ý | Script chạy nhiều cấu hình và lưu kết quả |
| Chạy benchmark với các cấu hình | Người 2 | Người 1 giám sát và đối chiếu | File CSV hoặc bảng dữ liệu thô |
| Kiểm tra độ đúng của các số liệu | Cả hai | Cả hai | Bộ số liệu đã rà soát |
| Vẽ bảng và biểu đồ | Người 2 | Người 1 kiểm tra | Biểu đồ time, speedup, efficiency, error |
| Viết cơ sở lý thuyết | Người 1 | Người 2 đọc soát | Chương lý thuyết hoàn chỉnh |
| Viết phân tích thiết kế song song | Người 1 | Người 2 đọc soát | Chương thuật toán và PCAM |
| Viết cài đặt chương trình | Chia theo phần phụ trách | Cả hai | Chương cài đặt |
| Viết kịch bản thực nghiệm | Người 2 | Người 1 đọc soát | Chương benchmark |
| Viết kết quả và đánh giá | Người 2 | Người 1 đọc soát | Chương số liệu và phân tích |
| Viết mở đầu và kết luận | Cả hai | Cả hai | Chương 1 và Chương 7 |
| Vẽ flowchart tuần tự | Người 1 | Người 2 góp ý | Sơ đồ tuần tự |
| Vẽ flowchart OpenMP | Người 1 | Người 2 góp ý | Sơ đồ OpenMP |
| Vẽ flowchart MPI | Người 2 | Người 1 góp ý | Sơ đồ MPI |
| Làm slide phần lý thuyết và OpenMP | Người 1 | Người 2 góp ý | Phần đầu slide |
| Làm slide phần MPI và thực nghiệm | Người 2 | Người 1 góp ý | Phần sau slide |
| Ghép slide cuối cùng và thống nhất phong cách | Cả hai | Cả hai | Bộ slide hoàn chỉnh |
| Tập thuyết trình và phản biện | Cả hai | Cả hai | Kịch bản bảo vệ |

---

## Phân rã đóng góp theo từng mảng

### 1. Mảng kỹ thuật

**Người 1** chịu trách nhiệm chính:

- Thiết kế hàm tính Pi tuần tự.
- Song song hóa bằng OpenMP.
- Giải thích lựa chọn `schedule(static)` là mặc định hợp lý cho workload gần đồng đều.
- Kiểm tra `reduction` và tránh `race condition`.

**Người 2** chịu trách nhiệm chính:

- Chia miền tính toán cho MPI.
- Tính tổng cục bộ trên mỗi process.
- Gộp kết quả bằng `MPI_Reduce`.
- Thiết kế cơ chế benchmark nhiều lần và lưu số liệu có hệ thống.

### 2. Mảng số liệu và đánh giá

**Người 1**:

- Kiểm tra logic tính `speedup`, `efficiency`, `error`.
- Đối chiếu tính đúng đắn giữa Serial, OpenMP và MPI.
- Góp ý nhận xét kỹ thuật cho từng bảng và biểu đồ.

**Người 2**:

- Trực tiếp chạy benchmark.
- Tổ chức bộ dữ liệu thô.
- Tổng hợp bảng kết quả.
- Vẽ biểu đồ và viết phần phân tích xu hướng hiệu năng.

### 3. Mảng báo cáo

**Người 1** phụ trách chính:

- Chương 2: Cơ sở lý thuyết.
- Chương 3: Phân tích và thiết kế thuật toán song song.
- Phần Serial/OpenMP trong Chương 4.

**Người 2** phụ trách chính:

- Phần MPI trong Chương 4.
- Chương 5: Kịch bản thực nghiệm.
- Chương 6: Kết quả thực nghiệm và đánh giá.

**Cả hai** cùng phụ trách:

- Chương 1: Giới thiệu đề tài.
- Chương 7: Kết luận và hướng phát triển.
- Chỉnh hình thức, trích dẫn, mục lục, bảng biểu.

### 4. Mảng slide và bảo vệ

**Người 1** phụ trách trình bày:

- Bối cảnh đề tài.
- Phương pháp tích phân số.
- Thiết kế thuật toán tuần tự và OpenMP.

**Người 2** phụ trách trình bày:

- MPI.
- Benchmark.
- Kết quả thực nghiệm và so sánh.
- Kết luận.

---

## Những đầu việc bắt buộc nhóm phải hoàn thành

Nhóm được xem là hoàn thành đúng định hướng nếu có đủ các đầu việc bắt buộc sau:

1. Chốt cấu trúc bài toán, aim, scope và tiêu chí hoàn thành.
2. Cài đặt đủ 3 phiên bản: `Serial`, `OpenMP`, `MPI`.
3. Bảo đảm các phiên bản cho kết quả gần đúng và sai số hợp lý.
4. Có cơ chế đo thời gian công bằng và nhất quán.
5. Chạy đủ các thí nghiệm chính:
   - ảnh hưởng của `N`,
   - strong scaling,
   - weak scaling,
   - so sánh OpenMP và MPI.
6. Có bảng và biểu đồ cho `time`, `speedup`, `efficiency`, `error`.
7. Có flowchart tuần tự, OpenMP và MPI.
8. Có báo cáo đầy đủ các chương theo cấu trúc đã thống nhất.
9. Có slide bảo vệ rõ ràng, nhất quán.
10. Có phân tích nguyên nhân của overhead, reduction cost và giới hạn phần cứng.

---

## Cách chứng minh đóng góp của từng người

Để khi người ngoài đọc vẫn thấy rõ đóng góp cá nhân, nhóm nên giữ lại các dấu vết công việc sau:

- Ghi rõ người phụ trách dưới từng chương báo cáo trong bản nội bộ.
- Lưu lịch sử chỉnh sửa file code và file báo cáo.
- Lưu các file benchmark, biểu đồ và bản nháp slide có tên người thực hiện.
- Khi bảo vệ, mỗi người trình bày đúng phần mình phụ trách kỹ thuật.
- Khi được hỏi, mỗi người phải giải thích được phần lõi của mình và hiểu được phần còn lại ở mức tổng quát.

---

## Kết luận phân công

Cách chia việc này nhằm bảo đảm:

- Cả 2 người đều có đóng góp kỹ thuật thực chất.
- Cả 2 người đều có đóng góp vào báo cáo và slide.
- Các phần quan trọng như code, số liệu và nhận xét đều có kiểm tra chéo.
- Khi nộp bài hoặc bảo vệ, nhóm có thể giải thích rõ ai làm gì mà vẫn thể hiện được tinh thần làm việc nhóm.
