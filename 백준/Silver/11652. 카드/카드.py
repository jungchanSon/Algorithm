import sys 
input = sys.stdin.readline

n = int(input())
card_dict = dict()

for _ in range(n):
    card = int(input())
    if card_dict.get(card):
        card_dict[card] += 1
    else:
        card_dict[card] = 1

mx = -1
ans = str()
for i in card_dict.keys():
    if card_dict[i] > mx:
        ans = i
        mx = card_dict[i]
    elif card_dict[i] == mx:
        ans = sorted([ans, i])[0]
print(ans)