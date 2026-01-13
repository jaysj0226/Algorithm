n = int(input())
segments = [tuple(map(str,input().split())) for _ in range(n)]
MAX_NUM = 1000
# Please write your code here.
def print_ans(arr):
    return len([x for x in arr if x >= 2])
def simulation():
    arr = [0] * MAX_NUM
    nxt_pos=0
    pos = 0
    for segment in segments:
        length, way = segment
        if way == "R":
            nxt_pos = pos + int(length)
            for i in range(pos,nxt_pos):
                arr[i] += 1
        else:
            nxt_pos = pos - int(length)
            for i in range(nxt_pos,pos):
                arr[i] += 1

        pos = nxt_pos
    print(print_ans(arr))

simulation()
    