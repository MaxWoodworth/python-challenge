#Import Dependicies
import os
import csv

#Locate and Open Poll CSV
pollcsv = os.path.join("Resources", "Poll.csv")
with open(pollcsv, newline="") as csvfile:

    #Read Poll CSV
    reader = csv.reader(csvfile, delimiter=',')
    csvheader = next(reader)
    person = []

    #Start loop 
    for i in reader:
        person.append(i[2])

    person_count = [[j, person.count(j)] for j in set(person)]
    
    #Creates variables for votes and candidates
    votes = []
    candidate = []
    
    for i in person_count:
        candidate.append(i[0])
        votes.append(i[1])

    person_zip = zip(candidate, votes)
    person_list = list(person_zip)

    #Sets the winner to be the person with the most votes
    winner = max(votes)

    for i in person_list:
        if i[1] == winner:
            winning_candidate = i[0]       

#Use len to return the total number of votes           
total_votes = len(person)

#Calculates the total votes and percent of vote
correy_total = person.count('Correy')
correy_percent = int(correy_total) / int(total_votes)
o_tooley_total = person.count("O'Tooley")
o_tooley_percent = o_tooley_total / total_votes
li_total = person.count('Li')
li_percent = li_total / total_votes
khan_total = person.count('Khan')
khan_percent = khan_total / total_votes

#Prints "Election Results" with Spacer
print(f'Election Results')
print(f'-------------------------')
#Prints "Total Votes" with Spacer
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
#Prints "Khan, Correy, Li, and O'Tooley" percent and totals with Spacer after
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})")
print(f'-------------------------')
print(f'Winner: {winning_candidate}')
print(f'-------------------------')

#Prints and creates a txt document to output the same results as above
with open('PyPoll.txt', 'w') as text_file:
    print(f'Election Results', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {o_tooley_percent:.3%} ({o_tooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winning_candidate}', file=text_file)
    print(f'-------------------------', file=text_file)