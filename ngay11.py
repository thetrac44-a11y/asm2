# Bài tập nhanh tại lớp 1:
# Viết một hàm is_even(number) để kiểm tra một số có phải là số chẵn hay

# không. Hàm này nên dùng print hay return?

# Chúng ta muốn hàm này trả về một kết quả (True hoặc False) để chương trình

# chính có thể dùng nó trong một câu lệnh if. Do đó, phải dùng return.

# Bài tập nhanh tại lớp 2:
# Câu hỏi: Đoán xem kết quả của đoạn code sau là gì?

# Bài tập nhanh tại lớp 3:
# ✓ Tạo file string_utils.py.

# ✓ Trong file đó, viết hàm viet_hoa_chu_dau(s: str) → str để viết hoa chữ cái

# đầu của một chuỗi.

# ✓ Tạo file app.py.

# ✓ Trong app.py, import và sử dụng hàm vừa tạo để xử lý một chuỗi bất kỳ.
#Bai1
def bai1():
    def is_even(number):
        return number % 2 == 0
    
    x= int(input("Nhập một số nguyên: "))
    if is_even(x):
        print(f"{x} là số chẵn.")
    else:
        print(f"{x} là số lẻ.")
#Bai2
def bai2():
    x = 10
    def my_func():
        x = 5 
        x += 1
        print("Bên trong hàm:", x)
    my_func()
    print("Bên ngoài hàm:", x)
#Kết quả:
#Bên trong hàm: 6   
bai2()