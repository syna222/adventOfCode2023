from itertools import combinations
import numpy as np
import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day11.txt").readlines()
# Remove newline characters and create a list of lists
data = [list(line.strip()) for line in file_data]
# Convert the list of lists into a NumPy array
array = np.array(data, dtype="<U10")  #change dtype to make numpy array contain more than 1 char/pos (default)

#create record of lines and columns that should be "duplicated":
lines = []
columns = []
for i, row in enumerate(array):
    if all(cell == "." for cell in row):
        lines.append(i)
for i, row in enumerate(array.T):   #t = transform array so that columns are treated as rows!
    if all(cell == "." for cell in row):
        columns.append(i)
        
#replace #s with numbers:
enumerator = 1
for i, row in enumerate(array):
    for j, colpos in enumerate(array[i]):
        if array[i][j] == "#":
            array[i][j] = str(enumerator)
            enumerator += 1

whereabouts = []
for e in range(1, enumerator):
    i, j = np.where(array == str(e))
    i = i[0]
    j = j[0] #unpack values from numpy result
    whereabouts.append([i, j])

#use combinations to form pairs of points/their coordinates:
pairs = list(combinations(whereabouts, 2))

#für jedes x-pair schauen, wieviele instanzen aus lines-array in range(kleineres x, größeres x) liegen + wieviele instanzen aus columns-array in range(kleineres y, größeres y) liegen
#die anzahl * duplikationsfaktor (z.B. 1 für doppelt, 999999999 für 1Mio.) wird auf die jeweilige differenz (zw. klx/gröx oder kly/gröy) addiert, die modifizierten differenzen addiert geben die neue schrittzahl
def get_sum(clone_factor):
    summator = 0
    for pair in pairs:
        #print(pair)
        x1 = pair[0][0]
        y1 = pair[0][1]
        x2 = pair[1][0]
        y2 = pair[1][1]
        #put x and y values in arrays to get bigger/smaller value for each for range
        x_s = [x1, x2]
        y_s = [y1, y2]
        lines_in = [l for l in lines if l in range(min(x_s), max(x_s))]
        cols_in = [c for c in columns if c in range(min(y_s), max(y_s))]
        diff = abs(x1-x2) + len(lines_in) * clone_factor + abs(y1-y2) + len(cols_in) * clone_factor  #count how many lines to be cloned lie between x-points and how many cols between y-points + multiply with faktor + add to step number
        summator += diff
    return summator

print("part one:", get_sum(1))
print("part two:", get_sum(999999))




