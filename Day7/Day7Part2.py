with open('Day7/input.txt', 'r') as file:
    lines = file.readlines()
import copy
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def getRank(hand):
    cardsInHand = []
    appearances = []
    Jappearances = 0
    for cardInd in range(5):
        card = hand[cardInd]
        if card == 'J':
            Jappearances += 1
            continue
        if card not in cardsInHand:
            count = 0
            for i in range(5):
                if card == hand[i]:
                    count += 1
            appearances.append(count)
            cardsInHand.append(card)
    if Jappearances >= 4:
        rank = 1
        return rank
    if Jappearances == 3 and appearances == [2]:
        rank = 1
        return rank
    if 3 in appearances:
        indToRemove = appearances.index(3)
        appearancesWOutOne3 = copy.deepcopy(appearances)
        del appearancesWOutOne3[indToRemove]
    else:
        appearancesWOutOne3 = copy.deepcopy(appearances)
    if 2 in appearances:
        indToRemove = appearances.index(2)
        appearancesWOutOne2 = copy.deepcopy(appearances)
        del appearancesWOutOne2[indToRemove]
    else:
        appearancesWOutOne2 = copy.deepcopy(appearances)

    if 5 in appearances or max(appearances) + Jappearances == 5:
        rank = 1
    elif 4 in appearances or max(appearances) + Jappearances == 4:
        rank = 2
    elif 3 in appearances and max(appearancesWOutOne3) + Jappearances == 2:
        rank = 3
    elif 2 in appearances and max(appearancesWOutOne2) + Jappearances == 3:
        rank = 3
    elif 3 in appearances or max(appearances) + Jappearances == 3:
        rank = 4
    elif appearances.count(2) == 2:
        rank = 5 
    elif 2 in appearances or Jappearances == 1:
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
            if (card1.isdigit() or card1 == 'J') and (card2.isdigit() or card2 == 'J'):
                if card1 == 'J':
                    card1 = 0
                if card2 == 'J':
                    card2 = 0
                if int(card1) > int(card2):
                    return True
                else:
                    return False
            elif (card2.isdigit() or card2 == 'J'):
                return True
            elif (card1.isdigit() or card1 == 'J'):
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
    sum += (i+1)*hands[list[i]]['bid']

print(sum)