#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset [x]
#The net total amount of "Profit/Losses" over the entire period[x]
#The average of the changes in "Profit/Losses" over the entire period[x]
#The greatest increase in profits (date and amount) over the entire period[x]
#The greatest decrease in losses (date and amount) over the entire period[x]

#read csv file
import os
import csv

#where is file located
csvpath = os.path.join("Homework","python-challenge","Instructions","PyBank","Resources", "budget_data.csv")

#Create lists and variables
date = []
profit_loss = []
#create new list that holds month and value for min/max

#print(csvpath)

# Open the CSV
with open(csvpath, newline="") as csvfile:
    # skip header row
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #put dates in date list
        #dollar values are in string and int
        #convert to int before adding to list
        date.append(row[0])
        x = int(row[1])
        profit_loss.append(x)
monthtotal = len(date) #length of list
nettotal = sum(profit_loss) #iterate over file and convert item to int
avg_change = nettotal/monthtotal
print(str(monthtotal) + " months")
print(str(nettotal) + " total dollars")
print("average change is " + str(avg_change))
print("greatest increase " + str(max(profit_loss))) #print month as well
print("greatest decrease " + str(min(profit_loss))) #print month as well


# Print results to text file
print(str(monthtotal) + " months", file=open("output.txt", "a"))
print(str(nettotal) + " total dollars", file=open("finaloutput.txt", "a"))
print("average change is " + str(avg_change), file=open("finaloutput.txt", "a"))
print("greatest increase " + str(max(profit_loss)), file=open("finaloutput.txt", "a"))
print("greatest decrease " + str(min(profit_loss)), file=open("finaloutput.txt", "a"))