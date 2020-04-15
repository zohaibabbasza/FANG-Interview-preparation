d = 4
#a = [33,47,70,37,8,53,13,93,71,72,51,100,60,87,97]
a = [1,2,3,4,5]
n = len(a)
new_a = a.copy()
for i in range(n):
    print(a[i])
    print(a)
    new_index = (i + n - d) % n
    new_a[new_index] = a[i]
print(new_a)