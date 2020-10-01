#Import OS and CSV files
import os   
import csv

#Set Path for CSV File
csv_path = os.path.join("..","Resources","election_data.csv")


#Read the CSV file   
with open(csv_path) as csv_file: 
      
    csv_reader = csv.reader(csv_file, delimiter= ',')
    csv_header = next(csv_file)
    # print(csv_reader)   

#Declare variables
    Count = 0
    Votes_Cast = 0
    percent_of_votes = 0
    Candidate_Votes = 0
    Popular_Vote = ""
    Candidates = {}
    

    
    for row in csv_reader:
        
# Count the total number of votes cast
        candidate = row[2]
        Count += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1

    
    
# Print Statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {Count}")
    print("-------------------------------")
    # print(f' {Candidates}')
    # print(f' {Candidates["Khan"]}')
    
            
#Total number of votes for each candidate
    for candidate in Candidates:
        Votes_Cast += Candidates[candidate]
    
        # percent of votes for each candidate
        percent_of_votes = (Candidates[candidate])/(Count) * 100
        print(f"{candidate}: {round(float(percent_of_votes),3)}% ({Votes_Cast})")
        # print(candidate + round(float(percent_of_votes),2 + "%" (Votes_Cast))
        
        if Candidates[candidate] > Candidate_Votes:
            Popular_Vote = candidate
            Candidate_Votes = Candidates[candidate]
        
        
    
#The winner of the election based on popular vote.
    print("-------------------------------")

    print(f"Winner: {Popular_Vote}")
    
    print("-------------------------------")


 #Text File
txt_path = os.path.join("Pypoll.txt")

with open("txt_path.txt", "w") as PyPoll_file:

    PyPoll_file.write(f'Election Resulst\n')
    PyPoll_file.write(f'-----------------\n')
    PyPoll_file.write(f"Total Votes: {Count}\n")
    PyPoll_file.write(f'-----------------\n')
    PyPoll_file.write(f' {Candidates["Khan"]} {round(float(percent_of_votes),3)} {(Votes_Cast)}\n')
    PyPoll_file.write(f' {Candidates["Correy"]} {round(float(percent_of_votes),3)} {(Votes_Cast)}\n')
    PyPoll_file.write(f' {Candidates["Li"]} {round(float(percent_of_votes),3)} {(Votes_Cast)}\n')
    PyPoll_file.write(f' {candidate}: {round(float(percent_of_votes),3)}% ({Votes_Cast})\n')
    PyPoll_file.write(f'-----------------\n')
    PyPoll_file.write(f'Winner: {Popular_Vote}\n')
    PyPoll_file.write(f'-----------------\n')

    
    PyPoll_file.close() 
      
