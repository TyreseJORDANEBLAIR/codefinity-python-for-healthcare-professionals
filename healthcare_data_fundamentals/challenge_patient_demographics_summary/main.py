import pandas as pd

data = pd.DataFrame({
    "age": [34, 58, 47, 29, 53],
    "gender": ["Female", "Male", "Female", "Male", "Female"],
    "diagnosis": ["Hypertension", "Diabetes", "Asthma", "Healthy", "Cancer"]
})
# Calculate average age
# average_age = ...
# print(f"Average age of patients: {average_age:.2f}")
average_age = data['age'].mean()
print(f"Average age of patients: {average_age:.2f}")
# Count number of patients by gender
# gender_counts = ...
# print("Number of patients by gender:")
# for gender, count in gender_counts.items():
#     print(f"  {gender}: {count}")
gender_counts = data['gender'].value_counts()
print("Number of patients by gender:")
for gender, count in gender_counts.items():
    print(f" {gender}: {count}")