words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

d = dict()
for i in words:
    for j in i:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

print(d)