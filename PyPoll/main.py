#%%
import os
import csv
polldata = os.path.join('..','Resources','election_data.csv')
with open(polldata) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #total number of votes cast
    candidates_list=list(csv_reader)
    number_of_votes = len(candidates_list)
    print(f'Total Votes: {number_of_votes}')
    
#candidates' individual votes and percentages
    candidates =[]
    vote_count_0 = 0
    vote_count_1 = 0
    vote_count_2 = 0
    vote_count_3 = 0
    
    #collecting all names
    for row in candidates_list:
        name = row[2]
        candidates.append(name)
        
    #collecting all list of unique names
    unique_names = []    
    for x in candidates:
        if x not in unique_names:
            unique_names.append(x)
    print(unique_names)
        
    for row in candidates_list:
        name = row[2]
        if name == unique_names[0]:
            vote_count_0 = vote_count_0 + 1
        if name == unique_names[1]:
            vote_count_1 = vote_count_1 + 1
        if name == unique_names[2]:
            vote_count_2 = vote_count_2 + 1
        if name == unique_names[3]:
            vote_count_3 = vote_count_3 + 1
            
    print (vote_count_0)
    print (vote_count_1)
    print (vote_count_2)
    print (vote_count_3)


    
# %%
