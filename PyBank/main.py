import os
import csv
bankdata = os.path.join('..','Resources','budget_data.csv')
with open(bankdata) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        print(row)
