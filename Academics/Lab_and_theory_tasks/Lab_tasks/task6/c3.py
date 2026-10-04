# question # 03

votes1 = ["Ali", "Sara", "Ali", "Hamza", "Sara", "Ali", "Zara","Hamza", "Sara", "Sara"]

votes2 = ["Ali", "Sara", "Sara", "Ali", "Zara"]

# counting each candidate votes
def count_votes(votes):
    '''
    counts the number of votes received by each candidate
    '''
    vote_counting = {}
    for i in range(len(votes)):
        if votes[i] in vote_counting:
            vote_counting[votes[i]] += 1
        else:
            vote_counting[votes[i]] = 1
    return vote_counting

def announce_result(votes):
    '''
    print votes count, winner, and candidates with fewer than 2 votes
    '''
    vote_count = count_votes(votes)
    print("result on the basis of votes of candidate :")

    for candidate in vote_count:
        print(candidate, ":", vote_count[candidate])
        
    highest = 0
    for candidate in vote_count:
        if (vote_count[candidate] > highest):
            highest = vote_count[candidate]
    # printing winners
    winners = []
    for candidate in vote_count:
        if (vote_count[candidate] == highest):
            winners.append(candidate)
    if len(winners) == 1:
        print("winner with the most votes :", winners[0])
    else:
        print("tie between winners :", winners)

    # printing candidates with votes less than 2
    fewer_than_2 = []
    for candidate in vote_count:
        if (vote_count[candidate] < 2):
            fewer_than_2.append(candidate)
    print("candidate(s) with votes fewer than 2 votes :", fewer_than_2)


# calling for 1st voting round
announce_result(votes1)
# calling for 2nd voting round
announce_result(votes2)
    


