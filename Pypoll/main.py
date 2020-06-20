#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------



import os
import csv
pypoll_csv = os.path.join("Pypoll","Resources","election_data.csv")

# Open and read csv file
with open(pypoll_csv,'r' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Read the first row of the header
    csv_header = next(csvfile)
 
    # Set variables 
    Votes = []
    Vote_Total = 0
    
    
    #Read the header data
    pypoll_header = next(csvreader)
    for data in csvreader:

        # Store Data for Financial Analysis Summary
        Votes.append(int(data[0])

     
#Calc

Vote_Total = len(Votes)


print(Vote_Total)
 



