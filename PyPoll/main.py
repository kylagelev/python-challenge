import os
import csv
polldata = os.path.join('..','Resources','election_data.csv')
with open(polldata) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        print(row)