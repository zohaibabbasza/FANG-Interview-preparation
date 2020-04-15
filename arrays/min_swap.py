arr = [2,3,4,1,5]
count = 0
i = 0
while i != len(arr):
    if arr[i]-1 != i:
        arr[arr[i]-1], arr[i] = arr[i],arr[arr[i]-1]
        count += 1
    else:
        i += 1

print(arr)
print(count)