
import csv
import re

with open(r'dataset\datasets.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Headers are lines 1-44 (indices 0-43)
headers = [lines[i].strip() for i in range(44) if lines[i].strip()]

# Data starts at line 47 (index 46), skip "Column44" label at index 45
data_values = [lines[i].strip() for i in range(46, len(lines)) if lines[i].strip()]

print(f"Headers: {len(headers)}")
print(f"Data values: {len(data_values)}")

num_cols = 44
num_rows = len(data_values) // num_cols

print(f"Rows: {num_rows} (44 columns each)")

with open(r'dataset\data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    
    for i in range(num_rows):
        start = i * num_cols
        end = start + num_cols
        row = data_values[start:end]
        writer.writerow(row)

print(f"Created data.csv successfully!")
