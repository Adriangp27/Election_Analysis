# Add our dependencies.
import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize list to hold candidates.
candidate_options = []
#Initialize dictionary to hold candidate names with their votes
candidate_votes = {}

# Winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Adding the total vote for each row iteration
        total_votes += 1

        # find the candidate name on the data set
        candidate_name = row[2]

        # Checking if the candidates is already on the list
        if candidate_name not in candidate_options:

            # Adding the candidates to the list
            candidate_options.append(candidate_name)

            # Tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        # Adding votes for each candidate
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]

        # Calculating the percentages
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate results, number of votes and percentages 
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning vote count and candidate
        # Determine if the votes is greater than the winning count
        # Set winning candidate name to winning_candidate variable
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Set and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)