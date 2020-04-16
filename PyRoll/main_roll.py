# To import the libraries
import pathlib
import csv

# To set the path to the file that we are going to read
csvpath = pathlib.Path("Resources/election_data.csv")

# To set the variables
total_voter = 0
khan_count = 0
correy_count = 0
li_count = 0
tooley_count = 0
khan_percent = 0.0
correy_percent = 0.0
li_percent = 0.0
tooley_percent = 0.0

# To read the file
with open (csvpath, "r") as csvfile:

    reader = csv.reader(csvfile, delimiter = ",")

    header = next(csvfile)

# To calculate how many votes does each candidate win
    for row in reader:

        voterID = row[0]
        county = row[1]
        candidate = row[2]
        total_voter += 1


        if candidate == "Correy":
            correy_count += 1

        elif candidate == "Khan":
            khan_count += 1

        elif candidate == "Li":
            li_count += 1

        else:
            tooley_count += 1
        
        
# To calculate the percentage of votes each candidate won
    khan_percent = khan_count / total_voter * 100
    correy_percent = correy_count / total_voter * 100
    li_percent = li_count / total_voter * 100
    tooley_percent = tooley_count / total_voter * 100

# To calculate who the winner is
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
count_list = [khan_count, correy_count, li_count, tooley_count]
roll_dict = dict (zip(candidate_list, count_list))
winner = max(roll_dict, key=roll_dict.get)

# To print the analysis in the terminal
print ("Election Results")
print("-----------------------------------")
print (f"Total Votes: {total_voter}")
print("-----------------------------------")
print (f"Khan: {khan_percent:.3f}% ({khan_count})")
print (f"Correy: {correy_percent:.3f}% ({correy_count})")
print (f"Li: {li_percent:.3f}% ({li_count})")
print (f"O'Tooley: {tooley_percent:.3f}% ({tooley_count})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

# To print the analysis in the RollAnalysis.txt file
csvpath_w = pathlib.Path("Analysis/RollAnalysis.txt")

with open (csvpath_w, "w") as csvfile_w:

    csvfile_w.write("Election Results")
    csvfile_w.write("\n")
    csvfile_w.write("-----------------------------------")
    csvfile_w.write("\n")
    csvfile_w.write(f"Total Votes: {total_voter}")
    csvfile_w.write("\n")
    csvfile_w.write("-----------------------------------")
    csvfile_w.write("\n")
    csvfile_w.write(f"Khan: {khan_percent:.3f}% ({khan_count})")
    csvfile_w.write("\n")
    csvfile_w.write(f"Correy: {correy_percent:.3f}% ({correy_count})")
    csvfile_w.write("\n")
    csvfile_w.write(f"Li: {li_percent:.3f}% ({li_count})")
    csvfile_w.write("\n")
    csvfile_w.write(f"O'Tooley: {tooley_percent:.3f}% ({tooley_count})")
    csvfile_w.write("\n")
    csvfile_w.write("-----------------------------------")
    csvfile_w.write("\n")
    csvfile_w.write(f"Winner: {winner}")
    csvfile_w.write("\n")
    csvfile_w.write("-----------------------------------")
