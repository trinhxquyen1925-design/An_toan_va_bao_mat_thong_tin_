import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes

# ==========================================
# GIAI ĐOẠN 1: CHUẨN BỊ
# ==========================================
# Người nhận tạo cặp khóa RSA và công bố Khóa Công Khai
private_key_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_rsa = private_key_rsa.public_key()

# Thông điệp rất dài (mô phỏng một file lớn mà RSA không mã hóa nổi)
message = b"Day la mot file tai lieu cuc ky lon. " * 50 
print(f"1. Kích thước dữ liệu gốc: {len(message)} bytes")

# ==========================================
# GIAI ĐOẠN 2: NGƯỜI GỬI MÃ HÓA (DÙNG AES VÀ RSA)
# ==========================================
# A. Sinh ngẫu nhiên Khóa Phiên AES (Session Key) 256-bit (32 bytes)
session_key_aes = os.urandom(32)
iv = os.urandom(16)

# B. Dùng AES để mã hóa khối dữ liệu lớn siêu tốc
padder = symmetric_padding.PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()
cipher_aes = Cipher(algorithms.AES(session_key_aes), modes.CBC(iv), backend=default_backend())
encryptor = cipher_aes.encryptor()
ciphertext_aes = encryptor.update(padded_data) + encryptor.finalize()
print("2. Đã mã hóa file dữ liệu bằng AES (tốc độ cao).")

# C. Dùng Khóa Công Khai RSA của người nhận để mã hóa Khóa Phiên AES (Bọc khóa)
encrypted_session_key = public_key_rsa.encrypt(
    session_key_aes,
    asymmetric_padding.OAEP(
        mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("3. Đã dùng RSA để bọc Khóa Phiên AES an toàn.")

# ---> Người gửi đóng gói: [encrypted_session_key, iv, ciphertext_aes] và gửi đi qua Internet.

# ==========================================
# GIAI ĐOẠN 3: NGƯỜI NHẬN GIẢI MÃ
# ==========================================
# A. Nhận được gói tin, người nhận dùng Khóa Bí Mật RSA của mình để giải mã lấy lại Khóa Phiên AES
decrypted_session_key = private_key_rsa.decrypt(
    encrypted_session_key,
    asymmetric_padding.OAEP(
        mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("4. Người nhận đã mở khóa RSA để lấy lại Khóa Phiên AES.")

# B. Dùng Khóa Phiên AES vừa lấy lại được để giải mã file dữ liệu lớn
cipher_decrypt = Cipher(algorithms.AES(decrypted_session_key), modes.CBC(iv), backend=default_backend())
decryptor = cipher_decrypt.decryptor()
unpadded_data = decryptor.update(ciphertext_aes) + decryptor.finalize()

unpadder = symmetric_padding.PKCS7(128).unpadder()
original_message = unpadder.update(unpadded_data) + unpadder.finalize()

print(f"5. Khôi phục thành công! Kích thước dữ liệu giải mã: {len(original_message)} bytes")
# Kiểm tra đối chiếu
assert original_message == message
print("=> Khớp 100% với file gốc.")