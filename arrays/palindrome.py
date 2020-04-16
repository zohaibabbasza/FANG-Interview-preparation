x = -121
x_ = str(x)
if x < 0:
    print('false')
else:
    if int(x_[::-1])  == x:
        print('true')
    else:
        print('false')