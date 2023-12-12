# Import modules os and csv

import os
import csv

# Set the path for PyPoll Election Data csv

PyPollcsv = os.path.join("..", "Resources", "election_data.csv")

# Create variable lists 
                    
count = 0
candidates = {}
vote_count = []
vote_percent = []

# with open(PyPollcsv, encoding='utf-8') as csvfile:
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)
    
    # Calculate the total number of votes cast 
    for row in csvreader:
        count = count + 1
        candidate_name = row[2]
        try:
            candidates[candidate_name] += 1 
        except: 
            candidates[candidate_name] = 1 
        
# Create output for calculation of the total votes, percentage, and voter count for each candidate  
text_output = "Election Results\n"
text_output += "----------------------------\n"
text_output += f"Total Votes: {count}\n"
text_output += "----------------------------\n"

winner = ["", 0]
for candidate,votes in candidates.items(): 
    percentage = (votes / count) * 100
    text_output += f"{candidate}: {percentage: .3f}% ({votes})\n"
    
    if votes > winner [1]:
        winner [1] = votes
        winner [0] = candidate 
        
text_output += "----------------------------\n"
text_output += f"Winner: {winner [0]}\n"
text_output += "----------------------------\n"
                             
print (text_output)

with open("PyPoll Analysis.txt","w") as outputFile: 
    outputFile.write (text_output) 
