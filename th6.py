import pandas as pd

# ==============================
# 1. LOAD DATA
# ==============================

transactions_path = "synthetic_bank_data.csv"
job_path = "AML_5Months_TimeLogic.csv"

transactions_df = pd.read_csv(transactions_path)
job_df = pd.read_csv(job_path)

# ==============================
# 2. PREPROCESS
# ==============================

# Chuẩn hóa cột
transactions_df["account_id"] = transactions_df.iloc[:, 0]
transactions_df["amount"] = pd.to_numeric(
    transactions_df.iloc[:, 8], errors="coerce"
)

job_df["account_id"] = job_df["Customer_ID"]
job_df["income"] = pd.to_numeric(job_df["Income"], errors="coerce")
job_df["job"] = job_df["Job"]

transactions_df = transactions_df.dropna(subset=["amount"])
job_df = job_df.dropna(subset=["income"])

# ==============================
# 3. TÍNH TỔNG GIAO DỊCH
# ==============================

total_transaction = (
    transactions_df
    .groupby("account_id")["amount"]
    .sum()
    .reset_index()
)

total_transaction.rename(columns={"amount": "total_amount"}, inplace=True)

# ==============================
# 4. MERGE DATA
# ==============================

merged_df = pd.merge(
    total_transaction,
    job_df[["account_id", "income", "job"]],
    on="account_id",
    how="left"
)

# ==============================
# 5. RISK EVALUATION MODEL
# ==============================

def evaluate_risk(row):
    income = row["income"]
    total_amount = row["total_amount"]
    job = str(row["job"]).lower()

    reasons = []
    score = 0
    ratio = 0

    if income > 0:
        ratio = total_amount / income

    # 1️⃣ Ratio checks
    if ratio > 10:
        reasons.append("Giao dịch vượt 10 lần thu nhập")
        score += 1

    if ratio > 20:
        reasons.append("Giao dịch vượt 20 lần thu nhập")
        score += 2

    if ratio > 50:
        reasons.append("Giao dịch vượt 50 lần thu nhập")
        score += 3

    # 2️⃣ Nghề nhạy cảm
    suspicious_jobs = ["student", "unemployed", "housewife"]
    if job in suspicious_jobs and ratio > 10:
        reasons.append("Nghề nghiệp không phù hợp với dòng tiền")
        score += 2

    # 3️⃣ Thu nhập thấp nhưng dòng tiền cực lớn
    if income < 7000000 and total_amount > 1000000000:
        reasons.append("Thu nhập thấp nhưng dòng tiền cực lớn")
        score += 3

    # ====== CLASSIFY ======
    if score >= 6:
        level = "High"
    elif score >= 3:
        level = "Medium"
    elif score >= 1:
        level = "Low"
    else:
        level = ""

    return pd.Series([ratio, "; ".join(reasons), level])


merged_df[["ratio", "TH6_flag", "Risk_Level"]] = merged_df.apply(
    evaluate_risk, axis=1
)

# Lọc tài khoản vi phạm
result = merged_df[merged_df["Risk_Level"] != ""]

# ==============================
# 6. SUMMARY SHEET
# ==============================

summary = pd.DataFrame({
    "Metric": [
        "Tổng số tài khoản",
        "Tổng số tài khoản vi phạm",
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ],
    "Value": [
        len(merged_df),
        len(result),
        len(result[result["Risk_Level"] == "High"]),
        len(result[result["Risk_Level"] == "Medium"]),
        len(result[result["Risk_Level"] == "Low"])
    ]
})

# ==============================
# 7. TOP 10 HIGH RISK
# ==============================

top10_high = (
    result[result["Risk_Level"] == "High"]
    .sort_values(by="ratio", ascending=False)
    .head(10)
)

# ==============================
# 8. EXPORT TO EXCEL
# ==============================

output_file = "TH6_AML_Final_Report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    result.to_excel(writer, index=False, sheet_name="TH6_Violation")
    summary.to_excel(writer, index=False, sheet_name="Summary")
    top10_high.to_excel(writer, index=False, sheet_name="Top10_HighRisk")

print("======================================")
print("Đã tạo file:", output_file)
print("Tổng tài khoản:", len(merged_df))
print("Tài khoản vi phạm:", len(result))
print("======================================")
