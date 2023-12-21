import re

file_data = open(r"C:\Users\vck\Documents\CODING\Python Scripts\AOC2023\day1.txt").readlines()

def part_one(file_data):
    digits_list = []
    for line in file_data:
        digit_sublist = []
        for char in line:
            if char.isdigit():
                digit_sublist.append(char)
        digits_list.append(digit_sublist)
    sum_list = [int(str(x[0]) + str(x[-1])) for x in digits_list]
    return sum(sum_list)
print(part_one(file_data))
    
def part_two(file_data):
    line_numbers = []
    search_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    counter = 0
    for line in file_data:
        line_dict = {}
        for term in search_list:
            res = re.finditer(term, line)
            for match in res:
                line_dict[match.end()] = match.group()
        #sort dict + get first/last num
        line_dict = dict(sorted(line_dict.items()))
        line_dict = {key: replacers.get(value, value) if not value.isdigit() else value for key, value in line_dict.items()}
        values_list = list(line_dict.values())
        number = int(values_list[0] + values_list[-1])
        counter += 1
        line_numbers.append(number)
    return sum(line_numbers)  
print(part_two(file_data))

  
    
    
    
    
    
    
    
    
    
    
