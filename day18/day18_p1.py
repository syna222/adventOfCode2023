file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day18.txt").read().splitlines()

n = 0
m = 0
coordinates = [[n, m]]
step_count = 0

for f in file_data:
    direc, q, col = f.split(" ")
    if direc == "L":
        m -= int(q)
    elif direc == "R":
        m += int(q)
    elif direc == "U":
        n -= int(q)
    elif direc == "D":
        n += int(q)
    else:
        pass
    coordinates.append([n, m])
    step_count += int(q)

#shoelace area method to determine area of polygon (coordinates have to be listed clockwise + starting point needs to be present @ start + end)
shoelace_prodsum_1 = 0
shoelace_prodsum_2 = 0

for i in range(len(coordinates) - 1):
    n, m = coordinates[i]
    #shoelace left to right:
    prod_1 = n * coordinates[i+1][1]
    shoelace_prodsum_1 += prod_1
    #shoelace right to left:
    prod_2 = m * coordinates[i+1][0]
    shoelace_prodsum_2 += prod_2
    
area = abs(shoelace_prodsum_1 - shoelace_prodsum_2) / 2
print("area:", area)
print("points on border:", step_count)

#reverse pick's theorem (take area to determine points within) ! subtract duplicate starting point!
num_points = area - (step_count/2) + 1
print("points in polygon:", int(num_points))
print("total points", int(step_count + num_points))
