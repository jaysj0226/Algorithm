n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
MAX_NUM = 1000
OFFSET = 100

# Please write your code here.
def lines(arr,segment):
    first, last = segment
    first,last = first + OFFSET, last + OFFSET
    for i in range(first,last):
        arr[i] += 1

def simulation():
    arr = [0] * MAX_NUM
    for segment in segments:
        lines(arr,segment)
    print(max(arr))
simulation()
    