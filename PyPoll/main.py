import os
import csv

total_votes = 0

#create empty lists
candidates = []
num_votes = []
vote_percent = []
winners = []

#dictionary candidate and num_votes.
poll = {}

# # Path to collect data from the Resources folder
Path_Of_Election_Data_csv = os.path.join("Resources", "election_data.csv")\

# Open and read csv
with open(Path_Of_Election_Data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
# dictionary keys and values for candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

for v in num_votes:
    vote_percent.append(round(v/total_votes*100, 3))

# zips candidates, num_votes, vote_percent into tuples
Zip_ = list(zip(candidates, num_votes, vote_percent))

for name in Zip_:
    if max(num_votes) == name[1]:
        winners.append(name[0])

# makes winner_list a str with the first entry
winner = winners[0]

#in case of multiple winners/tie
if len(winners) > 1:
    for w in range(1, len(winners)):
        winner = winner + ", " + winners[w]

#Location of output file
output_file = os.path.join("Analysis", "pypoll_analysis.txt" )

#write to the txtfile
with open(output_file, 'w') as txtfile:
    txtfile.write(f'')   
    txtfile.write("Election Results")
    txtfile.write(f'\n-------------------------')
    txtfile.write(f'\nTotal Votes: {total_votes}')
    txtfile.write(f'\n-------------------------')
    for entry in Zip_:
        txtfile.write(f'\n {entry[0]}: {(entry[2])}%  ({(entry[1])})') 
    txtfile.write(f'\n-------------------------')
    txtfile.write(f'\nWinner: : {winner} ')
    txtfile.write(f'\n-------------------------')   


#Print for testing
print("")
print("")
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{Zip_[0][0]}: {Zip_[0][2]}% ({Zip_[0][1]})")
print(f"{Zip_[1][0]}: {Zip_[1][2]}% ({Zip_[1][1]})")
print(f"{Zip_[2][0]}: {Zip_[2][2]}% ({Zip_[2][1]})")
print(f"{Zip_[3][0]}: {Zip_[3][2]}% ({Zip_[3][1]})")
print("-------------------------")
print(f"Winner: {winner} by a landslide")
print("-------------------------")
print("")
print("")

