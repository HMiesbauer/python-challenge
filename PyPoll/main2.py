#assign variables
total_votes_cast = 0
candidate_list = [] #list for names that got votes
stockham_votes = 0
deGette_votes = 0
doane_votes = 0
stockham_percentage = 0
deGette_percentage = 0
doane_percentage = 0


#I have 3 columns so index 0, 1, 2
import csv

#set file path
election_data_csv = ("Resources/election_data.csv")

#open file
with open(election_data_csv) as csv_file:
    election_results = csv.reader(csv_file)

#skip header row
    header = next(election_results)

#calculate total votes cast
   
    for row in election_results:
        total_votes_cast +=1

#get list of candidates who got votes 

            
# get candidate names and count votes using a loop so can use vote counts for variables in print statement(for loop code from chatgpt, my variables)
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

#Who received the most votes(winner)  
candidate_list_votes = [(stockham_votes), (deGette_votes), (doane_votes)] # list to get the candidate votes but need to pair with names
most_votes = candidate_list_votes.index(max(candidate_list_votes))
winner = candidate_list_votes[most_votes] 
print(winner)

#print output f statement from PyBank created with tutor David Chao
output = f"""
Election Results
-------------------------
Total Votes: {total_votes_cast:,}
-------------------------
Charles Casper Stockham: {stockham_percentage:.2f}% ({stockham_votes})
Diana DeGette: {deGette_percentage:.2f}% ({deGette_votes})
Raymon Anthony Doane: {doane_percentage:.2f}% ({doane_votes})
-------------------------
Winner: Diana DeGette
-------------------------
"""

#save output to file
with open("Analysis/election_results.txt", "w") as outfile:
    outfile.write(output)
