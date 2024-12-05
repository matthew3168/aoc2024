f1 = open("input.txt", "r")
g = open("input2.txt", "r")
rules = []
count = 0
for row in f1:
    row = row.strip("\n")
    rules.append(row.split("|"))

for i in g:
    i = i.strip('\n')
    row_split = i.split(",")
    print(row_split)
    flag = True
    for number_length in range(len(row_split)-1):
        print([row_split[number_length], row_split[number_length+1]])
        if [row_split[number_length], row_split[number_length+1]] not in rules:
            flag = False
            break
    if flag:
        print(flag, count, int(row_split[int((len(row_split)-1)/2)]))
        count += int(row_split[int((len(row_split)-1)/2)])
print(count)