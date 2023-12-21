import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day15.txt").read()
sequences = file_data.split(",")

def part_one():
    summator = 0
    for seq in sequences:
        curr_val = 0
        for s in seq:
            #turn s into ascii:
            curr_val += ord(s)
            curr_val *= 17
            curr_val %= 256
        summator += curr_val
    return summator

def get_hash(label):
    curr_val = 0
    for l in label:
        #turn s into ascii:
        curr_val += ord(l)
        curr_val *= 17
        curr_val %= 256
    return curr_val

def part_two():
    boxes = {}
    for seq in sequences:
        label = re.search(r"[a-z]+", seq).group(0)
        box_num = get_hash(label)
        operation = re.search(r"=|\-", seq).group(0)
        if operation == "-":
            if box_num in boxes.keys():
                if label in boxes[box_num].keys():
                    del boxes[box_num][label]
        if operation == "=":
            foc_len = re.search(r"=(\d+)", seq).group(1)
            if box_num not in boxes.keys():
                boxes[box_num] = {}
            boxes[box_num][label] = foc_len          
            
    all_focus_power = 0
    for box_num in boxes.keys():
        for lens in boxes[box_num].keys():
            lens_slot = list(boxes[box_num].keys()).index(lens)
            lens_power = (box_num + 1) * (lens_slot + 1) * int(boxes[box_num][lens])
            all_focus_power += lens_power      
    return all_focus_power   

print(part_one())
print(part_two())