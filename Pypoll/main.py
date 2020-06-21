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

# Set variables 
Voteid = []
Results = []
Candidates = []

    # Open and read csv file
with open(pypoll_csv,'r' ) as polldata:

    csvreader = csv.reader(polldata, delimiter=',')
    pypoll_header = next(csvreader)
   
    for data in csvreader:

        # Store Data 
        Voteid.append(data[0])
        Candidates.append(str(data[2]))
         
        
        # Unique Candidates
    for i in Results:
        if Candidates not in Results: 
            Results[Candidates] + i
        else: 
            Results[Candidates] += i

   
TotalVotes = len(Voteid)
winner = max(Results, key=Candidates.itemgetter(1))
#UniqueCandidates = list(set(CandidateList))
#CandidateVotes = CandidateList.count(data[2])

# Display Election Summary
print("Election Results")
print("----------------------")
print(f"Total Votes: {str(TotalVotes)}")
print("----------------------")
print(f'Khan: {Results["Khan"] / TotalVotes:.3%} ({TotalVotes["Khan"]})')
print(f'Correy: {Results["Correy"] / TotalVotes:.3%} ({TotalVotes["Correy"]})')
print(f'Li: {Results["Li"] / TotalVotes:.3%} ({TotalVotes["Li"]})')
#print(f'"O'Tooley:" + '{Results['O'Tooley'] / TotalVotes:.3%} ({TotalVotes["O'Tooley"]})')
print("----------------------")
print(f"Winner: {str(winner)}")
print("----------------------")


analysis_file = os.path.join ("Pypoll","Analysis","ElectionAnalysis.txt")
with open(analysis_file, 'w') as ElectionAnalysis:
    ElectionAnalysis.write("Election Result\n")
    ElectionAnalysis.write("--------------------------\n")
    ElectionAnalysis.write(f"Total Votes: {str(TotalVotes)}\n")
    ElectionAnalysis.write(f'Khan: {Results["Khan"] / TotalVotes:.3%} ({TotalVotes["Khan"]})\n')
    ElectionAnalysis.write(f'Correy: {Results["Correy"] / TotalVotes:.3%} ({TotalVotes["Correy"]})\n')
    ElectionAnalysis.write(f'Li: {Results["Li"] / TotalVotes:.3%} ({TotalVotes["Li"]})\n')
    #ElectionAnalysis.write(f'"O'Tooley:"+ " {Results["O'Tooley"] / TotalVotes:.3%} ({TotalVotes["O'Tooley"]})'\n)
    ElectionAnalysis.write("----------------\n")
    ElectionAnalysis.write("--------------------------\n")
    ElectionAnalysis.write(f"Winner: {str(winner)}\n")
    ElectionAnalysis.write("--------------------------\n")
   