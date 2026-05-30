# README - Định hướng xây dựng báo cáo

## Tên đề tài

**Xây dựng và đánh giá chương trình song song tính số Pi bằng phương pháp tích phân số sử dụng OpenMP và MPI**

---

## 1. Mục đích của README này

Tài liệu này dùng để định hướng cách xây dựng báo cáo cho đề tài môn **MI4364 - Tính toán song song**.

Báo cáo cần đi đúng trọng tâm của học phần: **thiết kế, cài đặt và đánh giá chương trình song song**. Bài toán tính số Pi chỉ đóng vai trò là bài toán minh họa để thể hiện các nội dung như phân rã dữ liệu, reduction, OpenMP, MPI, speedup, efficiency và khả năng mở rộng.

Báo cáo **không nên** đi theo hướng xây dựng app, web, giao diện người dùng, hoặc tính số Pi với số lượng chữ số cực lớn bằng các thuật toán số học độ chính xác cao.

---

## 2. Định hướng tổng thể của báo cáo

Báo cáo nên trả lời rõ các câu hỏi sau:

```text
1. Vì sao bài toán tính Pi phù hợp với tính toán song song?
2. Thuật toán tính Pi được chọn là gì?
3. Bài toán được phân rã như thế nào?
4. Phiên bản tuần tự hoạt động ra sao?
5. Phiên bản OpenMP song song hóa như thế nào?
6. Phiên bản MPI song song hóa như thế nào?
7. Reduction được dùng để tổng hợp kết quả ra sao?
8. Chương trình được đánh giá bằng những chỉ số nào?
9. Khi tăng số thread/process thì hiệu năng thay đổi như thế nào?
10. Kết quả thực nghiệm cho thấy điều gì?
```

Trọng tâm của báo cáo không phải là việc tính ra giá trị Pi, mà là **phân tích quá trình song song hóa và đánh giá hiệu năng chương trình song song**.

---

## 3. Khác biệt so với báo cáo mẫu

Báo cáo mẫu trước đó có hai phần chính:

```text
1. Tích vô hướng của hai vector
2. Chương trình song song tính số Pi
```

Tuy nhiên, đề tài năm nay của nhóm **không trình bày riêng phần tích vô hướng hai vector**. Vì vậy, không nên sao chép nguyên cấu trúc mục lục của báo cáo mẫu.

Báo cáo năm nay nên tập trung hoàn toàn vào một tuyến nội dung duy nhất:

```text
Tính số Pi bằng phương pháp tích phân số
→ Thiết kế thuật toán tuần tự
→ Song song hóa bằng OpenMP
→ Song song hóa bằng MPI
→ Thực nghiệm
→ Đánh giá hiệu năng
```

Do đó, cấu trúc báo cáo nên được tổ chức lại thành các chương độc lập, thay vì chia thành “Phần 1 - Tích vô hướng” và “Phần 2 - Tính Pi”.

---

## 4. Cấu trúc báo cáo tổng quát

Báo cáo nên gồm các phần chính sau:

```text
Trang bìa
Lời cảm ơn
Mục lục
Danh mục hình ảnh, bảng biểu nếu có

Chương 1. Giới thiệu đề tài
Chương 2. Cơ sở lý thuyết
Chương 3. Phân tích và thiết kế thuật toán song song
Chương 4. Cài đặt chương trình
Chương 5. Kịch bản thực nghiệm
Chương 6. Kết quả thực nghiệm và đánh giá
Chương 7. Kết luận và hướng phát triển

Phụ lục
```

Đây là cấu trúc phù hợp hơn với đề tài hiện tại, vì toàn bộ báo cáo xoay quanh một bài toán chính là **tính gần đúng số Pi bằng phương pháp tích phân số và đánh giá hiệu quả song song hóa**.

---

## 5. Mục lục chi tiết đề xuất

### Chương 1. Giới thiệu đề tài

```text
1.1. Bối cảnh học phần Tính toán song song
1.2. Lý do chọn bài toán tính số Pi
1.3. Mục tiêu của đề tài
1.4. Phạm vi thực hiện
1.5. Sản phẩm đầu ra
1.6. Tiêu chí hoàn thành đề tài
1.7. Cấu trúc báo cáo
```

#### Nội dung cần trình bày

Chương này cần làm rõ đề tài được đặt trong bối cảnh học phần **Tính toán song song**, không phải trong bối cảnh phát triển phần mềm ứng dụng.

Ở mục **1.3. Mục tiêu của đề tài**, nên viết rõ:

```text
Mục tiêu của đề tài là xây dựng và đánh giá chương trình song song tính gần đúng số Pi bằng phương pháp tích phân số. Đề tài tập trung vào việc áp dụng các mô hình lập trình song song chia sẻ bộ nhớ và truyền thông điệp, cụ thể là OpenMP và MPI, để phân rã miền tính toán, xử lý cộng dồn kết quả bằng reduction, đo lường thời gian thực thi, speedup, efficiency và khả năng mở rộng của chương trình khi thay đổi số luồng, số tiến trình và kích thước bài toán.
```

Ở mục **1.4. Phạm vi thực hiện**, cần nói rõ:

```text
Trong phạm vi:
- Cài đặt phiên bản tuần tự.
- Cài đặt phiên bản OpenMP.
- Cài đặt phiên bản MPI.
- Có thể cài đặt thêm phiên bản Hybrid MPI + OpenMP nếu đủ thời gian.
- Đo thời gian chạy, speedup, efficiency và sai số.
- Đánh giá strong scaling, weak scaling và so sánh OpenMP với MPI.

Ngoài phạm vi:
- Không xây dựng giao diện web/app.
- Không tập trung vào tính Pi nhiều chữ số bằng Chudnovsky/GMP.
- Không tối ưu sâu ở mức GPU/CUDA, SIMD thủ công hoặc cache blocking phức tạp.
```

Ở mục **1.6. Tiêu chí hoàn thành đề tài**, nên bổ sung rõ các tiêu chí tối thiểu để nhóm tự kiểm tra mức độ hoàn thành:

```text
- Có ít nhất 3 phiên bản chương trình: Serial, OpenMP, MPI.
- Các phiên bản cho ra giá trị Pi gần đúng và sai số hợp lý.
- Có bảng so sánh thời gian chạy giữa các phiên bản.
- Có tính speedup và efficiency.
- Có nhận xét vì sao speedup không tuyến tính hoàn toàn.
- Có phân tích sự khác nhau giữa OpenMP và MPI.
- Có liên hệ với các khái niệm trong học phần: decomposition, reduction, shared memory, message passing, scalability.
```

---

### Chương 2. Cơ sở lý thuyết

```text
2.1. Giới thiệu về số Pi
2.2. Một số phương pháp tính số Pi
2.3. Lựa chọn phương pháp tích phân số
2.4. Công thức tích phân tính Pi
2.5. Quy tắc điểm giữa
2.6. Sai số xấp xỉ
2.7. Khả năng song song hóa của bài toán
```

#### Nội dung cần trình bày

Chương này giải thích nền tảng toán học và lý do chọn phương pháp tính Pi.

Công thức chính:

```text
π = ∫[0,1] 4 / (1 + x²) dx
```

Ý tưởng tính gần đúng:

```text
1. Chia đoạn [0, 1] thành N khoảng nhỏ.
2. Với mỗi khoảng, lấy điểm giữa x_i.
3. Tính f(x_i) = 4 / (1 + x_i²).
4. Cộng tất cả các giá trị f(x_i).
5. Nhân với độ rộng mỗi khoảng để thu được giá trị gần đúng của Pi.
```

Mục **2.7. Khả năng song song hóa của bài toán** rất quan trọng. Cần nhấn mạnh rằng mỗi khoảng con trong tích phân có thể được tính độc lập, nên bài toán phù hợp với phân rã dữ liệu và reduction.

---

### Chương 3. Phân tích và thiết kế thuật toán song song

```text
3.1. Thuật toán tuần tự
3.2. Phân rã dữ liệu
3.3. Thiết kế thuật toán OpenMP
3.4. Thiết kế thuật toán MPI
3.5. Thiết kế Hybrid MPI + OpenMP nếu có
3.6. Kỹ thuật reduction và race condition
3.7. Phân tích theo mô hình PCAM
3.8. So sánh các phiên bản thuật toán
```

#### Nội dung cần trình bày

Đây là chương trọng tâm của báo cáo.

Cần giải thích:

```text
- Bản tuần tự duyệt toàn bộ N khoảng trên một luồng.
- Bản OpenMP chia vòng lặp cho nhiều thread.
- Bản MPI chia tập chỉ số cho nhiều process.
- Mỗi thread/process tính tổng cục bộ.
- Các tổng cục bộ được gộp lại bằng reduction.
```

Với phần **3.3. Thiết kế thuật toán OpenMP**, nên nói rõ thêm rằng với bài toán tích phân số theo quy tắc điểm giữa, khối lượng tính toán của mỗi vòng lặp gần như đồng đều. Vì vậy, `schedule(static)` thường là lựa chọn mặc định hợp lý; các chiến lược `dynamic` hoặc `guided` có thể được nhắc đến như phần mở rộng hoặc so sánh thêm, nhưng không phải lõi chính của đề tài.

#### 3.6. Reduction và race condition

Cần trình bày vấn đề:

```text
Nếu nhiều thread cùng cập nhật trực tiếp một biến sum chung,
chương trình có thể xảy ra race condition và cho kết quả sai.
```

Cách xử lý:

```text
- Với OpenMP: dùng reduction(+:sum).
- Với MPI: dùng MPI_Reduce để cộng các tổng cục bộ.
```

#### 3.7. Phân tích theo mô hình PCAM

Nên đưa mô hình PCAM vào để báo cáo bám sát tư duy thiết kế thuật toán song song.

```text
Partitioning:
- Chia N khoảng tích phân thành các phần nhỏ.

Communication:
- OpenMP dùng shared memory, giao tiếp ẩn qua bộ nhớ chung.
- MPI cần tổng hợp kết quả bằng truyền thông điệp, cụ thể là MPI_Reduce.

Agglomeration:
- Gom nhiều khoảng nhỏ thành block cho từng thread/process để giảm overhead.

Mapping:
- Ánh xạ các block tính toán lên thread trong OpenMP hoặc process trong MPI.
```

---

### Chương 4. Cài đặt chương trình

```text
4.1. Môi trường cài đặt
4.2. Cấu trúc thư mục chương trình
4.3. Các tham số đầu vào
4.4. Cài đặt phiên bản tuần tự
4.5. Cài đặt phiên bản OpenMP
4.6. Cài đặt phiên bản MPI
4.7. Cài đặt phiên bản Hybrid nếu có
4.8. Hàm đo thời gian
4.9. Hàm tính speedup, efficiency và sai số
4.10. Hướng dẫn biên dịch và chạy
```

#### Nội dung cần trình bày

Chương này giải thích phần code và cách chạy chương trình.

Cấu trúc chương trình có thể tổ chức như sau:

```text
pi-parallel/
│
├── README.md
├── src/
│   ├── pi_serial.cpp
│   ├── pi_openmp.cpp
│   ├── pi_mpi.cpp
│   └── pi_hybrid.cpp
│
├── scripts/
│   ├── run_openmp.sh
│   ├── run_mpi.sh
│   └── benchmark.sh
│
├── results/
│   ├── openmp_results.csv
│   ├── mpi_results.csv
│   └── hybrid_results.csv
│
└── report/
    ├── figures/
    └── tables/
```

Nếu muốn làm đơn giản hơn, có thể gom các chế độ vào một file `main.cpp`, nhưng vẫn nên tách rõ các hàm:

```text
compute_pi_serial()
compute_pi_openmp()
compute_pi_mpi()
measure_time()
compute_speedup()
compute_efficiency()
compute_error()
```

#### Tham số đầu vào nên có

```text
- N: số khoảng chia.
- mode: serial, openmp, mpi hoặc hybrid.
- threads: số thread với OpenMP.
- processes: số process với MPI.
```

Ví dụ đầu ra mong muốn:

```text
Algorithm: Numerical Integration - Midpoint Rule
Mode: OpenMP
N: 1000000000
Threads: 8
Pi: 3.141592653589793
Error: 0.000000000000001
Time: 1.82 seconds
Speedup: 5.47x
Efficiency: 68.4%
```

Ngoài code và bảng kết quả, báo cáo nên có tối thiểu các sơ đồ thuật toán sau:

```text
- Sơ đồ thuật toán tuần tự.
- Sơ đồ OpenMP: chia N khoảng cho nhiều thread, local sum, reduction.
- Sơ đồ MPI: chia N khoảng cho nhiều process, local sum, MPI_Reduce về rank 0.
```

---

### Chương 5. Kịch bản thực nghiệm

```text
5.1. Mục tiêu thực nghiệm
5.2. Cấu hình máy thử nghiệm
5.3. Công cụ và môi trường chạy
5.4. Bộ tham số thực nghiệm
5.5. Thí nghiệm thay đổi kích thước N
5.6. Thí nghiệm strong scaling
5.7. Thí nghiệm weak scaling
5.8. Thí nghiệm so sánh OpenMP và MPI
5.9. Quy tắc đo thời gian công bằng
5.10. Các chỉ số đánh giá
```

#### Nội dung cần trình bày

Chương này mô tả cách benchmark.

Không nên chỉ chạy một lần rồi kết luận. Nên chạy nhiều cấu hình khác nhau để thấy được xu hướng hiệu năng.

Ở mục **5.9. Quy tắc đo thời gian công bằng**, nên mô tả cụ thể hơn:

```text
- Mỗi cấu hình nên chạy nhiều lần, ví dụ 3 đến 5 lần.
- Nêu rõ lấy giá trị trung bình, trung vị hoặc giá trị tốt nhất, và áp dụng nhất quán.
- Không tính thời gian in kết quả ra màn hình vào thời gian thuật toán nếu có thể tách riêng.
- Với MPI, chỉ process rank 0 nên in kết quả cuối cùng.
- Dùng cùng compiler flags khi so sánh Serial, OpenMP và MPI ở mức tối đa có thể công bằng.
- Dùng cùng giá trị N khi so sánh trực tiếp giữa các phiên bản.
- Hạn chế chạy các ứng dụng nặng khác trong lúc benchmark.
```

Có thể bổ sung thêm một tiểu mục ngắn về **rủi ro kỹ thuật và đe dọa đến tính hợp lệ của benchmark**, ví dụ:

```text
- Nếu N quá nhỏ, overhead song song hóa có thể lớn hơn lợi ích.
- Nếu N quá lớn, chương trình có thể chạy rất lâu; cần chú ý kiểu dữ liệu cho biến đếm.
- Với kiểu double, sai số không giảm mãi khi N tăng do giới hạn dấu chấm động.
- MPI chạy trên một máy cá nhân chưa phản ánh đầy đủ môi trường cluster thật.
- Số thread vượt quá số lõi logic hợp lý có thể làm hiệu năng giảm.
```

#### Thí nghiệm 1: Ảnh hưởng của kích thước N

```text
Giữ số thread/process cố định, thay đổi N:

N = 10^6
N = 10^7
N = 10^8
N = 10^9
```

Mục tiêu:

```text
- Quan sát khi N tăng thì sai số thay đổi thế nào.
- Quan sát khi N lớn thì song song hóa có hiệu quả hơn không.
```

#### Thí nghiệm 2: Strong scaling

```text
Giữ nguyên N, tăng số thread/process:

N = 10^8 hoặc 10^9
p = 1, 2, 4, 8, 12
```

Mục tiêu:

```text
- Đánh giá khi tăng tài nguyên tính toán thì thời gian giảm bao nhiêu.
- Tính speedup và efficiency.
```

#### Thí nghiệm 3: Weak scaling

```text
Tăng N tương ứng với số thread/process:

p = 1  -> N = 10^7
p = 2  -> N = 2 × 10^7
p = 4  -> N = 4 × 10^7
p = 8  -> N = 8 × 10^7
```

Mục tiêu:

```text
- Đánh giá khả năng xử lý bài toán lớn hơn khi tăng tài nguyên.
- Quan sát overhead và chi phí reduction.
```

#### Thí nghiệm 4: So sánh OpenMP và MPI

```text
OpenMP: 1, 2, 4, 8 threads
MPI:    1, 2, 4, 8 processes
```

Mục tiêu:

```text
- So sánh mô hình chia sẻ bộ nhớ và mô hình truyền thông điệp.
- Nhận xét sự khác biệt về overhead, reduction và khả năng mở rộng.
```

---

### Chương 6. Kết quả thực nghiệm và đánh giá

```text
6.1. Kiểm tra độ chính xác
6.2. Ảnh hưởng của N đến sai số và thời gian chạy
6.3. Kết quả OpenMP
6.4. Kết quả MPI
6.5. Kết quả Hybrid nếu có
6.6. So sánh OpenMP và MPI
6.7. Phân tích speedup và efficiency
6.8. Phân tích overhead, reduction cost và communication cost
6.9. Nhận xét tổng hợp
```

#### Nội dung cần trình bày

Chương này trình bày bảng số liệu, biểu đồ và nhận xét.

Cần tránh kiểu trình bày chỉ có:

```text
Pi = 3.14159
```

Thay vào đó, phải có phân tích hiệu năng.

#### Các bảng nên có

```text
Bảng 1. Sai số theo kích thước N
Bảng 2. Thời gian chạy Serial, OpenMP, MPI
Bảng 3. Speedup và Efficiency của OpenMP
Bảng 4. Speedup và Efficiency của MPI
Bảng 5. So sánh OpenMP và MPI cùng số worker
```

#### Các biểu đồ nên có

```text
Hình 1. Time theo số thread/process
Hình 2. Speedup theo số thread/process
Hình 3. Efficiency theo số thread/process
Hình 4. Sai số theo N
```

#### Các nhận xét cần có

```text
- Khi tăng số thread/process, thời gian có xu hướng giảm.
- Speedup không tuyến tính hoàn toàn do overhead, chi phí reduction và giới hạn phần cứng.
- Efficiency thường giảm khi số thread/process tăng.
- OpenMP thường có overhead thấp hơn khi chạy trên cùng một máy chia sẻ bộ nhớ.
- MPI thể hiện rõ mô hình truyền thông điệp, nhưng có thêm chi phí giao tiếp.
- Với N nhỏ, overhead có thể lớn hơn lợi ích song song hóa.
- Với N lớn, chương trình song song có cơ hội thể hiện hiệu quả rõ hơn.
```

---

### Chương 7. Kết luận và hướng phát triển

```text
7.1. Kết quả đạt được
7.2. Mức độ đáp ứng mục tiêu đề tài
7.3. Hạn chế
7.4. Hướng phát triển
```

#### 7.1. Kết quả đạt được

Nên viết rõ nhóm đã đạt được:

```text
- Xây dựng được chương trình tính gần đúng số Pi bằng phương pháp tích phân số.
- Cài đặt được phiên bản tuần tự làm baseline.
- Cài đặt được phiên bản OpenMP theo mô hình chia sẻ bộ nhớ.
- Cài đặt được phiên bản MPI theo mô hình truyền thông điệp.
- Đánh giá được thời gian chạy, speedup, efficiency và sai số.
- Thực hiện được một số kịch bản thực nghiệm để đánh giá khả năng mở rộng.
```

#### 7.2. Mức độ đáp ứng mục tiêu đề tài

Cần liên hệ lại với aim ban đầu:

```text
Đề tài đã đáp ứng mục tiêu chính là sử dụng bài toán tính Pi để minh họa quá trình thiết kế, cài đặt và đánh giá chương trình song song. Trọng tâm của đề tài không nằm ở việc tính Pi với số chữ số cực lớn, mà nằm ở việc phân rã bài toán, ánh xạ công việc lên nhiều thread/process, tổng hợp kết quả bằng reduction và phân tích hiệu năng dựa trên các chỉ số speedup, efficiency.
```

#### 7.3. Hạn chế

Có thể nêu:

```text
- Nếu chỉ chạy trên một máy cá nhân, kết quả MPI chưa phản ánh đầy đủ môi trường cluster thật.
- Chưa tối ưu sâu về cache, SIMD hoặc vectorization.
- Chưa triển khai GPU/CUDA.
- Chưa triển khai các thuật toán tính Pi độ chính xác cao như Chudnovsky.
- Số lượng cấu hình thử nghiệm còn phụ thuộc vào phần cứng hiện có.
```

#### 7.4. Hướng phát triển

Có thể đề xuất:

```text
- Triển khai Hybrid MPI + OpenMP đầy đủ hơn.
- Chạy thử trên cluster nhiều máy vật lý.
- So sánh thêm với CUDA/GPU.
- Thử nghiệm các chiến lược scheduling khác nhau trong OpenMP.
- So sánh với các phương pháp tính Pi khác như Monte Carlo hoặc Chudnovsky.
- Tối ưu thêm ở mức SIMD hoặc vectorization.
```

---

## 6. Các chỉ số đánh giá bắt buộc nên có

### 6.1. Thời gian chạy

```text
T_p = thời gian chạy với p thread/process
```

### 6.2. Speedup

```text
Speedup = T_1 / T_p
```

Trong đó:

```text
T_1: thời gian chạy tuần tự hoặc chạy với 1 worker.
T_p: thời gian chạy với p thread/process.
```

### 6.3. Efficiency

```text
Efficiency = Speedup / p
```

Nếu biểu diễn theo phần trăm:

```text
Efficiency (%) = (Speedup / p) × 100
```

### 6.4. Sai số

```text
Error = |pi_computed - pi_reference|
```

Mục tiêu không phải đạt sai số nhỏ nhất tuyệt đối, mà là đảm bảo kết quả hợp lý và quan sát xu hướng khi tăng N.

---

## 7. Những điểm cần nhấn mạnh trong báo cáo

Báo cáo cần nhấn mạnh các ý sau:

```text
1. Bài toán tính Pi bằng tích phân số có khả năng song song hóa tự nhiên.
2. Mỗi khoảng con trong tích phân có thể được tính độc lập.
3. Phiên bản tuần tự dùng làm mốc so sánh.
4. OpenMP đại diện cho mô hình chia sẻ bộ nhớ.
5. MPI đại diện cho mô hình truyền thông điệp.
6. Reduction là kỹ thuật trung tâm để tổng hợp kết quả cục bộ.
7. Speedup và efficiency là hai chỉ số chính để đánh giá hiệu năng.
8. Strong scaling và weak scaling giúp đánh giá khả năng mở rộng.
9. Kết quả Pi không phải phần quan trọng nhất; phần quan trọng là đánh giá hiệu quả song song hóa.
10. Báo cáo phải liên hệ rõ với các nội dung được dạy trong học phần Tính toán song song.
```

---

## 8. Những lỗi cần tránh

Không nên làm báo cáo theo các hướng sau:

```text
- Chỉ trình bày công thức tính Pi rồi đưa code, không có phân tích song song hóa.
- Chỉ chạy một cấu hình duy nhất.
- Chỉ in kết quả Pi mà không đo thời gian.
- Không có bản tuần tự để so sánh.
- Không tính speedup và efficiency.
- Không giải thích reduction.
- Không phân biệt OpenMP và MPI.
- Sao chép cấu trúc báo cáo mẫu có phần tích vô hướng hai vector.
- Đưa Chudnovsky/GMP làm trọng tâm chính, khiến đề tài lệch khỏi mục tiêu học phần.
- Tập trung vào giao diện thay vì thuật toán và hiệu năng.
```

---

## 9. Mục lục hoàn chỉnh có thể dùng trực tiếp

```text
1. Giới thiệu đề tài
   1.1. Bối cảnh học phần Tính toán song song
   1.2. Lý do chọn bài toán tính số Pi
   1.3. Mục tiêu của đề tài
   1.4. Phạm vi thực hiện
   1.5. Sản phẩm đầu ra
   1.6. Cấu trúc báo cáo

2. Cơ sở lý thuyết
   2.1. Giới thiệu về số Pi
   2.2. Một số phương pháp tính số Pi
   2.3. Lựa chọn phương pháp tích phân số
   2.4. Công thức tích phân tính Pi
   2.5. Quy tắc điểm giữa
   2.6. Sai số xấp xỉ
   2.7. Khả năng song song hóa của bài toán

3. Phân tích và thiết kế thuật toán song song
   3.1. Thuật toán tuần tự
   3.2. Phân rã dữ liệu
   3.3. Thiết kế thuật toán OpenMP
   3.4. Thiết kế thuật toán MPI
   3.5. Thiết kế Hybrid MPI + OpenMP
   3.6. Kỹ thuật reduction và race condition
   3.7. Phân tích theo mô hình PCAM
   3.8. So sánh các phiên bản thuật toán

4. Cài đặt chương trình
   4.1. Môi trường cài đặt
   4.2. Cấu trúc thư mục chương trình
   4.3. Tham số đầu vào
   4.4. Cài đặt phiên bản tuần tự
   4.5. Cài đặt phiên bản OpenMP
   4.6. Cài đặt phiên bản MPI
   4.7. Cài đặt phiên bản Hybrid nếu có
   4.8. Đo thời gian thực thi
   4.9. Tính speedup, efficiency và sai số
   4.10. Hướng dẫn biên dịch và chạy

5. Kịch bản thực nghiệm
   5.1. Mục tiêu thực nghiệm
   5.2. Cấu hình máy thử nghiệm
   5.3. Công cụ và môi trường chạy
   5.4. Bộ tham số thực nghiệm
   5.5. Thí nghiệm thay đổi kích thước N
   5.6. Thí nghiệm strong scaling
   5.7. Thí nghiệm weak scaling
   5.8. Thí nghiệm so sánh OpenMP và MPI
   5.9. Quy tắc đo thời gian công bằng
   5.10. Các chỉ số đánh giá

6. Kết quả thực nghiệm và đánh giá
   6.1. Kiểm tra độ chính xác
   6.2. Ảnh hưởng của N đến sai số và thời gian chạy
   6.3. Kết quả OpenMP
   6.4. Kết quả MPI
   6.5. Kết quả Hybrid nếu có
   6.6. So sánh OpenMP và MPI
   6.7. Phân tích speedup và efficiency
   6.8. Phân tích overhead, reduction cost và communication cost
   6.9. Nhận xét tổng hợp

7. Kết luận và hướng phát triển
   7.1. Kết quả đạt được
   7.2. Mức độ đáp ứng mục tiêu đề tài
   7.3. Hạn chế
   7.4. Hướng phát triển

Phụ lục
   A. Mã nguồn chính
   B. Lệnh biên dịch và chạy chương trình
   C. Bảng kết quả đầy đủ
   D. Một số ảnh chụp màn hình khi chạy chương trình
```

---

## 10. Chốt định hướng báo cáo

Báo cáo không nên được hiểu là:

```text
Một báo cáo về công thức tính số Pi.
```

Mà nên được hiểu là:

```text
Một báo cáo về thiết kế, cài đặt và đánh giá chương trình song song,
lấy bài toán tính gần đúng số Pi làm bài toán minh họa.
```

Cái xương sống của báo cáo là:

```text
Phân rã dữ liệu
→ Cài đặt tuần tự
→ Cài đặt OpenMP
→ Cài đặt MPI
→ Reduction
→ Benchmark
→ Speedup
→ Efficiency
→ Scalability
→ Nhận xét hiệu năng
```

Vì vậy, khi viết báo cáo, nhóm cần ưu tiên các phần liên quan đến **song song hóa và đánh giá hiệu năng**. Phần công thức tính Pi chỉ cần đủ để giải thích thuật toán, không nên biến thành trọng tâm chính.

---

## 11. Kết luận cuối cùng

Với đề tài:

**Xây dựng và đánh giá chương trình song song tính số Pi bằng phương pháp tích phân số sử dụng OpenMP và MPI**

báo cáo nên được xây dựng theo hướng:

```text
- Bám sát đề cương học phần Tính toán song song.
- Không trình bày riêng phần tích vô hướng hai vector.
- Không tập trung vào Chudnovsky/GMP.
- Không xây dựng app hoặc giao diện.
- Tập trung vào thuật toán, phân rã dữ liệu, OpenMP, MPI, reduction và đánh giá hiệu năng.
```

Đây là hướng phù hợp nhất để báo cáo vừa đúng đề tài, vừa đúng mục tiêu học phần, vừa đủ nội dung để bảo vệ trước giảng viên.
