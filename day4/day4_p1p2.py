import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day4.txt").readlines()

def prepare_card(card):
    card = card.replace(":", "|")
    winners = card.split("|")[1].split()
    yours = card.split("|")[2].split()
    return [winners, yours]

def part_one():
    card_count = 0
    for card in file_data:
        card_value = 0
        [winners, yours] = prepare_card(card)
        for y in yours:
            if y in winners:
                if card_value == 0:
                    card_value += 1
                else:
                    card_value *= 2
        card_count += card_value
    return card_count
print(part_one())

def part_two():
    #create initial card registry:
    card_registry = []
    card_index = 1
    for card in file_data:
        card_hits = 0
        [winners, yours] = prepare_card(card)
        for y in yours:
            if y in winners:
                card_hits += 1
        card_registry.append([card_index, 1, card_hits])  #[card number, card instances (copies + orig), amassed hits]
        card_index += 1
    for i, card in enumerate(card_registry): 
        a = card[0]
        b = card[1]
        c = card[2]
        if i == len(card_registry) - 1:      
            break
        else:
            for j in range(i + 1 , i + c + 1):
                card_registry[j][1] += b
        i += 1
    card_sum = sum(card[1] for card in card_registry)
    return card_sum
print(part_two())
