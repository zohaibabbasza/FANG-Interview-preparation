s = "anviaj"

d = dict()
p = []
n = []
i = 0

while i != len(s):
    if s[i] in d:
        d[s[i]] += 1
        if len(p) > len(n) :
            n = p
            p = []
            del d[s[i]]
    else:
        d[s[i]] = 1
        p.append(s[i])
    i+=1
print(n)
print(p)
if len(n) <= len(p):
    n = n + p
print(len(set(n)))
