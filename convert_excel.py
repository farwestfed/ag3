import pandas as pd

# Read the Excel file
print("Reading Excel file...")
df = pd.read_excel('army_wx_data.xlsx')

# Print information about the data
print("\nData Overview:")
print(f"Shape: {df.shape}")
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Save to CSV for use in our React app
df.to_csv('ag3-dash/public/army_wx_data.csv', index=False)
print("\nSaved to ag3-dash/public/army_wx_data.csv") 