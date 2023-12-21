import re

#DELETED THE TEXT PARTS IN THE ORIGINAL FILE!
file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day5.txt").read()

pre_maps = re.split(r'^\s*$', file_data, flags=re.MULTILINE)
# Remove empty lines
pre_maps = [line for line in pre_maps if line]
seeds = pre_maps[0].split()
#delete seeds from maps:
pre_maps.pop(0)
maps = []
for p in pre_maps:
    m = p.split("\n")
    m = [line for line in m if line]   #deletes empty strings
    maps.append(m)
     
converted = []
for seed in seeds:
    curr_conv = int(seed)  #currently converted number
    for m in maps:   #only curr_conv assignment!
        for line in m:
            [a, b, c] = line.split()
            if int(b) <= curr_conv <= int(b)+int(c)-1:      #as soon as range test returns true, assign + jump to outer loop (maps)
                curr_conv = int(a) + curr_conv - int(b)
                break  
    converted.append(curr_conv)

print(min(converted))        