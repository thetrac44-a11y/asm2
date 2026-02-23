
# ✓ Tạo file string_utils.py.

# ✓ Trong file đó, viết hàm viet_hoa_chu_dau(s: str) → str để viết hoa chữ cái

# đầu của một chuỗi.

# ✓ Tạo file app.py.

# ✓ Trong app.py, import và sử dụng hàm vừa tạo để xử lý một chuỗi bất kỳ.
def bai3():
    input_string = input("viet chu:")
    result = string_utils.viet_hoa_chu_dau(input_string)
    print("Chuỗi sau khi viết hoa chữ cái đầu:", result)
     

bai3()