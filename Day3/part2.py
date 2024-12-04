import re

def process_file(filename):
    total = 0
    enabled = True
    
    with open(filename, "r") as f:
        content = f.read()
        
        # Process each instruction in order
        pos = 0
        while pos < len(content):
            # Check for control instructions
            do_match = re.match(r'do\(\)', content[pos:])
            dont_match = re.match(r"don't\(\)", content[pos:])
            mul_match = re.match(r'mul\((\d+),(\d+)\)', content[pos:])
            
            if do_match:
                enabled = True
                pos += len(do_match.group())
            elif dont_match:
                enabled = False
                pos += len(dont_match.group())
            elif mul_match and enabled:
                num1, num2 = map(int, mul_match.groups())
                total += num1 * num2
                pos += len(mul_match.group())
            else:
                pos += 1
                
    return total

print(process_file("input.txt"))