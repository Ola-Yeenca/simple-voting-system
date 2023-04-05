# Dictionary of empty candidates
candidates = {}

# getting the number of candidates from the user
while True:
    num_candidates = input("Enter the number of candidates: ")
    print('----------------------------------------------------')
    try:
        num_candidates = int(num_candidates)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        print('----------------------------------------------------')

# looping through the number of candidates
for i in range(num_candidates):
    # getting the name of the candidate
    name = input("Enter the name of the candidate: ")
    print('----------------------------------------------------')
    # adding the candidate to the dictionary
    candidates[name.lower()] = 0

# lets get the number of voters from the user
num_voters = int(input("Enter the number of voters: "))
print('----------------------------------------------------')

# loop through the number of voters and get their votes
for i in range(num_voters):
    print('voter ', (i+1))
    for name in candidates:
        print(name.title())
    #get the name of the candidate from the voter
    while True:
        vote = input("Who do you vote for? ").lower()
        print('----------------------------------------------------')

        #check if the vote is valid
        if vote in candidates:
            #add one to the vote count
            candidates[vote] += 1
            print('Thank you! Your vote has been recorded successfully.')
            print('----------------------------------------------------')
            break
        else:
            print("Invalid vote! Try again")
            print('----------------------------------------------------')

# print the results
print("Election Results")
print("----------------")
sorted_candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
for name, votes in sorted_candidates:
    if votes == 1:
        print(f"{name.title()} - 1 vote")
    else:
        print(f"{name.title()} - {votes} votes")
