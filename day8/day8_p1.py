import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day8.txt").readlines()

directions = file_data[0][:-1]
data = "".join(file_data[2:])

sought_triple = "AAA"  #starting point
i = 0
round_counter = 1

while True:
    regex = sought_triple + " = \(([A-Z]{3}), ([A-Z]{3})\)"
    match = re.search(regex, data)
    left = match.group(1)
    right = match.group(2)
    #choose left or right based on current pos in directions:
    if directions[i] == "L":
        sought_triple = left
    else:
        sought_triple = right
    if sought_triple == "ZZZ":
        break
    i += 1
    i %= len(directions)
    round_counter += 1

print(round_counter)   
