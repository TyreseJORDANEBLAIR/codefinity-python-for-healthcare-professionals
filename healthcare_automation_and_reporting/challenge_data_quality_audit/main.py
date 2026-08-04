import pandas as pd

data = {
    "patient_id": [1, 2, 3, 4, 5],
    "age": [34, -2, 55, 42, 28],
    "diagnosis": ["Hypertension", None, "Diabetes", "Asthma", None]
}
df = pd.DataFrame(data)

# Your code here
negative_age = df[df["age"] < 0]
missing_diagnosis = df[df["diagnosis"].isnull()]
problematic_records = pd.concat([negative_age, missing_diagnosis]).drop_duplicates()

# Output to CSV
problematic_records.to_csv("data_quality_report.csv", index=False)

print("Data quality audit complete. Problematic records:")
print(problematic_records)