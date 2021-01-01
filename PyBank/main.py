# %%
import os
import csv
bankdata = os.path.join('..','Resources','budget_data.csv')
with open(bankdata) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #total number of months, meaning total number of rows in data
    csv_reader=list(csv_reader)
    count_months=csv_reader
    print(f'Number of Months: {len(count_months)}')

    for row in csv_reader:
        print(row)
# %%
