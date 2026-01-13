n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
MAX_CARD = 2001
# Please write your code here.
cards = [-1] * MAX_CARD

pos = 0
nxt_pos = 0
for num, direction in commands:
    if direction == "R":
        nxt_pos = pos + int(num)
        for i in range(pos,nxt_pos):
            cards[i] = 1
    else:
        nxt_pos = pos - int(num)
        for i in range(nxt_pos,pos):
            cards[i] = 0
    pos = nxt_pos

print(sum(1 for i in cards if i == 0), sum(1 for i in cards if i == 1))
