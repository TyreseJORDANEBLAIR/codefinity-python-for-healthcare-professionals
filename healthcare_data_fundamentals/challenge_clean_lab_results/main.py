import pandas as pd

data = {
    "patient_id": [201, 202, 203, 204, 205],
    "cholesterol": [205, None, 187, None, 220]
}
df = pd.DataFrame(data)

# Your code here
# Count missing values in 'cholesterol'
missing_count = df["cholesterol"].isnull().sum()
print(missing_count)

# Fill missing values with median cholesterol value
# (fill code here)
median_chol = df["cholesterol"].median()
df["cholesterol"].fillna(median_chol, inplace=True)

print(df)
