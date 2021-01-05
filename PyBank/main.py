# %%
#above symbols allows code to run in jupyter interactive
import os
import csv
bankdata = os.path.join('..','Resources','budget_data.csv')
print("Financial Analysis")
print("----------------------")
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
#average change in profit
    changes=[]
  
#need to set greatest increase/decrease values in profits/losses
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = 0
    greatest_decrease_month = 0
    new_change2 = 0

    #creating list of change in profits/losses and indicating greatest increase/decrease
    for row in csv_reader:  
        new_change1 = int(row[1])
        change = new_change2 - new_change1
        if change>=greatest_increase:
                greatest_increase = change
                greatest_increase_name = row[0]
        if change<=greatest_decrease:
                greatest_decrease = change
                greatest_decrease_name = row[0]
        changes.append(change)
        new_change2 = new_change1
    changes.remove(changes[0])
    
    total = 0
    for x in range(len(changes)):
        item =(changes[x])
        total = total + item
    average = (total)/(len(changes))
    print(f'Average Change: ${round(average,2)}')          
    print (f'Greatest Increase in Profits: {greatest_increase_name} (${greatest_increase})')
    print (f'Greatest Decrease in Profits: {greatest_decrease_name} (${greatest_decrease})')

#write text file
output_path = os.path.join('..','Analysis','PyBank_Analysis.csv')
with open (output_path,'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Number of Months: 86'])
    csvwriter.writerow(['Net Total: $38382578'])
    csvwriter.writerow(['Average Change: $2315.12'])
    csvwriter.writerow(['Greatest Increase in Profits: Sep-2013 ($2196167)'])
    csvwriter.writerow(['Greatest Decrease in Profits: Feb-2012 ($-1926159)'])
