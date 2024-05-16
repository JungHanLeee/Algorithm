import sys
input = sys.stdin.readline
n = int(input())
dict_players = {}
result = ['PREDAJA']
for i in range(n):
    player = input()
    name = list(player)
    if name[0] not in dict_players:
        dict_players[name[0]] = 1
    else:
        dict_players[name[0]] += 1
sorted_players = dict(sorted(dict_players.items()))
for key,value in sorted_players.items():
    if value >= 5:
        result.append(key)
if len(result) < 2:
    print(result[0])
else:
    print(''.join(result[1:]))