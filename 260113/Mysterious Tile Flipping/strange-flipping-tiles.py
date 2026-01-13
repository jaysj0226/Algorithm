n = int(input())
commands = [input().split() for _ in range(n)]

MAX_MOVE = n * 100
OFFSET = MAX_MOVE
SIZE = 2 * MAX_MOVE + 1

tiles = [-1] * SIZE
pos = 0

for x, d in commands:
    x = int(x)

    if d == 'R':
        l, r = pos, pos + x          
        color = 1
        pos = pos + x - 1            
    else:
        l, r = pos - x + 1, pos + 1  
        color = 0
        pos = pos - x + 1            

    l += OFFSET
    r += OFFSET

    for i in range(l, r):
        tiles[i] = color

white = sum(1 for t in tiles if t == 0)
black = sum(1 for t in tiles if t == 1)

print(white, black)
