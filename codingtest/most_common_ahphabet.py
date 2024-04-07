import sys

arr = input().upper()

dictionary = {}
for i in arr:
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1

u = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)

if len(u) > 1 and u[0][1] == u[1][1]:
    print('?')
else:
    print(u[0][0])
