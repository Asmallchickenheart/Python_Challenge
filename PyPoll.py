# Use pandas module to read csv file
import pandas

col_list = ["Ballot ID", "County", "Candidate"]
csv_data = pandas.read_csv('/Users/siyuanliang/PycharmProjects/pythonProject/BootCamp_python/election_data.csv', usecols= col_list)
# set original value for each candidate
first_candidate = 0
second_candidate = 0
third_candidate = 0
# set original value for total votes
total_votes = 0
for i in csv_data["Candidate"]:
    # count total votes
    total_votes += 1
    # count votes for each candidate
    if i == "Charles Casper Stockham":
        first_candidate += 1
    elif i == "Diana DeGette":
        second_candidate += 1
    elif i == "Raymon Anthony Doane":
        third_candidate += 1
# calculate percentage for each candidate
first_percantage = round(first_candidate/total_votes*100, 3)
second_percantage = round(second_candidate/total_votes*100, 3)
third_percantage = round(third_candidate/total_votes*100, 3)
# find the winner
if first_candidate > second_candidate and first_candidate > third_candidate:
    winner = "Charles Casper Stockham"
elif second_candidate > first_candidate and second_candidate > third_candidate:
    winner = "Diana DeGette"
elif third_candidate > first_candidate and third_candidate > second_candidate:
    winner = "Raymon Anthony Doane"


print("Election Results")
print("-------------------------")    
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'Charles Casper Stockham: {first_percantage}% ({first_candidate})')
print(f'Diana DeGette: {second_percantage}% ({second_candidate})')
print(f'Raymon Anthony Doane: {third_percantage}% ({third_candidate})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

