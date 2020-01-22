import os
import csv
import statistics
# Path to collect data from the Resources folder
budget_data_csv = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')


# Define the function and have it accept the 'polldata' as its sole parameter

    
def poll_analysis(poll_data):
    
    #The total number of months included in the dataset
    # Count months 
    count = sum(1 for line in poll_data)
    print (f"Count {count}")
    csvfile.seek(0)
    header = next(poll_data)    
   
    pollresults={ }
    #count the polls  by the candidate and  store in dictionary 'pollresults'
    for row in poll_data:
        candidates = list(pollresults.keys())  
        if row[2] in candidates:
            pollcount=pollresults.get(row[2])
            pollresults.update({row[2]:pollcount+1})
        else:   
            pollresults.update({row[2]:1})
   
   
    winner=""
    winner_votes=0
    f= open("polling_analysis.txt","w+")   
    print(f"Election Results")
    f.write("Election Results \r\n" )
    print(f"-----------------------")
    f.write("----------------------- \r\n" )
    print(f"Total Votes:  {count}")
    f.write("Total Votes:   %d\r\n" % count)
    print(f"-----------------------")
    f.write("----------------------- \r\n" )
    #loop through the pollresults dictionary print out the each candidate vote %
    for i,j in pollresults.items():
        vote_percent=round((j/count)*100,3)
        print(f"{i} : {vote_percent} % ({j})") 
        f.write("%s " %i +" %f" % vote_percent + "(%d" %j +")\r\n")
       #Look for winner
        if winner_votes < j :
            winner=i
            winner_votes=j
    print(f"-----------------------")
    f.write("----------------------- \r\n" )
    print(f"Winner :{winner}") 
    f.write("Winner :   %s\r\n" % winner)
    print(f"-----------------------")
    f.write("----------------------- \r\n" )
    
    
    
# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:    
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        poll_analysis(csvreader)
       
