from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# ==========================================
# BƯỚC 1: SINH CẶP KHÓA RSA (Key Generation)
# ==========================================
# Tạo Khóa bí mật (Private Key) với độ dài 2048 bit (tiêu chuẩn an toàn hiện nay)
private_key = rsa.generate_private_key(
    public_exponent=65537, # Giá trị e phổ biến nhất
    key_size=2048,
)

# Rút trích Khóa công khai (Public Key) từ Khóa bí mật
public_key = private_key.public_key()

print("1. Đã sinh thành công cặp khóa RSA 2048-bit.\n")


# ==========================================
# BƯỚC 2: MÃ HÓA (Encryption)
# ==========================================
# Dữ liệu gốc cần bảo mật (phải chuyển sang dạng byte)
message = "Đây là thông điệp tối mật gửi bằng RSA".encode('utf-8')

# Dùng KHÓA CÔNG KHAI để mã hóa dữ liệu
# Sử dụng cơ chế đệm OAEP kết hợp băm SHA256 để chống lại các cuộc tấn công thay đổi bản mã
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"2. Bản mã (chỉ hiển thị 64 ký tự Hex đầu tiên cho gọn):\n{ciphertext.hex()[:64]}...\n")


# ==========================================
# BƯỚC 3: GIẢI MÃ (Decryption)
# ==========================================
# Dùng KHÓA BÍ MẬT để giải mã
# Phải sử dụng đúng cơ chế đệm (padding) như lúc mã hóa
plaintext_bytes = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Chuyển đổi byte trở lại thành chuỗi văn bản
print(f"3. Dữ liệu sau khi giải mã:\n{plaintext_bytes.decode('utf-8')}")