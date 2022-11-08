# imports
import os
import csv
from collections import Counter

# absolute file path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# source data
budget_data = os.path.join(THIS_FOLDER, 'Resources', 'election_data.csv')
# output file
PyPoll_analysis = os.path.join(THIS_FOLDER, 'analysis', 'PyPoll_analysis.txt')

# var declarations and initializations
total_votes = 0
candidate_name = ""
candidate_name_check = ""
candidates = []
candidate_votes = {}
candidate_votes_tally = 0
winning_candidate = "Person"
percentage_of_vote = 0.


# safely open file
with open(budget_data) as csvfile:
    
    # perform calculations on CSV
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip header row
    next(csvreader)

    # perform calculations
    for row in csvreader:

        # count the total votes (also use it as the key for the candidate_votes dict)
        total_votes+=1

        #add new candidate vote to dict
        candidate_votes[total_votes] = row[2]
        

voting_results = Counter(candidate_votes.values())
    
# print analysis to terminal
print("Election Results\n")
print("----------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("----------------------------\n")

# loop through voting_results dict and print results
for item in voting_results.items():
    print(f"{item[0]}: {str(round((int(item[1])/total_votes)*100,3))}% ({item[1]})\n")

print("----------------------------\n")

# get the max value from voting_results dict and print winner
print(f"Winner: {max(voting_results, key=voting_results.get)}\n")

print("----------------------------\n")

# write analysis to a new file as output
with open(PyPoll_analysis,'w',encoding='utf-8') as file_out:
    file_out.write("Election Results\n")
    file_out.write("----------------------------\n")
    file_out.write(f"Total Votes: {total_votes}\n")
    file_out.write("----------------------------\n")

    # loop through voting_results dict and write results
    for item in voting_results.items():
        file_out.write(f"{item[0]}: {str(round((int(item[1])/total_votes)*100,3))}% ({item[1]})\n")

    file_out.write("----------------------------\n")

    # get the max value from voting_results dict and write winner
    file_out.write(f"Winner: {max(voting_results, key=voting_results.get)}\n")

    file_out.write("----------------------------\n")
