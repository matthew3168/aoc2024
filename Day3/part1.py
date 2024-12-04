import re

f = open("input.txt", "r")
l= []
pattern = r"mul\((\d+),(\d+)\)"
m = r"\d"
counter = 0
for row in f:
    l = re.findall(pattern, row)
    for i in l:
        counter += (int(i[0])*int(i[1]))

print(counter)