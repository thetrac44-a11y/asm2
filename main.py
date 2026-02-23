# pip install fastapi uvicorn
# chạy code: uvicorn main:app --reload
# Kiểm tra kết quả: trang chủ http://127.0.0.1:8000
# Tài liệu tương tác: http://127.0.0.1:8000/docs

from fastapi import FastAPI

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

