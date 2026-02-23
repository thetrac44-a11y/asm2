import numpy as np

# Các giá trị của X (số lỗi)
X = np.array([0, 1, 2, 3, 4])

# Xác suất tương ứng
P = np.array([0.40, 0.35, 0.15, 0.08, 0.02])

# 1. Tính kỳ vọng E(X)
E_X = np.sum(X * P)

# 2. Tính phương sai Var(X)
Var_X = np.sum((X - E_X) ** 2 * P)

# 3. Tính độ lệch chuẩn
Std_X = np.sqrt(Var_X)

# In kết quả
print("Kỳ vọng E(X):", E_X)
print("Phương sai Var(X):", Var_X)
print("Độ lệch chuẩn σ:", Std_X)
