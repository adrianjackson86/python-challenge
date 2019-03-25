# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast[x]
# A complete list of candidates who received votes[x]
# The percentage of votes each candidate won[]
# The total number of votes each candidate won[x]
# The winner of the election based on popular vote.[]



#read csv file
import os
import csv

#where is file located
csvpath = os.path.join("Homework","python-challenge","Instructions","PyPoll","Resources", "election_data.csv")

#Create lists and variables
votes = []
candidates = []
winner = []
votetotal = 0
votepercent_candidate = 0
votetotal_candidate = 0
li = 0
khan = 0
correy = 0
tooley = 0

# put candidates into a dictionary
# length of column 0 will give vote total
# county does not matter
# unique values in column 2 are candidates
# {'Li', 'Khan', 'Correy', "O'Tooley"}

#print(csvpath)
# put candidates in dictionary
canddict = {"candidates":["Li","Khan","Correy","O'Tooley"]}
#print({canddict["candidates"][0]})

# Open the CSV
with open(csvpath, newline="") as csvfile:
#     # skip header row
#     # Voter ID,County,Candidate [0,1,2]
     next(csvfile)
     csvreader = csv.reader(csvfile, delimiter=",")
     for row in csvreader:
         votes.append(row)
         candidates.append(row[2])
         if row[2]=="Li":
             li = li + 1
         elif row[2]=="Khan":
             khan = khan + 1
         elif row[2]=="Correy":
             correy = correy + 1
         elif row[2]=="O'Tooley":
             tooley = tooley + 1
votetotal = len(votes)

# scan list to find unique names, 
# uniquelist = set(candidates) 
# print(uniquelist)

#print(f'{another_actor["name"]} was in {another_actor["best movies"][0]}')

#print(votetotal)
#print(li) # total votes for Li
#print(format((li/votetotal)*100,'.3f')) # % of Li's votes
#print({canddict["candidates"][0]})
khan_percent = format((khan/votetotal)*100,'.3f')
li_percent = format((li/votetotal)*100,'.3f')
correy_percent = format((correy/votetotal)*100,'.3f')
tooley_percent = format((tooley/votetotal)*100,'.3f')

# winner = [khan,li,correy,tooley]
# winner = max[winner]


# Print results to text file
print("Election Results\n-----------------------------", file=open("electionoutput.txt", "a"))
print("Total Votes: " + str(votetotal) + "\n-----------------------------", file=open("electionoutput.txt", "a"))
print(f'{canddict["candidates"][1]}: ' + khan_percent + "% (" + str(khan) + ")",file=open("electionoutput.txt", "a"))
print(f'{canddict["candidates"][2]}: ' + correy_percent + "% (" + str(correy) + ")",file=open("electionoutput.txt", "a"))
print(f'{canddict["candidates"][0]}: ' + li_percent + "% (" + str(li) + ")",file=open("electionoutput.txt", "a"))
print(f'{canddict["candidates"][3]}: ' + tooley_percent + "% (" + str(tooley) + ")",file=open("electionoutput.txt", "a"))
print("-----------------------------", file=open("electionoutput.txt", "a"))
print("Winner: ", file=open("electionoutput.txt", "a"))
print("-----------------------------", file=open("electionoutput.txt", "a"))