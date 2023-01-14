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
    
    #use a second variable to find the difference between just two rows at a time.
    difference = 0
    
    #Establish a variable for extreme profits
    max_profit = 0
    min_profit = 0
    
    #Create a loop to count the rows except for the headers
    for row in csvreader:
        
        #Increase the counter for each row in csvfile
        month_counter += 1
        
        #Increase the counter for each row
        net_total_profit += int(row[1])
        
        if month_counter > 1:
            difference = int(row[1]) - start
            total_difference += difference
            
        #Set max profit value
        if difference > max_profit:
            max_profit = difference
            date_max = row[0]
        
        #Set min profit value
        if difference < min_profit:
            min_profit = difference
            date_min = row[0]
            
        #Set the beginning profit/loss:
        start = int(row[1])
    
    #find the average of the changes in profit/losses
    avg_profit_changes = round(int(total_difference)/(int(month_counter)-1), 2)

#create the text to save and print in terminal
summary = ["Financial Analysis", "---------------------------------------------", f"Total Months: {month_counter}", 
           f"Total: ${net_total_profit}", f"Average Change: ${avg_profit_changes}", f"Greatest Increase in Profits: {date_max} (${max_profit})",
           f"Greatest Decrease in Profits: {date_min} (${min_profit})"]

#print the summary in the terminal
for item in summary:
    print(item)

#create the output text file
output_path = "E:/Downloads/python-challenge/PyBank/Analysis/budget_data_results.txt"

# Open the file using "write" mode.
with open(output_path, 'w') as output_file:

    #Writing the rows of text into text file
    for item in summary:
        output_file.write(item)
        output_file.write('\n')