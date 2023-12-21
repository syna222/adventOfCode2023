import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day6.txt").readlines()

def part_one():
    times = file_data[0].split(":")[1].split()
    records = file_data[1].split(":")[1].split()
    margin = 1
    for i in range(0, len(times)):
        win_poss = 0
        t = int(times[i])
        record = int(records[i])
        for press in range(1, t):
            miles = (t-press)*press
            if miles > record:
                win_poss += 1
        margin *= win_poss
    return margin
    
def part_two():
    times = [match.group() for match in re.finditer("\d+", file_data[0].split(":")[1])]
    time = int("".join(times))
    records = [match.group() for match in re.finditer("\d+", file_data[1].split(":")[1])]
    record = int("".join(records))
    win_poss = 0
    for press in range(1, time):
        miles = (time-press)*press
        if miles > record:
            win_poss += 1
    return win_poss

print(part_one())
print(part_two())
