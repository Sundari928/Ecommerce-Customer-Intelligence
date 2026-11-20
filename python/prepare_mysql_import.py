import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_ecommerce.csv")

# Convert True/False into 1/0
df["is_returned"] = (
    df["is_returned"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({"true": 1, "false": 0})
)

# Check conversion
print("Missing values:", df["is_returned"].isna().sum())
print(df["is_returned"].value_counts())

# Save new import-ready CSV
df.to_csv(
    "dataset/mysql_import_ecommerce.csv",
    index=False
)

print("MySQL Import File Created Successfully!")