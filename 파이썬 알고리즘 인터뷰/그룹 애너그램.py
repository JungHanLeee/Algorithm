import collections

words=["eat","tea","tan","ate","nat","bat"]

a=collections.defaultdict(list)
for word in words:
    a[''.join(sorted(word))].append(word)
print(a)
