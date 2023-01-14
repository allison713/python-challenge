#Import csv module
import csv

#Identify file path
file = "E:/Downloads/python-challenge/PyPoll/Resources/election_data.csv"

#open file as csvfile
with open(file, 'r', encoding='utf', newline='') as csvfile:
        
    #read the file separating by comma    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Assign the headers
    csv_header = next(csvfile)
    
    #Create a list of candidates. As we find a new candidate in the list, their name will be appended here.
    candidates = []
    data = []
    vote_counter = []
    
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
    
    print(candidates)
    
    for name in candidates:
        candidate_count = data.count(name)
        vote_counter.append(candidate_count)
        
    print(vote_counter)
        
 
    
    