s = "abccccdd"

d = dict()

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

pairs = 0
odd_check = False
for i in d.values():
    if i % 2 != 0:
        odd_check = True
    pairs += i//2
        
if odd_check:
    print(pairs * 2 + 1)
else:
    print(pairs*2)