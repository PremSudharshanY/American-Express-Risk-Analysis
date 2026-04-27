import pandas as pd
import numpy as np

# ----------------------------
# SETTINGS
# ----------------------------
rows = 800000
np.random.seed(42)

# ----------------------------
# DATA GENERATION
# ----------------------------
data = pd.DataFrame({
    "Customer_ID": np.arange(1, rows+1),

    "First_Name": np.random.choice(
        ["John","David","Emma","Sophia","Liam","Olivia","Noah","Ava"], rows
    ),

    "Last_Name": np.random.choice(
        ["Smith","Johnson","Brown","Taylor","Anderson","Thomas"], rows
    ),

    "Age": np.random.randint(18, 75, rows),

    "Gender": np.random.choice(["Male", "Female"], rows),

    "City": np.random.choice(
        ["New York","Los Angeles","Chicago","Houston","Phoenix"], rows
    ),

    # ✅ FIXED (no int32 error, unique values)
    "Account_Number": np.arange(
        1000000000, 1000000000 + rows, dtype=np.int64
    ),

    "Account_Type": np.random.choice(
        ["Savings", "Current", "Credit Card", "Loan"], rows
    ),

    "Account_Status": np.random.choice(
        ["Active","Inactive","Closed"], rows, p=[0.8, 0.15, 0.05]
    ),

    "Transaction_ID": np.arange(500000, 500000 + rows),

    "Transaction_Type": np.random.choice(
        ["Debit","Credit","Online Payment","ATM Withdrawal"], rows
    ),

    "Transaction_Amount": np.random.randint(100, 100000, rows),

    "Transaction_Date": pd.to_datetime("2023-01-01") +
        pd.to_timedelta(np.random.randint(0, 365, rows), unit='D'),

    "Merchant_Category": np.random.choice(
        ["Retail","Food","Travel","Bills","Entertainment"], rows
    ),

    "Credit_Score": np.random.randint(300, 900, rows),

    "Loan_Amount": np.random.randint(0, 500000, rows),

    "Interest_Rate": np.round(np.random.uniform(5, 20, rows), 2),

    "Tenure_Years": np.random.randint(0, 20, rows),

    "Balance": np.random.randint(1000, 1000000, rows),

    "Income": np.random.randint(20000, 200000, rows),

    "Card_Type": np.random.choice(
        ["Silver","Gold","Platinum"], rows
    ),

    "Reward_Points": np.random.randint(0, 50000, rows),

    "Late_Payment_Flag": np.random.choice(
        [0, 1], rows, p=[0.9, 0.1]
    ),

    "Fraud_Flag": np.random.choice(
        [0, 1], rows, p=[0.97, 0.03]
    ),

    "Customer_Satisfaction_Score": np.random.randint(1, 6, rows)
})

# ----------------------------
# ADD 4% ZERO BALANCE
# ----------------------------
zero_indices = np.random.choice(rows, int(rows * 0.04), replace=False)
data.loc[zero_indices, "Balance"] = 0

# ----------------------------
# SAVE FILE
# ----------------------------
data.to_csv("banking_dataset_800k.csv", index=False)

print("✅ Dataset created successfully!")