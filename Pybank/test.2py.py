#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

import os
import csv

pybankin_csv = os.path.join("Pybank","Resources","budget_data.csv")

# Set variables 
Total_Months = []
Profitloss_Total = []
Profitloss_Total = 0


#Open and loop through data
with open(pybankin_csv, 'r') as pybudget:

    # Parse data
    csvreader = csv.reader(pybudget, delimiter=',')

    # Read the header data
    pybankin_header = next(csvreader)
    for data in csvreader:

        # Store Data for Financial Analysis Summary
        Total_Months.append(data[0])
        Profitloss_Total += int(data[1]) 


# Calculations for Financial Analysis
TotalMonths = len(Total_Months)



# Display Financial Analysis Summary
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(Profitloss_Total)}")
