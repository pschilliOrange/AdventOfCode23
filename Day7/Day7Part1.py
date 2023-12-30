with open('Day7/example.txt', 'r') as file:
    lines = file.readlines()
def getRank(hand):
    cardsInHand = []
    appearances = []
    for cardInd in range(5):
        card = hand[cardInd]
        if card not in cardsInHand:
            count = 0
            for i in range(5):
                if card == hand[i]:
                    count += 1
            appearances.append(count)
            cardsInHand.append(card)
    if 5 in appearances:
        rank = 1
    elif 4 in appearances:
        rank = 2
    elif 3 in appearances and 2 in appearances:
        rank = 3
    elif 3 in appearances and 1 in appearances:
        rank = 4
    elif appearances.count(2) == 2:
        rank = 5 
    elif 2 in appearances:
        rank = 6
    else:
        rank = 7 
    return rank
def cardRank(card):
    if card == 'A':
        return 1
    elif card == 'K':
        return 2
    elif card == 'Q':
        return 3
    elif card == 'J':
        return 4
    elif card == 'T':
        return 5

def breakTie(hand1, hand2):
    for i in range(5):
        card1 = hand1[i]
        card2 = hand2[i]
        if card1 is not card2:
            if card1.isdigit() and card2.isdigit():
                if int(card1) > int(card2):
                    return True
                else:
                    return False
            elif card2.isdigit():
                return True
            elif card1.isdigit():
                return False
            else:
                if cardRank(card1) < cardRank(card2):
                    return True
                else:
                    return False

def isStronger(hand1, hand2):
    rank1 = getRank(hand1)
    rank2 = getRank(hand2)
    if rank1 <  rank2:
        return True
    elif rank1 > rank2:
        return False
    else:
        return breakTie(hand1, hand2)


hands = {}
for i in range(len(lines)):
    line = lines[i]
    hand = {}
    hand['cards'] = line[0:5]
    hand['bid'] = int(line.split(' ')[1]) 
    hands[i] = hand

list = []
list.append(0)
for i in range(1, len(lines)):
    indToPut = 0
    for j in range(len(list)-1, -1, -1):
        if not isStronger(hands[list[j]]['cards'],hands[i]['cards']):
            indToPut = j + 1
            break
    list.insert(indToPut, i)
sum = 0
for i in range(len(lines)):
    print((i+1), hands[list[i]]['bid'])
    sum += (i+1)*hands[list[i]]['bid']
for i in range(len(lines)):
    print(hands[list[i]]['cards'])

print(sum)