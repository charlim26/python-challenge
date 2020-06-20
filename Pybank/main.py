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

# Data list 
Total_Months = []
Profit_loss = 0



# Open and loop through data
with open(pybankin_csv, 'r') as pybudget:

# Parse data
    csvreader = csv.reader(pybudget, delimiter=',')

#Read the header data
    pybankin_header = next(csvreader)
    for data in csvreader:

# Store Data for Financial Analysis Summary
        Total_Months.append(data[0])
        Profit_loss.append(int(data[1])
        
        #AverageChange 


# Calculations for Financial Analysis
TotalMonths = len(Total_Months)
Total_ProfitLoss = sum(Profit_loss)   
#Average_change = sum(Averagechange)/len(Averagechange)
#Greatest_Increase = max(Averagechange)
#Greatest_Decrease = min(Averagechange)


# Display Financial Analysis Summary
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(TotalMonths)) 
#print("Total: $" + str(Total_Profitloss))
#print("Average Change:  $" + str(Average_change))
#print("Greatest Increase:  $" + str(Greatest_Increase))
#print("Greatest Decrease:  $" + str(Greatest_Decrease))