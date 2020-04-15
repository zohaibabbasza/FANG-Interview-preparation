s = 'aabbccddeefghi'

checker = dict()

for i in s:
    if i in checker:
        checker[i] += 1 
    else:
        checker[i] = 1
flag = 0
total_count = 0
i =0 
while True:
    try:
        total_count += checker[s[i]]
        if checker[s[i]] != checker[s[i+1]] :
            if checker[s[i]] == 1:
                flag = 1
                del checker[s[i]]
                s = s.replace(s[i],"")
            elif checker[s[i + 1]] == 1:
                flag = 1
                del checker[s[i+1]] 
                s=s.replace(s[i+1],"")
            else:
                if checker[s[i]] - checker[s[i+1]] == abs(1):
                    if flag == 0:
                        flag = 1
                        if checker[s[i]] > checker[s[i+1]]:
                            checker[s[i]] -= 1
                        else:
                            checker[s[i+1]] -= 1
                    else:
                        break
        i+=1
    except:
        break
if list(checker.values())[0] * len(s) == total_count  :
    print('YES')
else:
    print('NO')    

