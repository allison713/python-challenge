#Import csv module
import csv

#Identify file path
file = "PyPoll/Resources/election_data.csv"

#open file as csvfile
with open(file, 'r', encoding='utf', newline='') as csvfile:
        
    #read the file separating by comma    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Assign the headers
    csv_header = next(csvfile)
    
    #Create a list of candidates. As we find a new candidate in the list, their name will be appended here.
    candidates = []

    #
    data = []

    #Vote counter per candidate.
    vote_counter = []
    vote_percent = []
    
    #Establish a counter for the number of votes cast
    vote_total = 0
    
    #Create a loop that counts each row except the header
    for row in csvreader:
        
        #increase the votes counter
        vote_total += 1
        
        #adds the candidate to the data list
        data.append(row[2])
    
    #Add first name to candidates list
    candidates.append(data[0])
    
    #Check candidates list for a name in the data list. Add the name to candidates if it isn't already there. 
    for name in data:
        if name not in candidates:
            candidates.append(name)
    
    for name in candidates:
        candidate_count = data.count(name)
        vote_counter.append(candidate_count)

    #Create a percentage value for each vote counter value
    for vote in vote_counter:
        percentage = "{:.3%}".format(vote/vote_total)
        vote_percent.append(percentage)
    
    #Zip lists so that candidates are next to their own vote count
    candidates_zip = zip(candidates, vote_counter, vote_percent)
    
#create the text to save and print in terminal
summary = ["Election Results", "---------------------------------------------", 
           f"Total Votes: {vote_total}", "---------------------------------------------",
           f"{candidates[0]}: {vote_percent[0]}, ({vote_counter[0]})",
           f"{candidates[1]}: {vote_percent[1]}, ({vote_counter[1]})",
           f"{candidates[2]}: {vote_percent[2]}, ({vote_counter[2]})",
           "---------------------------------------------",
           f"Winner: {candidates[1]}"
           ]

#print the summary in the terminal
for item in summary:
    print(item)

#create the output text file
output_path = "PyPoll/Analysis/poll_results.csv"

# Open the file using "write" mode.
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Candidate","Vote Count","Percentage"])
    csvwriter.writerows(candidates_zip)
    
    