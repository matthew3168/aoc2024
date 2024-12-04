
f = open("input.txt", "r")
safe = 0
for row in f:

    w = row.split()
    flag = True
    rule = True #initialize to say there is 1 bad level tolerance still
    if int(w[0]) < int(w[1]): #if first 2 is increasing assume all is increasing
        for i in range(len(w)-2): #until second last number to check if all is decreasing
            if int(w[i]) >= int(w[i+1]) or int(w[i+1]) - int(w[i]) >3: #if decreasing/equal or difference more than 3
                if rule:
                    rule = False #no more tolerance after this
                    if int(w[i-1]) >= int(w[i+1]) or int(w[i+1]) - int(w[i-1]) >3:
                        flag = False
                        break 
                else:
                    flag = False
                    break

    elif int(w[0]) > int(w[1]): #assume decreasing
        for i in range(len(w)-2): #until second last number to check if all is decreasing
            if int(w[i]) <= int(w[i+1]) or int(w[i]) - int(w[i+1]) >3: #if increasing/equal or difference more than 3
                if rule:
                    rule = False #no more tolerance after this
                    if int(w[i-1]) <= int(w[i+1]) or int(w[i]) - int(w[i+1]) >3:
                        flag = False
                        break 
                else:
                    flag = False
                    break
    else:
        flag = False        
    if flag:
        safe +=1

print(safe)