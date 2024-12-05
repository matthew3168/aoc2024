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
    
    flag = False
    for number_length in range(len(row_split)):
        for j in range(number_length + 1, len(row_split)):
            if [row_split[j], row_split[number_length]] in rules:  
                flag = True
                break
        if flag:
            break
    #bumblebee sortinggggg
    if flag:
        swapped = True
        while swapped:
            swapped = False
            for k in range(len(row_split) - 1):
                if [row_split[k+1], row_split[k]] in rules:  #if rule opposite, swap
                    row_split[k], row_split[k+1] = row_split[k+1], row_split[k]
                    swapped = True
        
        # Add middle number to count
        print("fixed:", row_split, "middle:", row_split[int((len(row_split)-1)/2)])
        count += int(row_split[int((len(row_split)-1)/2)])

print(count)

f1.close()
g.close()