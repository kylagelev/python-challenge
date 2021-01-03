#%%
import os
import csv
polldata = os.path.join('..','Resources','election_data.csv')
with open(polldata) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #total number of votes cast
    csv_reader=list(csv_reader)
    number_of_votes = len(csv_reader)
    print(f'Total Votes: {number_of_votes}')
    
#candidates' individual votes and percentages
    #want to alphabetize list in order to input unique candidate names and the counted votes for each respective individual
    alphabetized_candidates = sorted(csv_reader, key=lambda x: x[2])

    candidates = []
    name = 0
    for row in alphabetized_candidates:
        if row[2] != name:
            name = row[2]
            candidates.append(name)
            pass
        else:
            name = row[2]
            pass
        
            
        
        print(candidates)
    #for row in csv_reader:
        #print(row)
# %%
