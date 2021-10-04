import os
import csv

# Path to collect data from the Resources folder
Path_Of_Budget_Data_csv = os.path.join("Resources", "budget_data.csv")

# Define variables
# Month_Counter = 0
PL_List = []
Month_List = []
Change_Value = 0
Current_Month_PL = 0
Changes_List = []

# Open and read csv
with open(Path_Of_Budget_Data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
              
    # add 1 to monthsCount for each row
        # Month_Counter += 1
    # add each month to monthList
        Month_List.append(str(row[0]))
    # increase netprofit with each row
        PL_List.append(int(row[1]))      
        
        # Calculate month to month changes in profit
        # if there is previous data do the following:
        if Change_Value != 0:
            
            # set monthProfit to value in profit column
            Current_Month_PL = int(row[1])
            
            # subtract current profit from previous month's profits to find the change
            Change_Value = Current_Month_PL - Change_Value
            
            # take this change value and store it in the changeList
            Changes_List.append(Change_Value)
            
            # reset change variable to the value in the current profit column, next
            Change_Value = int(row[1])
            
        # if there is no previous data reset change to value in profit column (this will only apply once for the first row)
        elif Change_Value == 0:
            Change_Value = int(row[1])  

 # No of months is just length of the month list
    Total_Months=len(Month_List)
# Total is just sum of the column 2 or index [1]
    Total = sum(PL_List)
# Now that we are done with those totals, to analyse changes we remove 1st month from monthList since there is no change that occurs
    Month_List.pop(0)
# Average change is just the sum of all changes divided by the number of changes and rounded to 2 dp
    Average_Change=round(sum(Changes_List) / float(len(Changes_List)), 2)
# find the index position of the greatest increase/decrease in profits
    Max_Index = Changes_List.index(max(Changes_List))
    Min_Index = Changes_List.index(min(Changes_List))
    # use index positions to find the month that corresponds with max and min values from the changeList

    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {Total_Months}')
    print(f'Total: ${Total}')
    print(f"Average Change: ${Average_Change}")  
    print(f'Greatest Increase in Profits: in {Month_List[int(Max_Index)]} with a profit of ${max(Changes_List)}')
    print(f'Greatest Loss In Profits: in {Month_List[int(Min_Index)]} with a loss of ${min(Changes_List)}')

    # set the file to write to
PyBank_Analysis_TextFile = os.path.join("Analysis","PyBank.txt")    
    
    # write the results to a text file
with open(PyBank_Analysis_TextFile, 'w') as txtfile:
        txtfile.write('Financial Analysis')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Months: {Total_Months}')
        txtfile.write(f'\nTotal: ${Total}')
        txtfile.write(f'\nAverage Change: ${Average_Change}')
        txtfile.write(f'\nGreatest Increase in Profits: in {Month_List[int(Max_Index)]} with a profit of ${max(Changes_List)}')
        txtfile.write(f'\nGreatest Loss In Profits: in {Month_List[int(Min_Index)]} with a loss of ${min(Changes_List)}')