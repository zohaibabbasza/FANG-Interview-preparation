from collections import Counter 

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
count = 0

if a >= b:
    larger = a
    smaller = b
else:
    larger = b
    smaller = a

words = dict()

for i in larger:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

for i in smaller:
    if i in words and words[i] > 0:
        words[i] -= 1
        count += 1
diff_smaller = len(smaller) - count
diff_larger = len(larger) - len(smaller)

print(2*diff_smaller + diff_larger)
