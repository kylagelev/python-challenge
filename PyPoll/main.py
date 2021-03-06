#%%
#above symbol allows code to run in jupyter interactive from vscode
import os
import csv
polldata = os.path.join('..','Resources','election_data.csv')
with open(polldata) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    
    print(f'Election Results')
    print(f'-------------------')

#total number of votes cast
    candidates_list=list(csv_reader)
    number_of_votes = len(candidates_list)
    print(f'Total Votes: {number_of_votes}')
    
    print(f'-------------------')
    
#candidates' individual votes and percentages
    candidates =[]
    vote_count_0 = 0
    vote_count_1 = 0
    vote_count_2 = 0
    vote_count_3 = 0
    
    for row in candidates_list:
        name = row[2]
        candidates.append(name)
        
    #collected all list of unique names
    unique_names = []    
    for x in candidates:
        if x not in unique_names:
            unique_names.append(x)
        
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

    percentage_0 = (vote_count_0/number_of_votes)*100
    percentage_1 = (vote_count_1/number_of_votes)*100
    percentage_2 = (vote_count_2/number_of_votes)*100
    percentage_3 = (vote_count_3/number_of_votes)*100
    
    print(f'{unique_names[0]}: {round(percentage_0,2)}00% ({vote_count_0})')
    print(f'{unique_names[1]}: {round(percentage_1,2)}00% ({vote_count_1})')
    print(f'{unique_names[2]}: {round(percentage_2,2)}00% ({vote_count_2})')
    print(f'{unique_names[3]}: {round(percentage_3,2)}00% ({vote_count_3})')

    print(f'-------------------')
    
#greatest votes = winner
    individual_votes = []
    individual_votes.append(vote_count_0)
    individual_votes.append(vote_count_1)
    individual_votes.append(vote_count_2)
    individual_votes.append(vote_count_3)
    
    #want to order from greatest to least (descending order)
    sorted_individual_votes = sorted(individual_votes, reverse = True)
    
    if sorted_individual_votes[0] == vote_count_0:
        winner = unique_names[0]
        print(f'Winner: {winner}!')
    if sorted_individual_votes[0] == vote_count_1:
        winner = unique_names[1]
        print(f'Winner: {winner}!')
    if sorted_individual_votes[0] == vote_count_2:
        winner = unique_names[2]
        print(f'Winner: {winner}!')
    if sorted_individual_votes[0] == vote_count_3:
        winner = unique_names[3]
        print(f'Winner: {winner}!')

#write text file
output_path = os.path.join('..','Analysis','PyPoll_Analysis.txt')
with open (output_path,'w', newline = '') as txtfile:
    csvwriter = csv.writer(txtfile, delimiter =',')
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f'Total Votes: {number_of_votes}'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f'{unique_names[0]}: {round(percentage_0,2)}00% ({vote_count_0})'])
    csvwriter.writerow([f'{unique_names[1]}: {round(percentage_1,2)}00% ({vote_count_1})'])
    csvwriter.writerow([f'{unique_names[2]}: {round(percentage_2,2)}00% ({vote_count_2})'])
    csvwriter.writerow([f'{unique_names[3]}: {round(percentage_3,2)}00% ({vote_count_3})'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f'Winner: {winner}!'])
# %%
