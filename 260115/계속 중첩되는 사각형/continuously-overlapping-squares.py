n = int(input())
OFFSET = 100
MAX_N = 201
# Please write your code here.
lines = [tuple(map(int,input().split())) for _ in range(n)]
areas = [[0]*MAX_N for _ in range(MAX_N)]

def get_area(idx,line):
    x1,y1,x2,y2 = line
    x1 += OFFSET; y1 += OFFSET; x2 += OFFSET; y2 += OFFSET

    val = 2 if idx%2 else 1
    for i in range(x1,x2):
        for j in range(y1,y2):
            areas[i][j]=val


def print_ans():
    print(sum(1 for area in areas for i in area if i == 2))

# 처음에 빨, 다음 파 --> 0 : 빨, 1 : 파 --> 짝 : 빨, 홀 : 파
def simulation():
    for idx,line in enumerate(lines):
        get_area(idx,line)
    
    print_ans()

simulation()


