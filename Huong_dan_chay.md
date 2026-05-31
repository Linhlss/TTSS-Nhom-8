# HUONG DAN CHAY PROJECT TINH SO PI SONG SONG

## 1. Muc dich cua project

Project nay dung de tinh gan dung so Pi bang phuong phap tich phan so, sau do so sanh thoi gian chay va hieu nang giua:

- `Serial`
- `OpenMP`
- `MPI`

Project hien tai da ho tro:

- Build ca 3 phien ban bang `make all`
- Chay rieng tung phien ban bang script
- Chay benchmark chung va xuat 1 file CSV duy nhat
- Chay benchmark suite day du theo `N`, strong scaling va weak scaling
- Sinh bieu do bao cao tu cac file CSV

---

## 2. Cau truc thu muc hien tai

```text
TTSS-CK/
├── bin/
├── docs/
├── include/
│   └── pi_common.h
├── report/
│   └── figures/
├── results/
│   ├── README.md
│   ├── benchmark_result.csv
│   ├── raw_runs.csv
│   ├── n_size_results.csv
│   ├── strong_scaling_results.csv
│   ├── weak_scaling_results.csv
│   ├── openmp_mpi_comparison.csv
│   ├── table_strong_scaling.csv
│   ├── table_error_by_n.csv
│   └── table_weak_scaling.csv
├── scripts/
│   ├── benchmark.py
│   ├── benchmark_suite.py
│   ├── generate_charts.py
│   ├── run_serial.sh
│   ├── run_openmp.sh
│   └── run_mpi.sh
├── src/
│   ├── pi_serial.c
│   ├── pi_openmp.c
│   ├── pi_openmp_race_demo.c
│   └── pi_mpi.c
├── Huong_dan_chay.md
├── Makefile
└── README.md
```

Y nghia cac file chinh:

- `src/pi_serial.c`: ban tuan tu
- `src/pi_openmp.c`: ban song song bang OpenMP
- `src/pi_mpi.c`: ban song song bang MPI
- `src/pi_openmp_race_demo.c`: file minh hoa race condition, khong dung lam ket qua chinh
- `include/pi_common.h`: ham dung chung, parse tham so, in ket qua CSV
- `scripts/benchmark.py`: benchmark chung cho `Serial`, `OpenMP`, `MPI`
- `scripts/benchmark_suite.py`: chay toan bo thi nghiem bat buoc va luu du lieu tho
- `scripts/generate_charts.py`: sinh bieu do PNG tu ket qua benchmark suite
- `scripts/run_serial.sh`: chay nhanh Serial
- `scripts/run_openmp.sh`: chay nhanh OpenMP
- `scripts/run_mpi.sh`: chay nhanh MPI
- `results/benchmark_result.csv`: file ket qua benchmark chung
- `results/raw_runs.csv`: du lieu tho tung lan chay trong benchmark suite
- `results/n_size_results.csv`: ket qua theo thay doi `N`
- `results/strong_scaling_results.csv`: ket qua strong scaling
- `results/weak_scaling_results.csv`: ket qua weak scaling
- `results/openmp_mpi_comparison.csv`: ket qua so sanh truc tiep OpenMP va MPI
- `results/table_*.csv`: cac bang tong hop dua vao bao cao
- `report/figures/`: cac bieu do PNG sinh tu benchmark suite
- `Makefile`: build va chay cac target chinh

---

## 3. Moi truong hien tai

Project hien tai dang duoc cau hinh de chay tren macOS voi Homebrew toolchain:

- `gcc-15` de build `Serial` va `OpenMP`
- `open-mpi` de build va chay `MPI`
- `python3` de chay benchmark

`Makefile` hien tai dang goi truc tiep:

```text
/opt/homebrew/bin/gcc-15
/opt/homebrew/bin/mpicc
/opt/homebrew/bin/mpirun
```

Neu may cua ban khong co cac tool nay, can cai dat truoc.

---

## 4. Cai cong cu can thiet tren macOS

Kiem tra:

```bash
/opt/homebrew/bin/gcc-15 --version
/opt/homebrew/bin/mpicc --version
/opt/homebrew/bin/mpirun --version
python3 --version
make --version
```

Neu thieu, cai dat:

```bash
brew install gcc libomp open-mpi
```

---

## 5. Vao dung thu muc project

Tu terminal, vao thu muc project:

```bash
cd /Users/thao/Documents/TTSS-CK
```

Kiem tra:

```bash
pwd
ls
```

Neu thay `src`, `scripts`, `include`, `results`, `Makefile` thi la dung.
Neu thay them `docs` va `report` thi la day du theo repo hien tai.

---

## 6. Bien dich project

Chay:

```bash
make all
```

Lenh nay hien tai se build 3 chuong trinh chinh:

```text
src/pi_serial.c -> bin/pi_serial
src/pi_openmp.c -> bin/pi_openmp
src/pi_mpi.c    -> bin/pi_mpi
```

Kiem tra:

```bash
ls bin
```

Ket qua mong doi:

```text
pi_mpi
pi_openmp
pi_serial
```

Luu y:

- `pi_openmp_race_demo` khong duoc build trong `make all`
- Neu `make all` bao `Nothing to be done for 'all'.` thi khong phai loi; nghia la cac file build da ton tai va khong can build lai
- Neu muon build lai tu dau, chay:

```bash
make clean
make all
```

---

## 7. Chay tung phien ban

### 7.1. Serial

Chay truc tiep:

```bash
./bin/pi_serial 1000000
```

Hoac dung script:

```bash
bash scripts/run_serial.sh 1000000
```

### 7.2. OpenMP

Chay truc tiep:

```bash
./bin/pi_openmp 1000000 4
```

Hoac dung script:

```bash
bash scripts/run_openmp.sh 1000000 4
```

Trong do:

- tham so 1: `N`
- tham so 2: so thread

### 7.3. MPI

Chay truc tiep:

```bash
/opt/homebrew/bin/mpirun -np 4 ./bin/pi_mpi 1000000
```

Hoac dung script:

```bash
bash scripts/run_mpi.sh 1000000 4
```

Trong do:

- tham so 1: `N`
- tham so 2: so process

---

## 8. Dinh dang output cua tung chuong trinh

Ca 3 phien ban hien tai deu in theo cung 1 dinh dang CSV:

```text
mode,N,workers,pi,error,time_sec
```

Vi du:

```text
serial,1000000,1,3.141592653589764,2.886579864025407e-14,0.001165000
openmp,1000000,4,3.141592653589876,8.260059303211165e-14,0.000469000
mpi,1000000,4,3.141592653589903,1.101341240428155e-13,0.000293000
```

Y nghia cac cot:

- `mode`: `serial`, `openmp`, `mpi`
- `N`: so khoang chia
- `workers`: so thread hoac so process
- `pi`: gia tri Pi tinh duoc
- `error`: sai so tuyet doi
- `time_sec`: thoi gian chay

---

## 9. Chay benchmark chung

Script benchmark hien tai:

```bash
scripts/benchmark.py
```

Cach chay:

```bash
python3 scripts/benchmark.py 100000000 3 1,2,4,8 1,2,4,8
```

Y nghia:

```text
100000000  = N
3          = moi cau hinh chay 3 lan
1,2,4,8    = cac cau hinh OpenMP
1,2,4,8    = cac cau hinh MPI
```

Script se:

```text
1. Build lai bang make all neu can
2. Chay Serial lam baseline
3. Chay OpenMP voi 1,2,4,8 thread
4. Chay MPI voi 1,2,4,8 process
5. Tinh speedup va efficiency
6. Ghi tat ca vao 1 file CSV chung
```

---

## 10. File ket qua benchmark

Ket qua duoc luu tai:

```text
results/benchmark_result.csv
```

Kiem tra nhanh:

```bash
sed -n '1,20p' results/benchmark_result.csv
```

Header hien tai:

```text
mode,N,workers,pi,error,time_sec,time_std,speedup,efficiency,efficiency_percent
```

Y nghia them:

- `time_std`: do lech chuan giua cac lan chay
- `speedup`: `T_serial / T_parallel`
- `efficiency`: `speedup / workers`
- `efficiency_percent`: `efficiency * 100`

---

## 11. Quy trinh chay de lay so lieu ky thuat

Thu tu nen chay:

```bash
cd /Users/thao/Documents/TTSS-CK
make clean
make all
bash scripts/run_serial.sh 1000000
bash scripts/run_openmp.sh 1000000 4
bash scripts/run_mpi.sh 1000000 4
python3 scripts/benchmark.py 100000000 3 1,2,4,8 1,2,4,8
```

Sau do mo:

```text
results/benchmark_result.csv
```

Neu can khoa toan bo so lieu de viet bao cao, chay:

```bash
make benchmark-suite
make charts
```

Bo du lieu day du se gom:

```text
results/raw_runs.csv
results/n_size_results.csv
results/strong_scaling_results.csv
results/weak_scaling_results.csv
results/openmp_mpi_comparison.csv
results/table_strong_scaling.csv
results/table_error_by_n.csv
results/table_weak_scaling.csv
```

Bieu do duoc luu tai:

```text
report/figures/
```

Kiem tra nhanh:

```bash
ls results
ls report/figures
```

---

## 12. Luu y khi do benchmark

- Khong chay nhieu benchmark chong cheo cung luc
- Nen dong cac ung dung nang khac neu co the
- `N` qua nho se lam speedup bi nhieu
- `N = 10^8` hien tai hop ly hon `10^7` de nhin xu huong
- OpenMP va MPI 1 worker co the nhanh hoac cham hon Serial mot chut do overhead va do sai so do thoi gian

---

## 13. Cac lenh quan trong can nho

Build:

```bash
make all
```

Build lai tu dau:

```bash
make clean
make all
```

Chay Serial:

```bash
bash scripts/run_serial.sh 1000000
```

Chay OpenMP 4 thread:

```bash
bash scripts/run_openmp.sh 1000000 4
```

Chay MPI 4 process:

```bash
bash scripts/run_mpi.sh 1000000 4
```

Chay benchmark chung:

```bash
python3 scripts/benchmark.py 100000000 3 1,2,4,8 1,2,4,8
```

Chay toan bo benchmark de viet bao cao:

```bash
make benchmark-suite
make charts
```

Mo ket qua:

```bash
sed -n '1,20p' results/benchmark_result.csv
```
