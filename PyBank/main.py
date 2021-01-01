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

#net total of profit/losses
#want each item 1 from each row, make them into numbers and then add value
    net_total = 0
    for row in csv_reader:
        profit_loss = int(row[1])
        net_total = net_total + profit_loss
    print(f'Net Total: ${net_total}')
    
    for row in csv_reader:
        print(row)
# %%
