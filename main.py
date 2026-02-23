import product_manager
# from product_manager import *
while True:
    print("=====QUẢN LÝ CỬA HÀNG LAPTOP=====")
    print("1. Thêm sản phẩm")
    print("2. Hiển thị sản phẩm")
    print("3. Tìm kiếm sản phẩm")
    print("4. Xóa sản phẩm")
    print("0. Thoát")
    choice = input("Chọn chức năng: ")

#Thêm
    if choice == "1":
        product = {
            "id": input("Nhập mã sản phẩm: "),
            "name": input("Nhập tên sản phẩm: "),
            "brand": input("Nhập thương hiệu: "),
            "price": int(input("Nhập giá: ")),
            "quantity": int(input("Nhập số lượng: "))
        }
        product_manager.add_product(product)
        print("Đã thêm sản phẩm")
# HIỂN THỊ 
    elif choice == "2":
        products = product_manager.show_products()
        if len(products) == 0:
            print(" Chưa có sản phẩm")
        else:
            for p in products:
                print(p)

    #  TÌM 
    elif choice == "3":
        code = input("Nhập mã sản phẩm: ")
        result = product_manager.find_product(code)
        if result:
            print(" Tìm thấy:", result)
        else:
            print(" Không tìm thấy")

    #  XÓA 
    elif choice == "4":
        code = input("Nhập mã sản phẩm: ")
        if product_manager.delete_product(code):
            print(" Đã xóa sản phẩm")
        else:
            print(" Không tìm thấy")
#Thoát
    elif choice == "0":
        print("Thoát chương trình:")
        break
    else:
        print("Hãy chọn lại:")

print("Cảm ơn đã sử dụng chương trình!")