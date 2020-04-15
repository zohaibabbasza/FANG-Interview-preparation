pair = dict()
arr = [1,2,1,2,1,3,2]

s = 0
for i in arr:
    if i in pair:
        pair[i] += 1
        if pair[i] % 2 == 0:
            print(pair[i])
            print('true')
            s += 1
            pair[i] = 0
    else:
        pair[i] = 1

print(pair)
print(s)
