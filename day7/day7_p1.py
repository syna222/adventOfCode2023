file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day7.txt").readlines()

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
basics = ["5", "41", "32", "311", "221", "2111", "11111"]
hands = []

def custom_sort(hand):
    return (hand[2], [order.index(card) for card in hand[0]])

for line in file_data:
    [card, bid] = line.split()
    occurrences = {}
    for c in card:
        if c not in occurrences:
            occurrences[c] = card.count(c)
    occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))
    occ_string = "".join(str(value) for value in occurrences.values())
    card_index = basics.index(occ_string)
    hands.append([card, bid, card_index])

#sort hands by card_index, then apply swapping algo
hands_sorted = sorted(hands, key=custom_sort, reverse=True)  #strongest to weakest
#get rank and multiply by bid:
total_winnings = 0
for i in range(0, len(hands_sorted)):
    product = int(hands_sorted[i][1]) * (i+1)
    total_winnings += product

print(total_winnings)