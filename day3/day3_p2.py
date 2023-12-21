import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day3.txt").readlines()

#create list for asterisks + surroundings:
stars_list = []
i = 0
for line in file_data:
    match_stars = re.finditer(r"\*", line)
    for star in match_stars:
        coord_list = []
        #create coordinate_list to check for nums around *:
        ystart = i - 1
        yend = i + 2
        xstart = star.start() - 1
        xend = star.end() + 1
        for y in range(ystart, yend):
            for x in range(xstart, xend):
                coord_list.append([y, x])
        star_pos = [i, star.start()]
        star_and_list = [star_pos, coord_list]
        stars_list.append(star_and_list)  #stars_list[x][0] to access star coordinates, stars_list[x][1] to access star's surrounding coordinates
    i += 1

#create list for nums + surroundings:
nums_list = []
line_index = 0
for line in file_data:
    match_nums = re.finditer(r"\d+", line)
    for match in match_nums:
        num = match.group(0)
        #coordinates of number:
        coord_list = []
        for c in range(match.start(), match.end()):
            coord_list.append([line_index, c])
        num_and_coord = [num, coord_list]
        nums_list.append(num_and_coord)   
    line_index += 1
    
product_sum = []
#for every star make a counter + adj_num_list, go through every of the star's coordinates + look up every number coordinate.
#if two match check if num already in adj_num_list! only append if not
# then check how many exist in star list - if there's exactly two -> multiply + append to prod_sum
for star in stars_list:
    adj_num_list = []
    for coord in star[1]:
        #compare to numbers coordinates:
        for num in nums_list:
            for numco in num[1]:
                if coord == numco and num[0] not in adj_num_list:
                    adj_num_list.append(num[0])
    if len(adj_num_list) == 2:
        product_sum.append(int(adj_num_list[0]) * int(adj_num_list[1]))
print(sum(product_sum))
        