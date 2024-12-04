f = open("input.txt", "r")
table = []

for i in f:
    row = []
    for j in range(len(i)-1):
        row.append(i[j])
    table.append(row)

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for row in range(1, rows-1):  # skip edges since we need diagonals
        for col in range(1, cols-1):
            # For center pos, we need M,A,S in diagonal pattern
            center = grid[row][col]
            if center == 'A':  # only check if center is 'A'
                # Check diagonal pattern matches
                # Top-left to bottom-right
                if (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
                    # Top-right to bottom-left
                    if (grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S') or (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M'):
                        count += 1
    
    return count

# Read input

print(count_xmas_patterns(table))