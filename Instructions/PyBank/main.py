#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#read csv file
import os
import csv

#where is file located
csvpath = os.path.join("Homework","Instructions","PyBank","Resources", "budget_data.csv")
#csvpath = "C:/Users/axj2722/GTATL201902DATA3/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv"
#Create lists and variables
date = []
profit_loss = []
monthtotal = 0
totalamount = 0
avgprofit = 0


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #put dates in date list
        date.append(row[0])
        #put profit values in list
        profit_loss.append(row[1])
        monthtotal = len(date) #lenght of list
        avgprofit = totalamount/len(totalamount)


cleaned_csv = zip(monthtotal)
finalreport = os.path.join("Homework","Instructions","PyBank", "FinalReport.csv") 

with open(finalreport,'w',newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow("Total Months")
    writer.writerows(cleaned_csv)


# clean_csv = zip(title,price,subscribers,percent,review_percent)
#     output_file = "cd \Activities\11-Stu_UdemyZip\Resources\web_final.csv"
#     #"C:\Users\axj2722\GTATL201902DATA3\03-Python\2\Activities\11-Stu_UdemyZip\Resources\web_final.csv"
#     #os.path.join("..","Resources","web_final.csv")

#     with open(output_file,"w",newline="") as datafile:
#         writer = csv.writer(datafile)
#         writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", "Percent of Reviews"])
#         writer.writerows(clean_csv)
        