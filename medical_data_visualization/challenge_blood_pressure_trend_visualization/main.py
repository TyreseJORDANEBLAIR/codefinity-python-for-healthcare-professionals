import pandas as pd
import matplotlib.pyplot as plt

def plot_bp_trend(df):
    df = df.copy()
    # Ensure 'date' column is datetime
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(8, 4))
    plt.plot(df['date'], df['blood_pressure'], marker='o', linestyle='-', color='blue')
    plt.xlabel("Date")
    plt.ylabel("Blood Pressure (mmHg)")
    plt.title("Blood Pressure Trend")
    plt.tight_layout()
    plt.savefig("bp_trend.png")
    plt.show()
    plt.close()

# Example usage
data = {
    "date": [
        "2024-01-01", "2024-01-10", "2024-01-20", "2024-02-01",
        "2024-02-15", "2024-03-01", "2024-03-10", "2024-03-20"
    ],
    "blood_pressure": [120, 122, 118, 125, 130, 128, 126, 124]
}
df = pd.DataFrame(data)
plot_bp_trend(df)