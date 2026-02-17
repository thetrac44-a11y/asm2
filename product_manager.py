#Danh sách sản phẩm 
products = []
#Thêm sản phẩm
def add_product(product):
    products.append(product)
#Hiển thị sản phẩm
def show_products():
    return products
#Tìm kiếm sản phẩm 
def find_product(product_id):
    for p in products:
        if p["id"] == product_id:
            return p
    return None
# xóa sản phẩm theo mã
def delete_product(product_id):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            return True 
        return False