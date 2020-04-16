# To import libraries
import pathlib
import csv

# To set the path to the file that we are going to read
csvpath = pathlib.Path("Resources/budget_data.csv")

# To read the file
with open (csvpath, "r") as csvfile:

# To set the variables
    csvreader = csv.reader (csvfile, delimiter = ",")
    header = next(csvfile)
    total_month = 0
    total_month_list = []
    total_profit= 0
    total_profit_list = []
    change = 0.0
    total_change = 0.0
    total_change_list = []
    average_change = 0.0
    
# To calculate total month, total profit and create a list of dates and profits
    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        total_month += 1
        total_profit += profit

        total_month_list.append(date)
        total_profit_list.append(profit)

# To calculate changes of profit between each month and total changes, and create a list of changes of profit
         
    for i in range(len(total_profit_list)-1):
        
        change = total_profit_list[i+1] - total_profit_list[i]
        total_change += change
        total_change_list.append(change)
        
# To calculate maximum increase and decrease in changes of profit and which month did it happen
    max_increase = max(total_change_list)
    max_decrease = min(total_change_list)
    average_change = round((total_change)/len(total_change_list), 2)
    max_month = total_month_list[total_change_list.index(max_increase)+1]
    min_month = total_month_list[total_change_list.index(max_decrease)+1]

# To print the analysis in terminal
    print("Financial Analysis")
    print("------------------------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")
    


# To print the analysis in the BankAnalysis.txt file
csvpath_w = pathlib.Path("Analysis/BankAnalysis.txt")

with open (csvpath_w, "w") as csvfile_w:
    
    csvfile_w.write("Financial Analysis")
    csvfile_w.write("\n")
    csvfile_w.write("------------------------------------------------")
    csvfile_w.write("\n")
    csvfile_w.write(f"Total Months: {total_month}")
    csvfile_w.write("\n")
    csvfile_w.write(f"Total: ${total_profit}")
    csvfile_w.write("\n")
    csvfile_w.write(f"Average Change: ${average_change}")
    csvfile_w.write("\n")
    csvfile_w.write(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    csvfile_w.write("\n")
    csvfile_w.write(f"Greatest Decrease in Profits: {min_month} (${max_decrease})")
    csvfile_w.write("\n")

