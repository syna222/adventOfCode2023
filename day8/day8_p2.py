import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day8.txt").readlines()
directions = file_data[0][:-1]
data = "".join(file_data[2:])

wanted = r"[A-Z0-9]{2}A"  #starting point
my_regex = r" = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)"
start_regex = wanted + my_regex
matches = list(re.finditer(start_regex, data))

match_indexer = 0
round_counts = [None for m in matches]  #beware of iterator exhaustion!

for m in matches:  #!group!   start at directions anew for each match
    i = 0  #for indexing direction
    rcount = 1
    while True:
        left = m.group(1)
        right = m.group(2)
        #choose left or right based on current pos in directions:
        if directions[i] == "L":
            sought_triple = left
        else:
            sought_triple = right
        if sought_triple[2] == "Z":  #if end is reached for match note final round count
            round_counts[match_indexer] = rcount
            break
        m = re.search(sought_triple + my_regex, data)
        i += 1
        i %= len(directions)
        rcount += 1
    match_indexer += 1

round_counts.sort(reverse=True)
#find lcm of all round counts (lcm method plagiarized):
#print(round_counts)

def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)

def LcmOfArray(arr, idx):
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/__gcd(a,b))

print(LcmOfArray(round_counts, 0))

    