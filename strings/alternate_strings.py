s = 'AAABBB'

i = 0 
count = 0
while True:
    try:
        temp = s[i]
        if s[i+1] == temp:
            count += 1
        if i == len(s):
            break
        i += 1
    except: 
        break
print(count)

