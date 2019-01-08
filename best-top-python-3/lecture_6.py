import csv

with open('example.csv') as f:
    rows = csv.reader(f, delimiter='.')
    for row in rows:
        print(row)