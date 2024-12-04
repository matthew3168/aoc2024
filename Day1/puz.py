from collections import defaultdict
f = open("input.txt", "r")
left = defaultdict(int)
right = defaultdict(int)
total = 0
for row in f:
    s = row.split()
    left[int(s[0])] += 1
    right[int(s[1])] += 1

# while True:
#     if len(left) == 0:
#         break
#     else:
#         left_min = min(left.keys())
#         right_min = min(right.keys())
#         if left[left_min] == 1:
#             del left[left_min]
#         else:
#             right[right_min] -=1
#         if right[right_min] == 1:
#             del right[right_min]
#         else:
#             right[right_min] -=1
#         i = abs(left_min-right_min)
#         total += i

for i in left:
    if right.get(i):
        total += left[i]*i*right.get(i)

print(total)