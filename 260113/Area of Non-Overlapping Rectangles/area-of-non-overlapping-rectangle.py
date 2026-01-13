x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
def area(i):
    return max(0, x2[i] - x1[i]) * max(0, y2[i] - y1[i])

def overlap(i, j):
    w = max(0, min(x2[i], x2[j]) - max(x1[i], x1[j]))
    h = max(0, min(y2[i], y2[j]) - max(y1[i], y1[j]))
    return w * h

# A와 B의 남은 면적
remain = area(0) + area(1) - overlap(0, 2) - overlap(1, 2)
print(remain)
