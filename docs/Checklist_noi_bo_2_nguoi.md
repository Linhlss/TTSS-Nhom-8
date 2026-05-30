# Checklist nội bộ cho nhóm 2 người

## Lưu ý sử dụng

Tài liệu này chỉ dùng nội bộ để theo dõi tiến độ và kiểm soát chất lượng. Có thể thay:

- `Người 1` bằng tên thật thành viên thứ nhất.
- `Người 2` bằng tên thật thành viên thứ hai.

Nên cập nhật trạng thái hằng ngày hoặc sau mỗi buổi làm việc.

---

## 0. Chốt định hướng chung

- [ ] Cả nhóm thống nhất tên đề tài chính thức.
- [ ] Cả nhóm thống nhất aim tổng thể.
- [ ] Cả nhóm thống nhất scope trong phạm vi và ngoài phạm vi.
- [ ] Cả nhóm thống nhất thuật toán chính là tích phân số theo quy tắc điểm giữa.
- [ ] Cả nhóm thống nhất `Hybrid MPI + OpenMP` chỉ là phần mở rộng, không phải phần bắt buộc.
- [ ] Cả nhóm thống nhất `OpenMP scheduling` không phải lõi chính; mặc định ưu tiên `schedule(static)`.
- [ ] Cả nhóm thống nhất tiêu chí hoàn thành đề tài.

---

## 1. Thiết kế code và cấu trúc dự án

- [ ] Người 1 chốt cấu trúc thư mục code.
- [ ] Người 1 chốt giao diện đầu vào: `N`, `mode`, `threads`, `processes`.
- [ ] Người 1 chốt format output chung cho các phiên bản.
- [ ] Người 1 và Người 2 thống nhất kiểu dữ liệu dùng cho biến đếm và biến tổng.
- [ ] Người 1 và Người 2 thống nhất cách đo thời gian.
- [ ] Người 2 chốt cách lưu kết quả benchmark ra file.
- [ ] Cả nhóm thống nhất tên các file nguồn và script chạy.

---

## 2. Cài đặt phiên bản Serial

### Người 1 phụ trách chính

- [ ] Viết bản `Serial`.
- [ ] Kiểm tra công thức tích phân số theo quy tắc điểm giữa.
- [ ] Kiểm tra kết quả Pi gần đúng với `N` nhỏ.
- [ ] Kiểm tra kết quả Pi gần đúng với `N` lớn hơn.
- [ ] Tách phần tính toán và phần in kết quả nếu cần.

### Người 2 kiểm tra chéo

- [ ] Chạy thử bản `Serial`.
- [ ] Đối chiếu công thức và kết quả.
- [ ] Góp ý format output nếu chưa thống nhất.

---

## 3. Cài đặt phiên bản OpenMP

### Người 1 phụ trách chính

- [ ] Viết bản `OpenMP`.
- [ ] Dùng `reduction(+:sum)` đúng chỗ.
- [ ] Kiểm tra không có `race condition`.
- [ ] Thiết lập số thread linh hoạt.
- [ ] Kiểm tra `schedule(static)` chạy đúng.
- [ ] Nếu có thử `dynamic/guided`, ghi rõ đó là phần tham khảo thêm chứ không phải trọng tâm.

### Người 2 kiểm tra chéo

- [ ] Chạy thử OpenMP với `1, 2, 4, 8` thread.
- [ ] Đối chiếu kết quả với `Serial`.
- [ ] Kiểm tra thời gian có hợp lý khi tăng thread.

---

## 4. Cài đặt phiên bản MPI

### Người 2 phụ trách chính

- [ ] Viết bản `MPI`.
- [ ] Chia miền tính toán hoặc tập chỉ số cho các process.
- [ ] Tính `local sum` trên từng process.
- [ ] Dùng `MPI_Reduce` để gộp kết quả.
- [ ] Chỉ cho `rank 0` in kết quả cuối.
- [ ] Kiểm tra chạy đúng với `1, 2, 4, 8` process.

### Người 1 kiểm tra chéo

- [ ] Chạy thử bản MPI.
- [ ] Đối chiếu kết quả với `Serial`.
- [ ] Kiểm tra logic reduction và output.

---

## 5. Hàm dùng chung và kiểm tra độ đúng

- [ ] Có cách tính `Error = |pi_computed - pi_reference|`.
- [ ] Có cách tính `Speedup = T1 / Tp`.
- [ ] Có cách tính `Efficiency = Speedup / p`.
- [ ] Cả nhóm thống nhất `T1` lấy từ đâu khi so sánh từng trường hợp.
- [ ] Kiểm tra cả 3 phiên bản cho kết quả gần nhau.
- [ ] Kiểm tra sai số giảm hợp lý khi `N` tăng.
- [ ] Kiểm tra không bị lỗi kiểu dữ liệu khi `N` lớn.

---

## 6. Thiết kế benchmark

### Người 2 phụ trách chính

- [ ] Viết script benchmark.
- [ ] Tạo file lưu kết quả dạng CSV hoặc bảng dữ liệu thô.
- [ ] Thiết lập benchmark theo thay đổi `N`.
- [ ] Thiết lập benchmark strong scaling.
- [ ] Thiết lập benchmark weak scaling.
- [ ] Thiết lập benchmark so sánh OpenMP và MPI.

### Cả nhóm cùng chốt quy tắc benchmark công bằng

- [ ] Mỗi cấu hình chạy ít nhất 3 lần.
- [ ] Quyết định lấy trung bình, trung vị hoặc giá trị tốt nhất.
- [ ] Dùng cùng `N` khi so sánh trực tiếp giữa các phiên bản.
- [ ] Dùng cùng mức compiler flags ở mức công bằng nhất có thể.
- [ ] Không tính phần in màn hình vào thời gian thuật toán nếu tách được.
- [ ] Tắt hoặc hạn chế ứng dụng nền nặng khi chạy benchmark.
- [ ] Ghi lại cấu hình máy thử nghiệm.

---

## 7. Chạy thực nghiệm

### Thí nghiệm 1: Ảnh hưởng của kích thước bài toán

- [ ] Chạy với `N = 10^6`.
- [ ] Chạy với `N = 10^7`.
- [ ] Chạy với `N = 10^8`.
- [ ] Nếu máy chịu được, chạy với `N = 10^9`.
- [ ] Ghi thời gian và sai số cho từng cấu hình.

### Thí nghiệm 2: Strong scaling

- [ ] Chọn `N` cố định đủ lớn.
- [ ] Chạy `p = 1`.
- [ ] Chạy `p = 2`.
- [ ] Chạy `p = 4`.
- [ ] Chạy `p = 8`.
- [ ] Nếu phần cứng phù hợp, chạy thêm `p = 12`.

### Thí nghiệm 3: Weak scaling

- [ ] Chốt bộ `N` tăng theo `p`.
- [ ] Chạy đủ các mức đã chốt.
- [ ] Ghi rõ logic chọn `N` tương ứng với `p`.

### Thí nghiệm 4: So sánh OpenMP và MPI

- [ ] So sánh cùng `N` với `1 worker`.
- [ ] So sánh cùng `N` với `2 worker`.
- [ ] So sánh cùng `N` với `4 worker`.
- [ ] So sánh cùng `N` với `8 worker`.
- [ ] Kiểm tra dữ liệu có bất thường hay không.

---

## 8. Xử lý số liệu

### Người 2 phụ trách chính

- [ ] Tổng hợp dữ liệu thô.
- [ ] Tính lại `speedup`.
- [ ] Tính lại `efficiency`.
- [ ] Lập bảng `time`.
- [ ] Lập bảng `speedup`.
- [ ] Lập bảng `efficiency`.
- [ ] Lập bảng `error`.
- [ ] Vẽ biểu đồ `time`.
- [ ] Vẽ biểu đồ `speedup`.
- [ ] Vẽ biểu đồ `efficiency`.
- [ ] Vẽ biểu đồ `error theo N`.

### Người 1 kiểm tra chéo

- [ ] Soát công thức tính.
- [ ] Kiểm tra biểu đồ có phản ánh đúng dữ liệu thô không.
- [ ] Đánh dấu các điểm bất thường cần giải thích.

---

## 9. Viết báo cáo

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
- [ ] Người 2 viết phần MPI.
- [ ] Nếu có Hybrid, ghi rõ là mở rộng.
- [ ] Cả nhóm thêm hướng dẫn biên dịch và chạy.

### Chương 5: Kịch bản thực nghiệm

- [ ] Người 2 viết cấu hình máy thử nghiệm.
- [ ] Người 2 viết bộ tham số benchmark.
- [ ] Người 2 viết strong scaling.
- [ ] Người 2 viết weak scaling.
- [ ] Người 2 viết quy tắc benchmark công bằng.
- [ ] Người 1 soát độ nhất quán với phần code.

### Chương 6: Kết quả thực nghiệm và đánh giá

- [ ] Người 2 chèn bảng số liệu.
- [ ] Người 2 chèn biểu đồ.
- [ ] Người 2 viết nhận xét OpenMP.
- [ ] Người 2 viết nhận xét MPI.
- [ ] Người 2 viết so sánh OpenMP và MPI.
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
- [ ] Người 2 vẽ flowchart MPI.
- [ ] Người 2 vẽ hoặc hoàn thiện biểu đồ benchmark.
- [ ] Cả nhóm thống nhất phong cách hình ảnh.

---

## 11. Làm slide

### Người 1 phụ trách

- [ ] Slide bối cảnh và mục tiêu.
- [ ] Slide phương pháp tích phân số.
- [ ] Slide thuật toán tuần tự.
- [ ] Slide OpenMP.
- [ ] Slide reduction và race condition.

### Người 2 phụ trách

- [ ] Slide MPI.
- [ ] Slide benchmark setup.
- [ ] Slide bảng số liệu chính.
- [ ] Slide biểu đồ và so sánh.
- [ ] Slide kết luận và hướng phát triển.

### Cả nhóm cùng làm

- [ ] Thống nhất template slide.
- [ ] Thống nhất màu sắc và cách trình bày.
- [ ] Cắt bớt chữ dài dòng.
- [ ] Kiểm tra slide không mâu thuẫn với báo cáo.

---

## 12. Chuẩn bị bảo vệ

- [ ] Chia người nói từng phần.
- [ ] Người 1 tập nói phần lý thuyết và OpenMP.
- [ ] Người 2 tập nói phần MPI và thực nghiệm.
- [ ] Tập nói toàn bài ít nhất 2 lần.
- [ ] Đo thời gian thuyết trình.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: vì sao chọn tích phân số.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: vì sao không chọn Chudnovsky làm lõi chính.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: vì sao `schedule(static)` là hợp lý.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: vì sao speedup không tuyến tính.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: khác nhau giữa OpenMP và MPI.
- [ ] Chuẩn bị câu trả lời cho câu hỏi: hạn chế của benchmark trên máy cá nhân.

---

## 13. Kiểm tra cuối trước khi nộp

- [ ] Code chạy được lại từ đầu.
- [ ] Các lệnh biên dịch đã được ghi rõ.
- [ ] Báo cáo và slide thống nhất số liệu.
- [ ] Các bảng và biểu đồ không sai đơn vị.
- [ ] Không còn chỗ ghi chú tạm hoặc nội dung chưa hoàn thiện.
- [ ] File nộp đã đặt tên gọn và rõ.
- [ ] Cả hai thành viên đều đọc lại bản cuối.

---

## 14. Ghi chú nội bộ

- [ ] Nếu có số liệu bất thường, không xóa ngay; lưu lại và giải thích nguyên nhân nếu cần.
- [ ] Nếu không kịp Hybrid, bỏ hẳn hoặc chỉ ghi ở hướng phát triển.
- [ ] Không sa đà vào app, web, GUI hoặc tối ưu ngoài phạm vi môn học.
- [ ] Ưu tiên hoàn thành chắc 3 bản `Serial`, `OpenMP`, `MPI` trước khi làm phần mở rộng.
