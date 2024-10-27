import csv

file_path: str = 'exemplo.csv'

csv_file: list = []

with open(file=file_path, mode="r", encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        csv_file.append(row)
        
print(csv_file)