s = "1?:??"
s = s.split(':')
hour = list(s[0])
minute = list(s[1])    
if hour[0] == '?':
        if hour[1] < '4':
            hour[0] = '2'
        elif hour[1]== '?':
            hour[0] = '2'
        else:
            hour[0] = 1
if hour[1] == '?':
    if hour[0] == '0' and hour[1] == '?':
        hour[1] = '9'
    elif hour[0] == '1' and hour[1] == '?':
        hour[1] = '9'
    else:
        hour[1] = '3'

if minute[0] == '?':
        minute[0] = '5'
if minute[1] == '?':
        minute[1] = '9'

hour = ''.join(hour)
minute = ''.join(minute)
print(hour+ ':' +minute)