#  Election Project
# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate received
# 5 The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

#Candidate Options and Votes
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here
    file_reader = csv.reader(election_data)

# Read the header row.
    headers = next(file_reader)
# print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name =row[2]
    
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

             # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0    
# print(candidate_votes)

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1




