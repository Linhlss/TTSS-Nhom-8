# Checklist nội bộ cho nhóm 2 người

## Lưu ý sử dụng

Tài liệu này chỉ dùng nội bộ để theo dõi tiến độ và kiểm soát chất lượng. Có thể thay:

- `Người 1` bằng tên thật thành viên thứ nhất.
- `Người 2` bằng tên thật thành viên thứ hai.

Nên cập nhật trạng thái hằng ngày hoặc sau mỗi buổi làm việc.

## Nguyên tắc tiến độ

- [x] Ưu tiên hoàn thành `code + kiểm thử + benchmark tối thiểu` trước.
- [x] Chỉ bắt đầu viết báo cáo chính thức khi 3 bản `Serial`, `OpenMP`, `MPI` đã chạy ổn định.
- [x] Chỉ khóa slide khi bảng số liệu và biểu đồ đã chốt.

---

## 0. Chốt định hướng chung

- [x] Cả nhóm thống nhất tên đề tài chính thức.
- [x] Cả nhóm thống nhất aim tổng thể.
- [x] Cả nhóm thống nhất scope trong phạm vi và ngoài phạm vi.
- [x] Cả nhóm thống nhất thuật toán chính là tích phân số theo quy tắc điểm giữa.
- [x] Cả nhóm thống nhất `Hybrid MPI + OpenMP` chỉ là phần mở rộng, không phải phần bắt buộc.
- [x] Cả nhóm thống nhất `OpenMP scheduling` không phải lõi chính; mặc định ưu tiên `schedule(static)`.
- [x] Cả nhóm thống nhất tiêu chí hoàn thành đề tài.

---

## 1. Thiết kế code và cấu trúc dự án

- [x] Người 1 chốt cấu trúc thư mục code.
- [ ] Người 1 chốt giao diện đầu vào: `N`, `mode`, `threads`, `processes`.
- [x] Người 1 chốt format output chung cho các phiên bản.
- [x] Người 1 và Người 2 thống nhất kiểu dữ liệu dùng cho biến đếm và biến tổng.
- [x] Người 1 và Người 2 thống nhất cách đo thời gian.
- [x] Người 2 chốt cách lưu kết quả benchmark ra file.
- [x] Cả nhóm thống nhất tên các file nguồn và script chạy.

---

## 2. Cài đặt phiên bản Serial

### Người 1 phụ trách chính

- [x] Viết bản `Serial`.
- [x] Kiểm tra công thức tích phân số theo quy tắc điểm giữa.
- [x] Kiểm tra kết quả Pi gần đúng với `N` nhỏ.
- [x] Kiểm tra kết quả Pi gần đúng với `N` lớn hơn.
- [x] Tách phần tính toán và phần in kết quả nếu cần.

### Người 2 kiểm tra chéo

- [x] Chạy thử bản `Serial`.
- [x] Đối chiếu công thức và kết quả.
- [x] Góp ý format output nếu chưa thống nhất.

---

## 3. Cài đặt phiên bản OpenMP

### Người 1 phụ trách chính

- [x] Viết bản `OpenMP`.
- [x] Dùng `reduction(+:sum)` đúng chỗ.
- [x] Kiểm tra không có `race condition`.
- [x] Thiết lập số thread linh hoạt.
- [x] Kiểm tra `schedule(static)` chạy đúng.
- [ ] Nếu có thử `dynamic/guided`, ghi rõ đó là phần tham khảo thêm chứ không phải trọng tâm.

### Người 2 kiểm tra chéo

- [x] Chạy thử OpenMP với `1, 2, 4, 8` thread.
- [x] Đối chiếu kết quả với `Serial`.
- [x] Kiểm tra thời gian có hợp lý khi tăng thread.

---

## 4. Cài đặt phiên bản MPI

### Người 2 phụ trách chính

- [x] Viết bản `MPI`.
- [x] Chia miền tính toán hoặc tập chỉ số cho các process.
- [x] Tính `local sum` trên từng process.
- [x] Dùng `MPI_Reduce` để gộp kết quả.
- [x] Chỉ cho `rank 0` in kết quả cuối.
- [x] Kiểm tra chạy đúng với `1, 2, 4, 8` process.

### Người 1 kiểm tra chéo

- [x] Chạy thử bản MPI.
- [x] Đối chiếu kết quả với `Serial`.
- [x] Kiểm tra logic reduction và output.

---

## 5. Hàm dùng chung và kiểm tra độ đúng

- [x] Có cách tính `Error = |pi_computed - pi_reference|`.
- [x] Có cách tính `Speedup = T1 / Tp`.
- [x] Có cách tính `Efficiency = Speedup / p`.
- [x] Cả nhóm thống nhất `T1` lấy từ đâu khi so sánh từng trường hợp.
- [x] Kiểm tra cả 3 phiên bản cho kết quả gần nhau.
- [x] Kiểm tra sai số thay đổi hợp lý khi `N` tăng; ghi rõ rounding error làm sai số không giảm đơn điệu tuyệt đối.
- [x] Kiểm tra không bị lỗi kiểu dữ liệu khi `N = 10^9`.

---

## 6. Thiết kế benchmark

### Người 2 phụ trách chính

- [x] Viết script benchmark.
- [x] Tạo file lưu kết quả dạng CSV hoặc bảng dữ liệu thô.
- [x] Thiết lập benchmark theo thay đổi `N`.
- [x] Thiết lập benchmark strong scaling.
- [x] Thiết lập benchmark weak scaling.
- [x] Thiết lập benchmark so sánh OpenMP và MPI.

### Cả nhóm cùng chốt quy tắc benchmark công bằng

- [x] Mỗi cấu hình chạy ít nhất 3 lần.
- [x] Quyết định lấy trung bình, trung vị hoặc giá trị tốt nhất.
- [x] Dùng cùng `N` khi so sánh trực tiếp giữa các phiên bản.
- [x] Dùng cùng mức compiler flags ở mức công bằng nhất có thể.
- [x] Không tính phần in màn hình vào thời gian thuật toán nếu tách được.
- [ ] Tắt hoặc hạn chế ứng dụng nền nặng khi chạy benchmark.
- [x] Ghi lại cấu hình máy thử nghiệm.

---

## 6.5. Mốc chặn trước khi viết báo cáo

- [x] Serial chạy đúng từ đầu đến cuối.
- [x] OpenMP chạy đúng với các mức thread chính.
- [x] MPI chạy đúng với các mức process chính.
- [x] Có ít nhất một file CSV benchmark dùng được.
- [x] Cả nhóm đã kiểm tra sơ bộ speedup, efficiency và sai số.
- [x] Đã chốt format output và cách tái chạy benchmark.

Chỉ khi hoàn thành hết mục này mới chuyển sang viết báo cáo chính thức và làm slide.

---

## 7. Chạy thực nghiệm

### Thí nghiệm 1: Ảnh hưởng của kích thước bài toán

- [x] Chạy với `N = 10^6`.
- [x] Chạy với `N = 10^7`.
- [x] Chạy với `N = 10^8`.
- [x] Nếu máy chịu được, chạy với `N = 10^9`.
- [x] Ghi thời gian và sai số cho từng cấu hình.

### Thí nghiệm 2: Strong scaling

- [x] Chọn `N` cố định đủ lớn.
- [x] Chạy `p = 1`.
- [x] Chạy `p = 2`.
- [x] Chạy `p = 4`.
- [x] Chạy `p = 8`.
- [ ] Nếu phần cứng phù hợp, chạy thêm `p = 12`.

### Thí nghiệm 3: Weak scaling

- [x] Chốt bộ `N` tăng theo `p`.
- [x] Chạy đủ các mức đã chốt.
- [x] Ghi rõ logic chọn `N = 10^7 × p`.

### Thí nghiệm 4: So sánh OpenMP và MPI

- [x] So sánh cùng `N` với `1 worker`.
- [x] So sánh cùng `N` với `2 worker`.
- [x] So sánh cùng `N` với `4 worker`.
- [x] So sánh cùng `N` với `8 worker`.
- [x] Kiểm tra dữ liệu có bất thường hay không.

---

## 8. Xử lý số liệu

### Người 2 phụ trách chính

- [x] Tổng hợp dữ liệu thô.
- [x] Tính lại `speedup`.
- [x] Tính lại `efficiency`.
- [x] Lập bảng `time`.
- [x] Lập bảng `speedup`.
- [x] Lập bảng `efficiency`.
- [x] Lập bảng `error`.
- [x] Vẽ biểu đồ `time`.
- [x] Vẽ biểu đồ `speedup`.
- [x] Vẽ biểu đồ `efficiency`.
- [x] Vẽ biểu đồ `error theo N`.

### Người 1 kiểm tra chéo

- [x] Soát công thức tính.
- [ ] Kiểm tra biểu đồ có phản ánh đúng dữ liệu thô không.
- [x] Đánh dấu các điểm bất thường cần giải thích.

---

## 9. Viết báo cáo

Chỉ mở phần này khi các mục từ `1` đến `8` đã đủ ổn định để không phải sửa lại cấu trúc báo cáo nhiều lần.

### Chương 1: Giới thiệu đề tài

- [ ] Cả nhóm viết chung phần bối cảnh học phần.
- [ ] Cả nhóm viết chung mục tiêu đề tài.
- [ ] Cả nhóm viết chung phạm vi thực hiện.
- [ ] Cả nhóm viết chung tiêu chí hoàn thành.

### Chương 2: Cơ sở lý thuyết

- [ ] Người 1 viết giới thiệu về số Pi.
- [ ] Người 1 viết công thức tích phân.
- [ ] Người 1 viết quy tắc điểm giữa.
- [ ] Người 2 đọc và soát tính rõ ràng.

### Chương 3: Phân tích và thiết kế thuật toán song song

- [ ] Người 1 viết thuật toán tuần tự.
- [ ] Người 1 viết OpenMP.
- [ ] Người 1 viết reduction và race condition.
- [ ] Người 1 viết PCAM.
- [ ] Người 2 góp ý phần MPI để chương không lệch.
- [ ] Người 2 kiểm tra phần nói về scheduling có đúng trọng tâm.

### Chương 4: Cài đặt chương trình

- [ ] Người 1 viết phần Serial.
- [ ] Người 1 viết phần OpenMP.
- [x] Người 2 viết phần MPI.
- [ ] Nếu có Hybrid, ghi rõ là mở rộng.
- [x] Cả nhóm thêm hướng dẫn biên dịch và chạy.

### Chương 5: Kịch bản thực nghiệm

- [x] Người 2 viết cấu hình máy thử nghiệm.
- [x] Người 2 viết bộ tham số benchmark.
- [x] Người 2 viết strong scaling.
- [x] Người 2 viết weak scaling.
- [x] Người 2 viết quy tắc benchmark công bằng.
- [ ] Người 1 soát độ nhất quán với phần code.

### Chương 6: Kết quả thực nghiệm và đánh giá

- [x] Người 2 chèn bảng số liệu.
- [x] Người 2 chèn biểu đồ.
- [x] Người 2 viết nhận xét OpenMP.
- [x] Người 2 viết nhận xét MPI.
- [x] Người 2 viết so sánh OpenMP và MPI.
- [ ] Người 1 bổ sung giải thích kỹ thuật cho các xu hướng quan trọng.

### Chương 7: Kết luận và hướng phát triển

- [ ] Cả nhóm viết phần kết quả đạt được.
- [ ] Cả nhóm viết phần hạn chế.
- [ ] Cả nhóm viết hướng phát triển.

### Hình thức báo cáo

- [ ] Có mục lục.
- [ ] Có đánh số hình và bảng.
- [ ] Có chú thích hình nếu cần.
- [ ] Có kiểm tra lỗi chính tả.
- [ ] Có thống nhất font, cỡ chữ, căn lề.

---

## 10. Vẽ sơ đồ và chuẩn bị hình minh họa

- [ ] Người 1 vẽ flowchart tuần tự.
- [ ] Người 1 vẽ flowchart OpenMP.
- [x] Người 2 vẽ flowchart MPI.
- [x] Người 2 vẽ hoặc hoàn thiện biểu đồ benchmark.
- [ ] Cả nhóm thống nhất phong cách hình ảnh.

---

## 11. Làm slide

Chỉ mở phần này sau khi:

- [x] Code đã ổn định.
- [x] Benchmark đã chốt.
- [x] Bảng số liệu và biểu đồ không còn thay đổi lớn.

### Người 1 phụ trách

- [ ] Slide bối cảnh và mục tiêu.
- [ ] Slide phương pháp tích phân số.
- [ ] Slide thuật toán tuần tự.
- [ ] Slide OpenMP.
- [ ] Slide reduction và race condition.

### Người 2 phụ trách

- [x] Slide MPI: nội dung nguồn đã chuẩn bị.
- [x] Slide benchmark setup: nội dung nguồn đã chuẩn bị.
- [x] Slide bảng số liệu chính: nội dung nguồn đã chuẩn bị.
- [x] Slide biểu đồ và so sánh: nội dung nguồn đã chuẩn bị.
- [x] Slide kết luận và hướng phát triển: nội dung nguồn đã chuẩn bị.

### Cả nhóm cùng làm

- [ ] Thống nhất template slide.
- [ ] Thống nhất màu sắc và cách trình bày.
- [ ] Cắt bớt chữ dài dòng.
- [ ] Kiểm tra slide không mâu thuẫn với báo cáo.

---

## 12. Chuẩn bị bảo vệ

- [x] Chia người nói từng phần.
- [ ] Người 1 tập nói phần lý thuyết và OpenMP.
- [ ] Người 2 tập nói phần MPI và thực nghiệm.
- [ ] Tập nói toàn bài ít nhất 2 lần.
- [ ] Đo thời gian thuyết trình.
- [x] Chuẩn bị câu trả lời cho câu hỏi: vì sao chọn tích phân số.
- [x] Chuẩn bị câu trả lời cho câu hỏi: vì sao không chọn Chudnovsky làm lõi chính.
- [x] Chuẩn bị câu trả lời cho câu hỏi: vì sao `schedule(static)` là hợp lý.
- [x] Chuẩn bị câu trả lời cho câu hỏi: vì sao speedup không tuyến tính.
- [x] Chuẩn bị câu trả lời cho câu hỏi: khác nhau giữa OpenMP và MPI.
- [x] Chuẩn bị câu trả lời cho câu hỏi: hạn chế của benchmark trên máy cá nhân.

---

## 13. Kiểm tra cuối trước khi nộp

- [ ] Code chạy được lại từ đầu.
- [x] Các lệnh biên dịch đã được ghi rõ.
- [ ] Báo cáo và slide thống nhất số liệu.
- [x] Các bảng và biểu đồ không sai đơn vị.
- [ ] Không còn chỗ ghi chú tạm hoặc nội dung chưa hoàn thiện.
- [ ] File nộp đã đặt tên gọn và rõ.
- [ ] Cả hai thành viên đều đọc lại bản cuối.

---

## 14. Ghi chú nội bộ

- [x] Nếu có số liệu bất thường, không xóa ngay; lưu lại và giải thích nguyên nhân nếu cần.
- [x] Nếu không kịp Hybrid, bỏ hẳn hoặc chỉ ghi ở hướng phát triển.
- [x] Không sa đà vào app, web, GUI hoặc tối ưu ngoài phạm vi môn học.
- [x] Ưu tiên hoàn thành chắc 3 bản `Serial`, `OpenMP`, `MPI` trước khi làm phần mở rộng.
