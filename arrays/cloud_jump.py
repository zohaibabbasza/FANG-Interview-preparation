c = [0,0,0,1,0,0]
s = len(c)
i = 0
jumps = 0
while True:
    if i + 2 < s and c[ i + 2 ] == 0:
        i +=2 
    elif i + 1 < s and c[i+1] == 0:
        i += 1
    else:
        break
    jumps +=1

print(jumps)