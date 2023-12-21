import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day3.txt").readlines()

engine_nums = []
line_index = 0
for line in file_data:
    match_nums = re.finditer(r"\d+", line)
    for match in match_nums:
        num = match.group(0)
        check_list = []
        #create coordinate_list to check for symbols around the number:
        ystart = line_index - 1               #lower lim
        yend = line_index + 2                 #upper lim
        xstart = match.start() - 1            #lower lim
        xend = match.end() + 1                #upper lim
        for y in range(ystart, yend):
            for x in range(xstart, xend):
                coord = [y, x]
                check_list.append(coord)
        #go through coord list, check if out of bounds, if not access position & check for symbol ... if symbol, add num to engine_nums + continue w/ next num
        for coord in check_list:
            y = coord[0]
            x = coord[1]
            if y <= 0 or y > len(file_data)-1 or x <= 0 or x > len(file_data[0])-1:  #len(file_data[0]) to access line length
                continue
            #check position:
            match = re.search(r"[^\w\s\.]", file_data[y][x])
            if match:
                engine_nums.append(num)
                break
    line_index += 1

print(sum([int(i) for i in engine_nums if i.isdigit()]))
