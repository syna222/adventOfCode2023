file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day21.txt").read().splitlines()

def reach(start_pos, n): #n = number of steps
    x = start_pos[0]
    y = start_pos[1]
    if n == 0:
        return []
    elif n == 1:
        #check if no hash!
        pre = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
        coords = []
        for p in pre:
            a, b = p
            if 0 <= a < len(file_data) and 0 <= b < len(file_data[0]) and file_data[a][b] != "#":
                coords.append(p)
        return coords
    else:
        previous_positions = reach(start_pos, n-1)
        new_positions = set()  # Use a set to avoid duplicates
        for pos in previous_positions:
            x, y = pos
            # For each position, add all positions one step away + check if none of them are a hash:
            for nx, ny in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
                if 0 <= nx < len(file_data) and 0 <= ny < len(file_data[0]) and file_data[nx][ny] != "#":
                    new_positions.add((nx, ny))
        return list(new_positions)  # Convert set back to list
        
start_point = 0    
for i, elem in enumerate(file_data):
    for j, el in enumerate(file_data[i]):
        if file_data[i][j] == "S":
            start_point = (i, j)
#print(reach(start_point, 64))
print(len(reach(start_point, 64)))




