import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "diagnosis": ["Diabetes", "Diabetes", "Healthy", "Healthy", "Prediabetes", "Diabetes", "Prediabetes", "Healthy"],
    "glucose_level": [180, 175, 95, 90, 130, 200, 140, 100]
}
df = pd.DataFrame(data)

# Your code here
plt.figure(figsize=(8,6))
sns.boxplot(x="diagnosis", y="glucose_level", data=df)
plt.title("Glucose Level Comparison by Diagnosis")
plt.xlabel("Diagnosis Group")
plt.ylabel("Glucose Level (mg/dL)")
plt.show()