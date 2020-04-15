
ar = ['U','D','D','D','U','D','U','U']

level = valley = 0

for i in ar:
    if i == 'U':
        level += 1
    else:
        level -= 1
    if level == 0 and i == 'U':
        valley += 1
print(valley)
