import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day19.txt").read()
workflows, parts = file_data.split("\n\n")
parts = parts.split()
ps = []

for p in parts:
    dic = {}
    x, m, a, s = p.split(",")
    dic["x"] = int(x[3:])
    dic["m"] = int(m[2:])
    dic["a"] = int(a[2:])
    dic["s"] = int(s[2:-1])
    ps.append(dic)

accepted = []
for p in ps:
    wf_regex = r"^in\{(.+)\}$"
    while True:
        if wf_regex == "^A\{(.+)\}$" or wf_regex == "^R\{(.+)\}$":
            break
        match = re.search(wf_regex, workflows, re.MULTILINE)  #applies ^ and $ to each beginning/ending of line
        conds = match.group(1).split(",")
        #print(conds)
        for c in conds:
            if ":" in c:  #if full condition w/rule
                letter = c[0]
                num = re.search(r"(\d+):", c).group(1)
                goal = re.search(r":(.+)", c).group(1)
                #print("c:", c)
                #test condition:
                if c[1] == "<":
                    if p[letter] < int(num):
                        wf_regex = r"^" + goal + r"\{(.+)\}$"
                        if goal == "A":
                            accepted.append(p)
                        break
                else:
                    if p[letter] > int(num):
                        wf_regex = r"^" + goal + r"\{(.+)\}$"
                        if goal == "A":
                            accepted.append(p)
                        break
            else:
                if c == "A":
                    accepted.append(p)
                    wf_regex = r"^" + c + r"\{(.+)\}$"
                    break
                else:
                    wf_regex = r"^" + c + r"\{(.+)\}$"

all_sums = 0
for a in accepted:
    summer = 0
    for key in a.keys():
        summer += a[key]
    all_sums += summer
print(all_sums)

