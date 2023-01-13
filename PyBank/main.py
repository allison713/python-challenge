#Import csv module
import csv

#Identify file path
file = "E:/Downloads/python-challenge/PyBank/Resources/budget_data.csv"

#open file as csvfile
with open(file, 'r', encoding='utf', newline='') as csvfile:
        
    #read the file separating by comma    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Assign the headers
    csv_header = next(csvfile)
    
    #Establish a counter for the months, it goes up by 1 for each row.
    month_counter = 0
    
    #Establish a net total counter
    net_total_profit = 0
    
    #Establish the variable for total changes in profit
    total_difference = 0
    difference = 0
    
    #Create a loop to count the rows except for the headers
    for row in csvreader:
        
        #Increase the counter for each row in csvfile
        month_counter += 1
        
        #Increase the counter for each row
        net_total_profit += int(row[1])
        
        if month_counter > 1:
            difference = int(row[1]) - start
            total_difference += difference
            
        #Set the beginning profit/loss:
        start = int(row[1])
        
            
print(total_difference)
        