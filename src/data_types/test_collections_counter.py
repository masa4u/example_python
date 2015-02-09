from collections import Counter


cnt = Counter()

for word in ['red', 'blue', 'red', 'greek', 'blue', 'blue']:
    cnt[word] += 1

print cnt

print cnt['red']