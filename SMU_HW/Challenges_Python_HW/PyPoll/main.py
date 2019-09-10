#create a variable for total votes and a dictionary for poll data
total_votes = int(0)
poll = {}
#imprt the data, hardcode the file (needs to be changed to work on another device), and prep data for analysis
import os
import csv
file = 'C:/Users/sadva/SMU_Coursework/SMU_HW/Challenges_Python_HW/PyPoll/election_data.csv'
with open (file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #calculate total votes
        total_votes += 1
        #add data to poll dictionary, each candidate gets a count of votes to them
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
#print total votes
print(
    "",
    "Election Results",
    "-------------------------",
    "Total Votes:", total_votes,
    "-------------------------",
)
#calculate and print each candidate with percentage and number of votes to them
for candidate in poll:
    print(candidate, ":", round(poll[candidate]/total_votes*100, 1), "% (", poll[candidate], ")")
print("-------------------------")
#calculate and print winner of the election
for candidate in poll:
    if poll[candidate] >= total_votes/2:
        print("Winner:", candidate)
#write data in a seperate text file
text = 'C:/Users/sadva/SMU_Coursework/SMU_HW/Challenges_Python_HW/PyPoll/output.txt'
with open (text, 'w') as textfile:
    textfile.write("\n")
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write("Total Values:" + str(total_votes) + "\n")
    textfile.write("-------------------------\n")
    for candidate in poll:
        textfile.write(str(candidate) + ":" + str(round(poll[candidate]/total_votes*100 + 1)) + "% (" + str(poll[candidate]) + ")\n")
    textfile.write("-------------------------\n")
    for candidate in poll:
        if poll[candidate] >= total_votes/2:
            textfile.write("Winner:" + str(candidate))