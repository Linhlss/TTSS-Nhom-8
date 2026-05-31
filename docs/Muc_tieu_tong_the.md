# Mục tiêu tổng thể


## Tên chính thức của đề tài 

Tên đề tài báo cáo là "Xây dựng và đánh giá chương trình song song tính số Pi bằng phương pháp tích phân số sử dụng OpenMP và MPI".

## Định hướng đề tài: Viết chương trình song song tính số Pi

Tài liệu này dùng để định hướng toàn bộ đề tài, giúp nhóm giữ đúng trọng tâm của học phần **MI4364 - Tính toán song song** và tránh đi lệch sang xây dựng ứng dụng phần mềm, giao diện hoặc tính toán số Pi độ chính xác cao ngoài phạm vi cần thiết.

---

## 1. Căn cứ từ đề cương học phần

Theo đề cương học phần, môn **Tính toán song song** không nhằm đào tạo sinh viên xây dựng một hệ thống phần mềm lớn, mà tập trung vào các nội dung chính sau:

- Hiểu các khái niệm cơ bản, thuật ngữ và vai trò của tính toán song song.
- Nắm được các mô hình tính toán song song và hiệu quả của thuật toán song song.
- Vận dụng được một số mẫu thiết kế thuật toán song song như phân chia, chia để trị, cây nhị phân, reduction.
- Cài đặt một số thuật toán song song cho bài toán thực tế không quá phức tạp.
- Sử dụng được các mô hình lập trình song song phổ biến:
  - **OpenMP** cho mô hình chia sẻ bộ nhớ.
  - **MPI** cho mô hình truyền thông điệp.
- Đánh giá chương trình song song thông qua thời gian chạy, speedup, efficiency và khả năng mở rộng.

Vì vậy, bài tập lớn không nên đặt trọng tâm vào việc “tính số Pi càng nhiều chữ số càng tốt”, mà nên dùng bài toán tính số Pi như một bài toán tính toán để thể hiện khả năng **thiết kế, cài đặt và đánh giá chương trình song song**.

---

## 2. Aim tổng thể của đề tài

Aim của đề tài là:

> **Thiết kế, cài đặt và đánh giá hiệu năng chương trình song song tính gần đúng số Pi, nhằm minh họa các mô hình lập trình song song, kỹ thuật phân rã dữ liệu, reduction và khả năng mở rộng khi tăng số luồng hoặc số tiến trình.**

Nói cách khác, đề tài tập trung vào:

- Cách chia bài toán tính Pi thành các phần nhỏ độc lập.
- Cách ánh xạ các phần việc đó lên nhiều thread/process.
- Cách tổng hợp kết quả cục bộ bằng kỹ thuật reduction.
- Cách đo lường và phân tích hiệu quả của song song hóa.
- Cách so sánh phiên bản tuần tự với các phiên bản song song.

Đề tài **không tập trung** vào việc xây dựng app, web, giao diện người dùng, hoặc lập kỷ lục tính số Pi nhiều chữ số.

### 2.1. Thứ tự ưu tiên thực hiện

Ở giai đoạn hiện tại, nhóm nên ưu tiên theo thứ tự sau:

```text
Pha 1: Hoàn thành code và benchmark tối thiểu
- Chạy đúng bản Serial.
- Chạy đúng bản OpenMP.
- Chạy đúng bản MPI.
- Thống nhất format output.
- Kiểm tra sai số, thời gian chạy, speedup, efficiency.
- Có ít nhất một bộ kết quả benchmark ban đầu để đối chiếu.

Pha 2: Mở rộng benchmark và khóa số liệu
- Bổ sung strong scaling, weak scaling, so sánh OpenMP và MPI.
- Rà soát tính công bằng của benchmark.
- Chốt bộ bảng số liệu dùng cho báo cáo.

Pha 3: Viết báo cáo và làm slide
- Viết các chương báo cáo dựa trên code và số liệu đã ổn định.
- Vẽ flowchart, biểu đồ và hình minh họa.
- Làm slide và chuẩn bị bảo vệ.
```

Không nên đầu tư mạnh vào báo cáo và slide khi code còn chưa ổn định. Phần tài liệu chỉ nên được khóa sau khi nhóm đã xác nhận các phiên bản chương trình chạy đúng và có số liệu đủ tin cậy.

---

## 3. Thuật toán chính được lựa chọn

Thuật toán chính nên chọn là:

> **Phương pháp tích phân số theo quy tắc điểm giữa để tính gần đúng số Pi.**

Công thức sử dụng:

```text
π = ∫[0,1] 4 / (1 + x²) dx
```

Ý tưởng tính toán:

```text
1. Chia đoạn [0, 1] thành N khoảng nhỏ.
2. Với mỗi khoảng, lấy điểm giữa x_i.
3. Tính giá trị f(x_i) = 4 / (1 + x_i²).
4. Cộng tất cả các giá trị lại.
5. Nhân với độ rộng mỗi khoảng để thu được giá trị gần đúng của Pi.
```

Lý do chọn thuật toán này:

- Dễ phân rã dữ liệu thành nhiều phần độc lập.
- Rất phù hợp với OpenMP và MPI.
- Dễ minh họa các khái niệm trong học phần: decomposition, reduction, speedup, efficiency, scalability.
- Không bị lệch trọng tâm sang số học độ chính xác cao như Chudnovsky/GMP.
- Đủ đơn giản để dễ bảo vệ, nhưng vẫn có thể scale bằng cách tăng số khoảng chia N lên rất lớn.

---

## 4. Vì sao không chọn Chudnovsky làm thuật toán chính?

Thuật toán Chudnovsky rất mạnh để tính Pi nhiều chữ số, nhưng không nên chọn làm lõi chính nếu mục tiêu là bám sát đề cương học phần cơ bản.

Lý do:

- Dễ làm bài bị lệch sang chủ đề **tính toán số lớn** và **độ chính xác cao**.
- Cần thư viện như GMP/MPFR, làm tăng độ phức tạp ngoài trọng tâm môn học.
- Khó giải thích đầy đủ nếu nhóm chưa thật sự nắm chắc số học độ chính xác tùy ý.
- Báo cáo mẫu đã đi theo hướng này, nên nếu làm tương tự dễ bị trùng ý tưởng.

Chudnovsky có thể được nhắc đến ở phần **phương pháp liên quan** hoặc **hướng phát triển**, nhưng không nên là phần chính của đề tài này.

---

## 5. Scope của đề tài

### 5.1. Trong phạm vi thực hiện

Đề tài sẽ tập trung vào các phần sau:

1. **Cài đặt thuật toán tuần tự**
   - Tính Pi bằng phương pháp tích phân số trên một luồng.
   - Dùng làm baseline để so sánh.

2. **Cài đặt phiên bản OpenMP**
   - Sử dụng mô hình chia sẻ bộ nhớ.
   - Chia vòng lặp tính tổng cho nhiều thread.
   - Dùng `reduction` để cộng tổng cục bộ.
   - Thử nghiệm với nhiều số lượng thread khác nhau.

3. **Cài đặt phiên bản MPI**
   - Sử dụng mô hình truyền thông điệp.
   - Chia miền tính toán cho nhiều process.
   - Mỗi process tính tổng cục bộ.
   - Dùng `MPI_Reduce` để tổng hợp kết quả.

4. **Có thể cài đặt thêm phiên bản Hybrid MPI + OpenMP**
   - Mỗi process MPI quản lý một phần miền tính toán.
   - Trong mỗi process, OpenMP chia nhỏ tiếp cho nhiều thread.
   - Đây là phần mở rộng nếu còn thời gian.

5. **Đánh giá hiệu năng**
   - Đo thời gian chạy.
   - Tính speedup.
   - Tính efficiency.
   - Đánh giá strong scaling và weak scaling nếu có thể.
   - So sánh OpenMP, MPI và Hybrid nếu triển khai được.

6. **Kiểm tra độ chính xác**
   - So sánh kết quả tính được với giá trị Pi chuẩn.
   - Tính sai số tuyệt đối.
   - Nhận xét ảnh hưởng của N đến độ chính xác.

---

### 5.2. Ngoài phạm vi thực hiện

Đề tài sẽ không tập trung vào:

- Xây dựng giao diện đồ họa, web app hoặc phần mềm hoàn chỉnh cho người dùng cuối.
- Tính Pi hàng trăm nghìn hoặc hàng triệu chữ số bằng số học độ chính xác tùy ý.
- Tối ưu GPU/CUDA nếu môn học không yêu cầu.
- Cài đặt các thuật toán số học phức tạp như Chudnovsky, Gauss-Legendre, Borwein làm lõi chính.
- Tối ưu cấp thấp quá sâu như SIMD thủ công, cache blocking phức tạp hoặc vector intrinsic.

---

## 6. Sản phẩm cuối cùng của đề tài

Sản phẩm cuối cùng nên là một **chương trình benchmark chạy bằng terminal**, không phải một hệ thống phần mềm lớn.

Trong ngắn hạn, sản phẩm ưu tiên trước mắt của nhóm nên là:

```text
- Code Serial, OpenMP, MPI chạy được.
- Có lệnh biên dịch và chạy rõ ràng.
- Có script benchmark cơ bản.
- Có ít nhất một file CSV kết quả ban đầu để kiểm tra.
```

Sau khi các phần trên ổn định, nhóm mới chuyển sang hoàn thiện báo cáo và slide.

Chương trình nên có khả năng:

```text
- Nhận số khoảng chia N.
- Nhận số thread hoặc số process.
- Chọn chế độ chạy: serial, OpenMP, MPI, hoặc hybrid.
- In ra giá trị Pi tính được.
- In ra sai số so với Pi chuẩn.
- In ra thời gian chạy.
- In ra speedup và efficiency.
```

Ngoài chương trình benchmark, phần báo cáo nên có tối thiểu các sơ đồ thuật toán sau để giúp việc trình bày và bảo vệ rõ ràng hơn:

```text
- Sơ đồ thuật toán tuần tự.
- Sơ đồ OpenMP: chia N khoảng cho nhiều thread, local sum, reduction.
- Sơ đồ MPI: chia N khoảng cho nhiều process, local sum, MPI_Reduce về rank 0.
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

### 6.1. Tiêu chí hoàn thành đề tài

Có thể xem đề tài đạt yêu cầu tốt nếu thỏa các tiêu chí sau:

```text
- Có ít nhất 3 phiên bản chương trình: Serial, OpenMP, MPI.
- Các phiên bản cho ra giá trị Pi gần đúng và sai số hợp lý.
- Có bảng so sánh thời gian chạy giữa các phiên bản.
- Có tính speedup và efficiency.
- Có nhận xét vì sao speedup không tuyến tính hoàn toàn.
- Có phân tích sự khác nhau giữa OpenMP và MPI.
- Có liên hệ với các khái niệm trong học phần: decomposition, reduction, shared memory, message passing, scalability.
```

Nếu chia theo tiến độ thực hiện, có thể xem đề tài đạt mốc kỹ thuật ban đầu khi thỏa các điều kiện ngắn hạn sau:

```text
- Serial chạy đúng và cho giá trị Pi hợp lý.
- OpenMP chạy đúng với nhiều số thread.
- MPI chạy đúng với nhiều số process.
- Kết quả giữa các phiên bản gần nhau.
- Có benchmark cơ bản và có thể xuất kết quả ra CSV.
```

---

## 7. Cấu trúc chương trình đề xuất

Cấu trúc code có thể tổ chức như sau:

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
```

---

## 8. Các thí nghiệm cần thực hiện

### 8.1. Thí nghiệm 1: Ảnh hưởng của kích thước bài toán

Giữ số thread/process cố định, thay đổi N:

```text
N = 10^6
N = 10^7
N = 10^8
N = 10^9
```

Mục tiêu:

- Chứng minh khi N lớn, song song hóa có ý nghĩa hơn.
- Quan sát sai số giảm khi N tăng.

---

### 8.2. Thí nghiệm 2: Strong scaling

Giữ nguyên N, tăng số thread/process:

```text
N = 10^8 hoặc 10^9
p = 1, 2, 4, 8, 12
```

Mục tiêu:

- Đánh giá khi tăng tài nguyên tính toán thì thời gian giảm bao nhiêu.
- Tính speedup và efficiency.

---

### 8.3. Thí nghiệm 3: Weak scaling

Tăng N tương ứng với số thread/process:

```text
p = 1  -> N = 10^7
p = 2  -> N = 2 × 10^7
p = 4  -> N = 4 × 10^7
p = 8  -> N = 8 × 10^7
```

Mục tiêu:

- Đánh giá khả năng xử lý bài toán lớn hơn khi tăng tài nguyên.
- Quan sát chi phí overhead và chi phí reduction.

---

### 8.4. Thí nghiệm 4: So sánh OpenMP và MPI

Chạy cùng một N với OpenMP và MPI:

```text
OpenMP: 1, 2, 4, 8 threads
MPI:    1, 2, 4, 8 processes
```

Mục tiêu:

- So sánh mô hình chia sẻ bộ nhớ và truyền thông điệp.
- Nhận xét sự khác biệt về overhead, reduction và khả năng mở rộng.

### 8.5. Quy tắc benchmark công bằng nên áp dụng

Để bảng số liệu và speedup có ý nghĩa, nên bổ sung rõ các quy tắc benchmark sau:

```text
- Mỗi cấu hình nên chạy nhiều lần, ví dụ 3 đến 5 lần.
- Nêu rõ lấy giá trị trung bình, trung vị hoặc giá trị tốt nhất, và áp dụng nhất quán.
- Không tính thời gian in kết quả ra màn hình vào thời gian thuật toán nếu có thể tách riêng.
- Với MPI, chỉ process rank 0 nên in kết quả cuối cùng.
- Dùng cùng compiler flags khi so sánh Serial, OpenMP và MPI ở mức tối đa có thể công bằng.
- Dùng cùng giá trị N khi so sánh trực tiếp giữa các phiên bản.
- Hạn chế chạy các ứng dụng nặng khác trong lúc benchmark.
```

### 8.6. Rủi ro kỹ thuật cần chú ý

Nên nêu rõ một số rủi ro và giới hạn thực nghiệm để báo cáo trung thực hơn:

```text
- Nếu N quá nhỏ, overhead song song hóa có thể lớn hơn lợi ích, làm OpenMP hoặc MPI chậm hơn serial.
- Nếu N quá lớn, thời gian chạy có thể rất dài; cũng cần chú ý dùng kiểu dữ liệu đủ lớn cho biến đếm.
- Với kiểu double, sai số sẽ không giảm mãi khi N tăng do giới hạn độ chính xác dấu chấm động.
- MPI chạy trên một máy cá nhân chủ yếu mới phản ánh message passing trên shared hardware, chưa đại diện đầy đủ cho cluster thật.
- Nếu số thread vượt quá số lõi logic hợp lý, hiệu năng có thể giảm do oversubscription và context switching.
```

---

## 9. Các chỉ số đánh giá

### 9.1. Thời gian chạy

```text
T_p = thời gian chạy với p thread/process
```

### 9.2. Speedup

```text
Speedup = T_1 / T_p
```

Trong đó:

- `T_1` là thời gian chạy tuần tự hoặc chạy với 1 thread/process.
- `T_p` là thời gian chạy với p thread/process.

### 9.3. Efficiency

```text
Efficiency = Speedup / p
```

Nếu biểu diễn theo phần trăm:

```text
Efficiency (%) = (Speedup / p) × 100
```

### 9.4. Sai số

```text
Error = |pi_computed - pi_reference|
```

Mục tiêu không phải đạt sai số nhỏ nhất tuyệt đối, mà là đảm bảo chương trình tính đúng xu hướng và kết quả hợp lý khi N tăng.

---

## 10. Những nội dung cần nhấn mạnh trong báo cáo

Báo cáo nên nhấn mạnh các điểm sau:

1. **Bài toán có khả năng song song hóa tự nhiên**
   - Mỗi khoảng con trong tích phân có thể tính độc lập.

2. **Phân rã dữ liệu**
   - Chia miền [0, 1] hoặc tập chỉ số `0..N-1` thành các phần nhỏ.

3. **Reduction**
   - Mỗi thread/process tính tổng cục bộ.
   - Các tổng cục bộ được cộng lại để tạo kết quả cuối cùng.

4. **So sánh mô hình lập trình song song**
   - OpenMP: dễ triển khai trên shared memory.
   - MPI: phù hợp với distributed memory và mô hình nhiều process.
   - Hybrid: kết hợp cả hai nếu triển khai được.

   Với bài toán tích phân số theo quy tắc điểm giữa, khối lượng công việc giữa các vòng lặp thường gần tương đương nhau. Vì vậy, trong OpenMP, `schedule(static)` thường là lựa chọn hợp lý mặc định; các chiến lược `dynamic` hoặc `guided` chỉ nên được xem là phần mở rộng hoặc so sánh thêm, không phải trọng tâm chính của đề tài.

5. **Đánh giá hiệu năng**
   - Không chỉ đưa ra kết quả Pi.
   - Phải có bảng thời gian, speedup, efficiency.
   - Phải nhận xét vì sao speedup không tuyến tính hoàn toàn.

6. **Khả năng mở rộng**
   - Khi tăng số thread/process, thời gian có giảm không?
   - Khi tăng kích thước bài toán, chương trình có tận dụng tốt tài nguyên không?

---

## 11. Aim và scope viết gọn để đưa vào báo cáo

Có thể dùng đoạn sau trong báo cáo:

```text
Mục tiêu của đề tài là xây dựng và đánh giá chương trình song song tính gần đúng số Pi bằng phương pháp tích phân số. Đề tài tập trung vào việc áp dụng các mô hình lập trình song song chia sẻ bộ nhớ và truyền thông điệp, cụ thể là OpenMP và MPI, để phân rã miền tính toán, xử lý cộng dồn kết quả bằng reduction, đo lường thời gian thực thi, speedup, efficiency và khả năng mở rộng của chương trình khi thay đổi số luồng, số tiến trình và kích thước bài toán.
```

Scope viết gọn:

```text
Phạm vi của đề tài bao gồm việc cài đặt phiên bản tuần tự, phiên bản song song bằng OpenMP, phiên bản song song bằng MPI và có thể mở rộng sang mô hình hybrid MPI + OpenMP. Đề tài tập trung vào phân tích hiệu năng và khả năng mở rộng, không tập trung vào xây dựng giao diện người dùng hoặc tính số Pi với số lượng chữ số cực lớn bằng các thư viện số học độ chính xác cao.
```

---

## 12. Kết luận định hướng

Đề tài nên được hiểu là:

> **Một bài toán thực nghiệm về thiết kế và đánh giá chương trình song song, lấy việc tính gần đúng số Pi làm bài toán minh họa.**

Do đó, trong quá trình thực hiện, nhóm cần ưu tiên:

```text
1. Cài đặt đúng các phiên bản tuần tự, OpenMP và MPI.
2. Kiểm tra tính đúng đắn và thống nhất output.
3. Đo thời gian chạy một cách công bằng.
4. Tạo được bộ benchmark cơ bản và file kết quả.
5. Sau đó mới khóa nội dung báo cáo, biểu đồ và slide.
6. Cuối cùng mới tối ưu cách trình bày và luyện bảo vệ.
```

Thuật toán chính nên là:

> **Tính Pi bằng tích phân số theo quy tắc điểm giữa, song song hóa bằng OpenMP và MPI.**

Đây là lựa chọn bám sát đề cương học phần, đủ rõ để triển khai, đủ scale để đánh giá hiệu năng, và không làm đề tài bị lệch sang một lĩnh vực ngoài trọng tâm.
