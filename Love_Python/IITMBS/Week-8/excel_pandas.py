import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 35, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

 # Write the DataFrame to an Excel file
df.to_excel(r"C:\Users\HP\Book1_empty.xlsx", index=False)

# # Write to CSV
# df.to_csv("path/to/your/csv/file.csv", index=False)
