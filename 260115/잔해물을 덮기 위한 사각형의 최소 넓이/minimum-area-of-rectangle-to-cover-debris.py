OFFSET = 1000
MAX_R = 2000 

rects = 2
lines = [tuple(map(int, input().split())) for _ in range(rects)]

blocks = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

def paint(idx, line):
    x1, y1, x2, y2 = line

    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            blocks[x][y] = idx 

def bounding_area_for_first():
    min_x, max_x = MAX_R, 0
    min_y, max_y = MAX_R, 0
    exist = False

    for x in range(MAX_R + 1):
        for y in range(MAX_R + 1):
            if blocks[x][y] == 1:
                exist = True
                min_x = min(min_x,x)
                max_x = max(max_x,x)
                min_y = min(min_y,y)
                max_y = max(max_y,y)

    if not exist:
        return 0
    return (max_x - min_x + 1) * (max_y - min_y + 1)

def simulation():
    for idx, line in enumerate(lines, start=1):
        paint(idx, line)

    print(bounding_area_for_first())

simulation()
