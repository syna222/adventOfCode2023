import numpy as np
import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day13.txt").read()
all_maps = re.split(r'^\s*$', file_data, flags=re.MULTILINE)

def search_array(np_array, hor_or_ver, flipped):
    to_the_left = None
    for i, line in enumerate(np_array):   #method for searching top to bottom
        if i==0 and (np_array[i] == np_array[i+1]).all():
            #print("mirror line between line", i , "and", i+1)
            to_the_left = i+1
            if flipped:
                to_the_left = len(np_array) - to_the_left
            break
        else:
            end_comparison = 2*(i+1)
            if end_comparison <= len(np_array):
                if (np_array[0:i+1] == np.flipud(np_array[i+1:end_comparison])).all() == True:
                    to_the_left = i+1
                    if flipped:
                        to_the_left = len(np_array) - to_the_left            
    if hor_or_ver == "vertical" or (hor_or_ver == "horizontal" and not to_the_left):
        return to_the_left
    elif hor_or_ver == "horizontal" and to_the_left:
        return 100 * to_the_left
    else:
        return "error message, hor_or_ver was neither horizontal nor vertical"

summator = 0
#do this for every array:
for mappy in all_maps:
    map_lines = mappy.split("\n")  #for empty lines
    #transform into np array
    map_lines = [line for line in map_lines if line]
    data = [list(line.strip()) for line in map_lines]
    array = np.array(data, dtype="<U10")  #dtype for expanding space at each position
    #search each array from each side ("faked" by transforming/flipping array and always checking from top to bottom):
    res1 = search_array(array, "horizontal", False)
    array2 = np.flipud(array)   #flip whole array top to bottom -> horizontal
    res2 = search_array(array2, "horizontal", True)
    array3 = array.T            #transform original array -> vertical
    res3 = search_array(array3, "vertical", False)
    array4 = np.flipud(array.T) #flip transformed array -> vertical
    res4 = search_array(array4, "vertical", True)
    res_array = [res1, res2, res3, res4]
    winner = [x for x in res_array if x]
    #print(winner[0])
    summator += winner[0]
    
print(summator)


            