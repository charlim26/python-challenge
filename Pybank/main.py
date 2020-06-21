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

#Open and loop through data
with open(pybankin_csv, 'r') as pybudget:

    # Set variables 
    Total_Months = []
    Profitloss_Total = []
    Profit_loss = []
    Profitloss_Total = 0
    average_change = 0
    year_change = []
    change = 0
   
  
    #Parse data
    csvreader = csv.reader(pybudget, delimiter=',')

    #Read the header data
    pybankin_header = next(csvreader)
    for data in csvreader:

        # Store Data for Financial Analysis Summary
        Total_Months.append(data[0])
        Profit_loss.append(int(data[1]))
        Profitloss_Total += int(data[1]) 
         
    # Average change   
    for i in range(1,len(Profit_loss)):
        change = (Profit_loss[i]) - (Profit_loss[i-1])
        year_change.append(change)  
        Total_Change = (sum(year_change))
                     

# Calculations for Financial Analysis Print
TotalMonths = len(Total_Months)
Average_Change = round(Total_Change/((len(Total_Months))-1),2)
Greatest_Increase = max(year_change)
Greatest_Inc_Index = year_change.index(Greatest_Increase)+1
Greatest_Decrease = min(year_change)
Greatest_Dec_Index = year_change.index(Greatest_Decrease )+1

# Display Financial Analysis Summary
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {str(TotalMonths)}")
print(f"Total: ${str(Profitloss_Total)}")
print(f"Average Change: ${str(Average_Change)}")
print(f"Greatest Increase: {Total_Months[Greatest_Inc_Index]} (${str(Greatest_Increase)})")
print(f"Greatest Increase: {Total_Months[Greatest_Dec_Index]} (${str(Greatest_Decrease )})")

analysis_file = os.path.join ("Pybank","Analysis","FinancialAnalysis.txt")
with open(analysis_file, 'w') as FinancialAnalysis:
    FinancialAnalysis.write("Financial Analysis\n")
    FinancialAnalysis.write("--------------------------\n")
    FinancialAnalysis.write(f"Total Months: {str(TotalMonths)}\n")
    FinancialAnalysis.write(f"Total: ${str(Profitloss_Total)}\n")
    FinancialAnalysis.write(f"Average Change: ${str(Average_Change)}\n")
    FinancialAnalysis.write(f"Greatest Increase: {Total_Months[Greatest_Inc_Index]} (${str(Greatest_Increase)})\n")
    FinancialAnalysis.write(f"Greatest Increase: {Total_Months[Greatest_Dec_Index]} (${str(Greatest_Decrease )})\n")