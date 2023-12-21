file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day7.txt").readlines()

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
basics = ["5", "41", "32", "311", "221", "2111", "11111"]
hands = []

def custom_sort(hand):
    return (hand[3], [order.index(card) for card in hand[0]])

for line in file_data:
    [card, bid] = line.split()
    occurrences = {}
    for c in card:
        if c not in occurrences and c != "J":
            occurrences[c] = card.count(c)
    #get card w/ max occurrences or highest type (lowest order index) if multiple// exception: JJJJJ 
    if card == "JJJJJ":
        copy = "AAAAA"
    else:
        copy = card
        max_value = max(occurrences.values())
        max_cards = [key for key, value in occurrences.items() if value == max_value]
        #hightest cards with their order index:
        maxcards_orderindices = [order.index(candidate) for candidate in max_cards]
        replacer = max_cards[maxcards_orderindices.index(min(maxcards_orderindices))] #look up position of lowest order index and get this position from the most counted cards
        copy = copy.replace("J", replacer)
    occurrences = {}
    for c in copy:
        if c not in occurrences:
            occurrences[c] = copy.count(c)
    occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
    occ_string = "".join(str(value) for value in occurrences.values())
    hands.append([card, copy, bid, card_index])
    
#sort hands by card_index, then apply swapping algo
hands_sorted = sorted(hands, key=custom_sort, reverse=True)  #strongest to weakest
#get rank and multiply by bid:
total_winnings = 0
for i in range(0, len(hands_sorted)):
    product = int(hands_sorted[i][2]) * (i+1)
    total_winnings += product

print(total_winnings)
    