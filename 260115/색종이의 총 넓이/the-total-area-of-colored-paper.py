MAX_N = 201
OFFSET = 100
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
areas = [[0] * MAX_N for _ in range(MAX_N)]

# Please write your code here.
def get_area(p):
    x,y = p
    x += OFFSET
    y += OFFSET
    for i in range(x,x+8):
        for j in range(y,y+8):
            areas[i][j] = 1
    
def print_ans():
    ans = []
    for area in areas:
        for i in area:
            if i == 1:
                ans.append(1)
    print(sum(ans))

def simulation():
    for starting_point in points:
        get_area(starting_point)
    
    print_ans()

simulation()