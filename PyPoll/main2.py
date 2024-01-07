#assign variables
total_votes_cast = 0
candidate_list = [] #list for names that got votes
stockham_votes = 0
deGette_votes = 0
doane_votes = 0
stockham_percentage = 0
deGette_percentage = 0
doane_percentage = 0
candidate_name = ""
vote_percentage = 0
candidate_votes = [] # list to get the votes per candidate
winner = ""

#I have 3 columns so index 0, 1, 2
import csv

#set file path
election_data_csv = ("Resources/election_data.csv")

#open file
with open(election_data_csv) as csv_file:
    election_results = csv.reader(csv_file)

#skip header row
    header = next(election_results)

#calculate total votes cast this works
   
    for row in election_results:
        total_votes_cast +=1

#get list of candidates who got votes - this doesnt work need list comphrehsion
        candidate_name = row[2]
        candidate_list.append(candidate_name)
    print(candidate_list)
            
# get candidate names and count votes using a loop put totals into the variables(for loop code from chatgpt, my variables)
with open(election_data_csv) as csv_file:
    election_results = csv.reader(csv_file)
    header = next(election_results)
    for row in election_results:
        candidate_name = row[2] 
        if candidate_name:
            if candidate_name == "Charles Casper Stockham":
                stockham_votes += 1
            elif candidate_name == "Diana DeGette":
                deGette_votes += 1
            elif candidate_name == "Raymon Anthony Doane":
                doane_votes += 1
      
#get % of votes each candidate won
    stockham_percentage = (stockham_votes / total_votes_cast) * 100
    deGette_percentage = (deGette_votes / total_votes_cast) * 100
    doane_percentage = (doane_votes / total_votes_cast) * 100

#Who received the most votes(winner)  - same code from line 36 just add in print statement for winner using max value from winner list 
                    



#print output
output = f"""
Election Results
-------------------------
Total Votes: {total_votes_cast:,}
-------------------------
Charles: {stockham_percentage} {stockham_votes}
Diane: {deGette_percentage} {deGette_votes}
Anthony: {doane_percentage} {doane_votes}
-------------------------
Winner: Diana DeGette
-------------------------
"""

#save output to file
with open("Analysis/election_results.txt", "w") as outfile:
    outfile.write(output)
