import csv
from pathlib import Path

# Paths to files
directory = Path('ideas_for_test/work_with_csv')
file1 = directory / 'file1.csv'
file2 = directory / 'file2.csv'
result_file = directory / 'result_Baskakov.csv'

# Reading data from the first file
with file1.open(newline='', encoding='utf-8') as f1:
    reader1 = csv.reader(f1)
    data1 = list(reader1)

# Reading data from the second file
with file2.open(newline='', encoding='utf-8') as f2:
    reader2 = csv.reader(f2)
    data2 = list(reader2)

# Combining data from both files
combined_data = data1 + data2

# Removing duplicates by converting to a set
unique_data = [list(x) for x in set(tuple(row) for row in combined_data)]

# Writing the unique data to a new CSV file
with result_file.open('w', newline='', encoding='utf-8') as result:
    writer = csv.writer(result)
    writer.writerows(unique_data)

print(f"Result has been saved to {result_file}")