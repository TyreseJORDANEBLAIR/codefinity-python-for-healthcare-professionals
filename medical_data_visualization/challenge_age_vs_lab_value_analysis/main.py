import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example DataFrame
data = {
    'age': [22, 34, 45, 51, 60, 38, 41, 55, 28, 65],
    'lab_result': [3.1, 3.7, 4.0, 4.6, 5.1, 3.6, 4.2, 4.9, 3.4, 5.3]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
# Scatter using df columns
sns.scatterplot(x=df['age'], y=df['lab_result'], color='blue', s=60)
# Trendline only
sns.regplot(x='age', y='lab_result', data=df, scatter=False, color='red', line_kws={"linewidth":2})
plt.xlabel('Age (years)')
plt.ylabel('Lab Result')
plt.title('Scatter Plot of Age vs. Lab Result with Trendline')
plt.tight_layout()
plt.show()