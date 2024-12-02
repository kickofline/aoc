f = open("4.txt", "r")
data = f.read()

cards = data.split("\n")
cardsArray = []
for card in cards:
    splitCard = card.split(": ")[1].split(" | ")
    spacesRemoved = [list(filter(None, splitCard[0].split(" "))) , list(filter(None, splitCard[1].split(" ")))]
    cardsArray.append(spacesRemoved)

matchesArray = []
for card in cardsArray:
    matches = 0
    for i in card[0]:
        for j in card[1]:
            if i == j:
                matches += 1
    matchesArray.append(matches)

# Function to calculate matches and return the number of scratchcards won
def calculate_matches(card):
    return len(set(card[0]) & set(card[1]))

def process_scratchcards(scratchcards):
    # Initialize a list to keep track of the number of instances of each card
    instances = [1] * len(scratchcards)

    # Iterate over each card
    for i in range(len(scratchcards)):
        matches = calculate_matches(scratchcards[i])
        # For each match, add an instance of the following cards
        for j in range(i + 1, min(i + 1 + matches, len(scratchcards))):
            instances[j] += instances[i]

    return sum(instances)

# Adding the original number of scratchcards to the total

print(process_scratchcards(cardsArray))

points = 0
for i in matchesArray:
    if i == 0:
        continue
    points += 2**(i-1)
#print("part 1 : " + str(points))
