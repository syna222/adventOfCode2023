import numpy as np

map_lines = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day14.txt").read().splitlines()

#transform into np array
data = [list(line.strip()) for line in map_lines]
array = np.array(data, dtype="<U10")

for n in range(len(array)):
    for m in range(len(array[0])):
        if array[n][m] == "O":
            pos = n
            while True:
                if array[pos-1][m] == "O" or array[pos-1][m] == "#" or pos == 0: #letztere Bedingung geht weil vorher schon geprüft wird, ob dort was liegt
                    array[pos][m] = "O"
                    if n != pos:
                        array[n][m] = "." #ursprüngliches O wird ersetzt durch ., aber nur, wenn O auch weiter vor bewegt wurde
                    break
                pos -= 1
load = 0
for n in range(len(array)):
    row_load = abs(len(array) - n)
    count = (array[n] == "O").sum()
    load += row_load * count
print(load)