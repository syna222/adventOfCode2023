import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day2.txt").readlines()
colour_dict = {"red":12, "green":13, "blue":14}

def part_one(file_data):
    legit_games = []
    for line in file_data:
        game_okay = True
        for key in colour_dict.keys():
            #find all instances of colour with their number:
            regex = r"(\d+) " + key
            matches = re.finditer(regex, line)
            for match in matches:
                amount = int(match.group(1))
                if amount > colour_dict[key]:
                    game_okay = False 
        if game_okay == True:
            legit_games.append(int(line.split(":")[0].split(" ")[1]))
    return sum(legit_games) 
print(part_one(file_data))
    
def part_two(file_data):
    product_sum = 0
    for line in file_data:
        product = 1
        for key in colour_dict.keys():
            regex = r"(\d+) " + key
            matches = re.finditer(regex, line)
            numbers = []  #for each colour (in each line)
            [numbers.append(int(match.group(1))) for match in matches]
            product *= max(numbers)
        product_sum += product
    return product_sum             
print(part_two(file_data))
