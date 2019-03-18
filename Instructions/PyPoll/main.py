# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast[]
# A complete list of candidates who received votes[]
# The percentage of votes each candidate won[]
# The total number of votes each candidate won[]
# The winner of the election based on popular vote.[]



#read csv file
import os
import csv

#where is file located
csvpath = os.path.join("Homework","python-challenge","Instructions","PyPoll","Resources", "election_data.csv")

#Create lists and variables
votetotal = 0
candidates = {}
votepercent_candidate = 0
votetotal_candidate = 0

# put candidates into a dictionary
# length of column 0 will give vote total
# county does not matter
# unique values in column 2 are candidates


print(csvpath)

# Open the CSV
# with open(csvpath, newline="") as csvfile:
#     # skip header row
#     # Voter ID,County,Candidate [0,1,2]
#     next(csvfile)
#     csvreader = csv.reader(csvfile, delimiter=",")
   # for row in csvreader: