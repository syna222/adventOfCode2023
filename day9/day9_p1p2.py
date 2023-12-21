import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day9.txt").readlines()

def part_one():
    line_answers = []
    for line in file_data:
        super_array = []  #for all subarrays (calculations)
        array = line.split()
        array = [int(a) for a in array]
        super_array.append(array)
        while True:
            array = [array[i+1]-array[i] for i in range(len(array)-1)]
            super_array.insert(0, array)
            res = all(x == 0 for x in array)
            if res:
                break
        x = 0 #for finding num
        for i in range(len(super_array)-1):
            x += super_array[i+1][-1]
        line_answers.append(x)
    return sum(line_answers)
print(part_one())

def part_two():        
    line_answers = []
    for line in file_data:
        super_array = []  #for all subarrays (calculations)
        array = line.split()
        array = [int(a) for a in array]
        super_array.append(array)
        while True:
            array = [array[i+1]-array[i] for i in range(len(array)-1)]
            super_array.insert(0, array)
            res = all(x == 0 for x in array)
            if res:
                break
        x = 0 #for finding num
        for i in range(len(super_array)-1):
            x = super_array[i+1][0] - x
        line_answers.append(x)
    return sum(line_answers)
print(part_two())

