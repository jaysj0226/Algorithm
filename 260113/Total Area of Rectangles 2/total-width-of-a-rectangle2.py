MAX_R = 200
OFFSET = 100
n = int(input())
xy = [tuple(map(int,input().split())) for _ in range(n)]
cnt_arr = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]
# Please write your code here.

for x1,y1,x2,y2 in xy:
    x1,y1 = x1 + OFFSET,y1 + OFFSET
    x2,y2 = x2 + OFFSET,y2 + OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            cnt_arr[x][y] = 1

area = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if cnt_arr[x][y]:
            area += 1
print(area)