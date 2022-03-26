# Adds our dependencies.
import csv
import os

# filename variable is created to a direct or indirect path to the file
file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# Initializes a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# county list and county votes dictionary.
county_options = []
county_votes = {}


# Tracks the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Tracks the largest county and county voter turnout.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Adds to the total vote count
        total_votes = total_votes + 1

        # Gets the candidate name from each row.
        candidate_name = row[2]

        # Extracts the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Adds the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # tracks the existing candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Adds a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # checks that the county does not match any existing county in the county list.
        if county_name not in county_options:

            # Adds the existing county to the list of counties.
            county_options.append(county_name)

            # tracks the existing county's vote count.
            county_votes[county_name] = 0    

        # Adds a vote to that county's vote count.
        county_votes[county_name] += 1


# Saves the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Prints the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Gets the county from the county dictionary.
    for county_name in county_votes:
        # Retrieves the county vote count.
        c_votes = county_votes[county_name]
        # Calculates the percentage of votes for the county.
        c_votes_percentage = float(c_votes) / float(total_votes) * 100

        # Prints the county results to the terminal.
        county_results = (
            f'{county_name}: {c_votes_percentage:.1f}% ({c_votes:,})\n')
        print(county_results, end='')

        # Saves the county votes to a text file.
        txt_file.write(county_results)

        # Determines the winning county and get its vote count.
        if (c_votes > winning_county_votes) and ( c_votes_percentage > winning_county_percentage ):
            winning_county = c_votes
            winning_county_percentage = c_votes_percentage
            winning_county = county_name

    # Prints the county with the largest turnout to the terminal.
    winning_county_summary = (
        f' \n'
        f"-------------------------\n"
        f'Largest County Turnout: {winning_county}\n'
        f"-------------------------\n"
    )
    
    print(winning_county_summary)

    # Saves the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Saves the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieves vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Prints each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Saves the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determines the winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Prints the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Saves the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)