import pandas as pd
import numpy as np

# =====================================================
# 1. LOAD DATA (TƯƠNG THÍCH MỌI PANDAS)
# =====================================================
try:
    df = pd.read_csv("synthetic_bank_data.csv", encoding="utf-8")
except:
    df = pd.read_csv("synthetic_bank_data.csv", encoding="latin1")

print("Columns:")
print(df.columns.tolist())

# =====================================================
# 2. DÙNG VỊ TRÍ CỘT (TRÁNH LỖI FONT)
# =====================================================
customer_col = df.columns[0]   # Customer_ID
amount_col   = df.columns[8]   # Số tiền
time_col     = df.columns[9]   # Thời gian

# =====================================================
# 3. CLEAN DATA
# =====================================================
df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
df[amount_col] = pd.to_numeric(df[amount_col], errors="coerce")

df = df.dropna(subset=[time_col, amount_col])
df = df.sort_values([customer_col, time_col])

# =====================================================
# 4. RULE 1 — SỐ TIỀN QUÁ ĐẸP
# =====================================================
df["round_amount"] = df[amount_col] % 100000 == 0
round_ratio = df.groupby(customer_col)["round_amount"].mean()

flag_round = round_ratio > 0.8   # >80% số tiền là số đẹp

# =====================================================
# 5. RULE 2 — KHOẢNG THỜI GIAN QUÁ ĐỀU
# =====================================================
df["time_diff"] = df.groupby(customer_col)[time_col].diff().dt.total_seconds()

time_std = df.groupby(customer_col)["time_diff"].std()

flag_time = time_std < 60   # độ lệch chuẩn < 60 giây

# =====================================================
# 6. RULE 3 — SỐ GIAO DỊCH MỖI NGÀY QUÁ ỔN ĐỊNH
# =====================================================
df["date"] = df[time_col].dt.date

daily_count = df.groupby([customer_col, "date"]).size().reset_index(name="count")

daily_std = daily_count.groupby(customer_col)["count"].std()

flag_daily = daily_std < 0.5

# =====================================================
# 7. RULE 4 — PHƯƠNG SAI SỐ TIỀN QUÁ THẤP
# (Không có noise tự nhiên)
# =====================================================
amount_std = df.groupby(customer_col)[amount_col].std()

flag_amount_variance = amount_std < 100000

# =====================================================
# 8. TỔNG HỢP FLAG
# =====================================================
mimic_df = pd.DataFrame({
    "round_pattern": flag_round,
    "time_pattern": flag_time,
    "daily_pattern": flag_daily,
    "low_amount_variance": flag_amount_variance
})

mimic_df["TH7_Mimicry_Flag"] = (
    mimic_df["round_pattern"] |
    mimic_df["time_pattern"] |
    mimic_df["daily_pattern"] |
    mimic_df["low_amount_variance"]
)

print("\n=== TH7 MIMICRY SUMMARY ===")
print(mimic_df.sum())

print("\nTotal Mimicry Customers:",
      mimic_df["TH7_Mimicry_Flag"].sum())

# =====================================================
# 9. MERGE VỀ DATA GỐC
# =====================================================
df = df.merge(
    mimic_df["TH7_Mimicry_Flag"],
    left_on=customer_col,
    right_index=True,
    how="left"
)

df["TH7_Mimicry_Flag"] = df["TH7_Mimicry_Flag"].fillna(False)

# =====================================================
# 10. SAVE FILE
# =====================================================
df.to_csv("TH7_Mimicry_Result.csv", index=False)

print("\nDone. Saved TH7_Mimicry_Result.csv")
