n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
MAX_NUM = 1000
# Please write your code here.
def lines(arr,segment):
    first, last = segment
    for i in range(first,last+1):
        arr[i] += 1

def simulation():
    arr = [0] * MAX_NUM
    for segment in segments:
        lines(arr,segment)
    print(max(arr))
simulation()
    