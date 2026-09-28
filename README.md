# Bài tập: Thuật toán mã hóa hiện đại (AES, RSA và Hybrid)

**Môn học:** An toàn và bảo mật thông tin  
**Trường:** Đại học Kỹ thuật Công nghiệp – Đại học Thái Nguyên  
**Ngành:** Kỹ thuật máy tính (Lớp: K59KMT)  
**Mã sinh viên:** K235480106059  
**Sinh viên thực hiện:** Trịnh Xuân Quyền  

## 1. Giới thiệu dự án
Dự án này là bài tập thực hành cài đặt và mô phỏng các thuật toán mã hóa dữ liệu cốt lõi trong an toàn thông tin bằng ngôn ngữ Python. Dự án đáp ứng các yêu cầu:
- **Thuật toán AES & DES:** Trình bày nguyên lý, quy trình mã hóa/giải mã và cài đặt trực tiếp thuật toán AES.
- **Thuật toán RSA:** Khảo sát nguyên lý sinh cặp khóa (Public/Private Key) và mã hóa bất đối xứng.
- **Mô hình áp dụng RSA & Mã hóa lai:** Áp dụng các mô hình xác thực (người gửi, người nhận, cả hai), so sánh hiệu năng thời gian giữa RSA và AES, từ đó xây dựng hệ thống mô phỏng "Phong bì số" kết hợp tốc độ của AES và khả năng bảo mật khóa của RSA.

## 2. Cấu trúc thư mục
- `aes.py`: Mã nguồn mô phỏng thuật toán AES và RSA hoạt động độc lập.
- `hybrid.py`: Mã nguồn mô phỏng kỹ thuật mã hóa lai (Hybrid Encryption) - kết hợp AES và RSA.
- `README.md`: Tài liệu mô tả dự án (file này).

## 3. Yêu cầu hệ thống
- **Ngôn ngữ:** Python 3.x
- **Thư viện bắt buộc:** `cryptography`

## 4. Hướng dẫn cài đặt và chạy chương trình

**Bước 1: Cài đặt thư viện**
Mở Terminal / Command Prompt tại thư mục chứa dự án và chạy lệnh:
```bash
pip install cryptography
```

**Bước 2: Chạy thử nghiệm AES và RSA độc lập**
```bash
python aes.py
```
<img width="1920" height="1020" alt="23dc3701-0ef3-4559-bfcd-1f33b657a983" src="https://github.com/user-attachments/assets/a751f1be-eb4b-4800-8bb5-72a51957a9ed" />

*Kết quả:* Chương trình sẽ sinh khóa, tiến hành mã hóa thông điệp, in ra bản mã (chuỗi Hex) và giải mã để khôi phục lại văn bản gốc.

**Bước 3: Chạy thử nghiệm Mã hóa lai (Hybrid Encryption)**
```bash
python hybrid.py
```
<img width="1920" height="1020" alt="4d09c7a1-98bc-4187-abd7-e9e95fe7a19d" src="https://github.com/user-attachments/assets/7cb55f16-fbbf-4ef8-bc13-92ff78e6697c" />

*Kết quả:* Chương trình mô phỏng việc mã hóa một tệp tin lớn bằng khóa phiên AES siêu tốc, sau đó dùng khóa công khai RSA bọc khóa phiên này lại. Ở chiều ngược lại, hệ thống tiến hành mở khóa bằng khóa bí mật RSA để lấy lại khóa phiên và khôi phục 100% dung lượng tệp tin gốc.
