x = 1022016516919819
s = ''


if x == 0:
    print(0) 
if x < 0:
    s += '-'
    x = abs(x)
zero_check = False
s_ =  str(x)
for i in range(len(s_),0,-1):
    print(s_[i-1])
    if s_[i-1] != '0':
        zero_check = True
    if zero_check:
        s += s_[i-1]
max_ = 2147483648
print(s)
if int(s) > max_ -1 or int(s) < max_*-1 :
    print(s)
        #return 0
print(s)


    