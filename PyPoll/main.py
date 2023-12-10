import os
import csv

# Define variables
total_votes = 0 
candidate_counts = {}

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csv_reader:

        #Count total votes
        total_votes += 1

        #Count votes for each candidate
        candidate = row[2]
        if candidate in candidate_counts:
            candidate_counts[candidate] +=1
        else:
            candidate_counts[candidate] = 1

    #Define the winner based on popular vote 
    winner = max(candidate_counts, key = candidate_counts.get)
    
#Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {total_votes}")
print("-------------------------")

#Iterate through candidates and print their statistics
for candidate, votes in candidate_counts.items():
    percentage = (votes/total_votes)*100
    print(f"{candidate}:{percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write into a text file named pypoll.txt to be stored in the analysis folder
txt_file_path = os.path.join("analysis", "pypoll.txt")
with open(txt_file_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    # Iterate through candidates and write their statistics
    for candidate, votes in candidate_counts.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")