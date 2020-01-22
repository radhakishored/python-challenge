import os
import csv
import statistics
# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')


# Define the function and have it accept the 'bankdata' as its sole parameter

    
def data_analyze(bank_data):
    
    #The total number of months included in the dataset
    # Count months 
    count = sum(1 for line in bank_data)
   
    
    #Move the pointer back to 1st row
    csvfile.seek(0)
    header = next(bank_data) 
    
    #The net total amount of "Profit/Losses" over the entire period
    total=0
    total = sum(int(row[1]) for row in bank_data)
   
       
    #Move the pointer back to 1st row
    csvfile.seek(0)
    header = next(bank_data)     
      
  
    # For forther analyssis 
    difference = []
    # Move the pointer to next row
    row1 = next(bank_data)
    previous=row1[1]
    # Capture mothly chnages in list  from row2
    for row in bank_data:
        difference.append(int(row[1])-int(previous))
        previous=row[1]
    
    #The average of the changes in "Profit/Losses" over the entire period   
    avg = round(sum(difference)/len(difference),2)
    #The greatest increase in profits (date and amount) over the entire period 
    maximum = max(difference)
    #The greatest decrease in losses (date and amount) over the entire period
    minimum = min(difference) 
    min_idx=difference.index(min(difference))  # Index of min value in list
    max_idx=difference.index(max(difference))   # Index of min value in list
    
    #move the pointer 1st row
    csvfile.seek(0)
    header = next(csvreader)
    list_data=list(bank_data)
    # Get the releative date  for min and max indexes
    min_date=(list_data[min_idx+1][0])
    max_date=(list_data[max_idx+1][0])
    
    print(f"Total months  {count}")
    print(f"Total: ${str(total)}")    
    print(f"Average  Change: $ {avg}")
    print(f"Greatest Increase in Profits: {max_date} (${maximum})")
    print(f"Greatest Decrease in Profits: {min_date} (${minimum})")
    f= open("bankdata_analysis.txt","w+")
    #f.write("This is line %d\r\n" % (i+1))
    f.write("Total months  %d\r\n" % count)
    f.write("Total: $ %d\r\n" % total )    
    f.write("Average  Change: $ %f\r\n" % avg )
    f.write("Greatest Increase in Profits: %s" % max_date + "($%d)\r\n" %maximum)
    f.write("Greatest Decrease in Profits: %s" % min_date + "($%d)\r\n" %minimum)
    
    
# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:    
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        data_analyze(csvreader)
       
        