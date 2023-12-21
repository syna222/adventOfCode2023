import math
import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day10.txt").readlines()

my_dict = {"|":["north", "south"], "-":["west", "east"], "L":["north", "east"], "J":["north", "west"], "7":["west", "south"], "F":["east", "south"], ".":["", ""]}
directions = {"north":[-1, 0], "east":[0, 1], "south":[1, 0], "west":[0, -1]}  #schema [i, j]
opposites = {"north":"south", "south":"north", "west":"east", "east":"west"}
i = 0
j = 0

for a in range(len(file_data)):
    for b in range(len(file_data[a])):
        if file_data[a][b] == "S":
            #i and j are set to starting position/S position:
            i = a
            j = b
            break

step_count = 0
coordinates = [[i, j]]
direction = ""
#check all 4 directions for S, if one applies, stop + take that route:
if "south" in my_dict[file_data[i-1][j]]:
        direction = "north"
        i = i - 1 #j stays
elif "west" in my_dict[file_data[i][j+1]]:
        direction = "east"
        j = j + 1
elif "north" in my_dict[file_data[i+1][j]]:
        direction = "south"
        i = i + 1
elif "east" in my_dict[file_data[i][j-1]]:
        direction = "west"
        j = j - 1
else:
    print("error")  
    
while True:
    sign = file_data[i][j]
    coordinates.append([i, j])
    if sign == "S":
        break
    #look up sign + take direction that remains when eliminating the opposite of the direction we came from (cause direction east connects to direction west -> opposites)
    came_from = opposites[direction]
    options = my_dict[file_data[i][j]]
    #update direction
    indexer = options.index(came_from) #avoid index we came from
    if indexer == 0:
        direction = options[1]
    elif indexer == 1:
        direction = options[0]
    #determine next position:
    i += directions[direction][0]
    j += directions[direction][1]
    step_count += 1
print("final stepcount:", step_count, "furthest away:", math.ceil(step_count/2))

#part TWO:
#shoelace area method to determine area of polygon (coordinates have to be listed clockwise + starting point needs to be present @ start + end)
shoelace_prodsum_1 = 0
shoelace_prodsum_2 = 0
#append starting pos to end + and increment stepcount by 1 to make loop for calculation:
coordinates.append(coordinates[0])
step_count += 1

for i in range(len(coordinates) - 1):
    n, m = coordinates[i]
    #shoelace left to right:
    prod_1 = n * coordinates[i+1][1]
    shoelace_prodsum_1 += prod_1
    #shoelace right to left:
    prod_2 = m * coordinates[i+1][0]
    shoelace_prodsum_2 += prod_2
    
area = abs(shoelace_prodsum_1 - shoelace_prodsum_2) / 2
print("area:", round(area))
print("points on border:", step_count)

#reverse pick's theorem (take area to determine points within):
num_points = area - (step_count/2) + 1
print("points in polygon itself:", int(num_points))
print("total points:", int(step_count + num_points))





