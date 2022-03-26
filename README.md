# Election_Analysis

## Project Overview
Based on the election results data that was provided to the Colorado Board of Elections, an audit of the election is required. Because of the variety of voting methods, including mail-in ballots, punch cards, and direct recording electronic counting machines, it is imperative that the certification process is as automated as possible. Below is a list of the deliverables required by the commission. 
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received the vote.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of voters from each county from the total amount.
8. Determine the county with the highest turnout. 

 
## Resources
- Data Source: elections_results.csv
- Software: Python 3.9.7, Visual Studio Code 1.65.2

## Results
According to the analysis of the election:
- There were 369,711 votes cast on the election.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

- The winner of the election was:
  - Diana DeGette with 73.8% of total voters. 

- The counties involved in the elections were:
  - Jefferson county with 38, 855 voters and 10.5% of the total voters.
  - Denver county with 306, 055 voters and 82.8% of the total voters.
  - Arapahoe county with 24, 801 voters and 6.7% of the total voters.

- The county that had the largest turnout:
  - Denver with 82.8% total participants

## Challenge Summary
It is possible to use the script written for the Colorado election for any other election. The script is designed so that it can be readily adapted with variations to accommodate a variety of candidates and/or counties. Here is an example of how the script can be utilized in other elections.

###### Sample Changes
As long as the file "election_results_county.csv" is located within the same "Resources" folder, then another election can be done using the existing script as long as it is given the correct path. For example, if another election is done, and the file "election_results_county.csv" is used, then the following script needs to be altered.

```
# Create a filename variable to a direct or indirect path to the file
file_to_load = os.path.join('Resources', 'election_results_county.csv')
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')
```

In addition, if the election board does not wish to see the breakdown of the county results, then the script below can be used. 
```

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