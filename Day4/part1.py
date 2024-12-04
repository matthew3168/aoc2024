f = open("input.txt", "r")
table = []

for i in f:
    row = []
    for j in range(len(i)-1):
        row.append(i[j])
    table.append(row) #2d list


def count(grid):
    rows = len(grid) #number of rows and columns
    cols = len(grid[0])
    
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def check(row, col, dx, dy, word): #fuction to check current letter if it is the word
        curr_row, curr_col = row, col #initialize current pos
        
        for letter in word:
            if (curr_row < 0 or curr_row >= rows or #if out or boundary or not the letter, return false
                curr_col < 0 or curr_col >= cols or 
                grid[curr_row][curr_col] != letter):
                return False
            curr_row += dx #if is correct letter change to next position (e.g. if moving left (-1, 0) then it will move left again using the same direction)
            curr_col += dy
        return True
    
    total = 0
    
    # pointer iterates through each position
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "X": #skip immediately if starting letter not X
                pass
            for dx, dy in directions:
                if check(row, col, dx, dy, "XMAS"):
                    total += 1
    
    return total

print(count(table))