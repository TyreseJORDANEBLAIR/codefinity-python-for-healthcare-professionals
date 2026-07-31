import pandas as pd

data = {
    'diagnosis': [
        'Hypertension', 'Diabetes', 'Hypertension', 'Asthma', 'Diabetes',
        'Hypertension', 'Asthma', 'Asthma', 'Diabetes', 'Hypertension'
    ]
}
df = pd.DataFrame(data)

counts = df['diagnosis'].value_counts().head(3)
for diag, count in counts.items():
    print(f"{diag} {count}")
