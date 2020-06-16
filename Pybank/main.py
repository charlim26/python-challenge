import os
import csv
budget_path = os.path.join('..', "Resources","budget_data.csv")
with open(budget_path) as csvfile:
 budget_reader = csv.reader(csvfile, delimiter=',')
 budget_header = next (csvfile)
print(f"Csv Header: {budget_header}")



