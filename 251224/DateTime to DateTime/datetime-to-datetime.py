from datetime import datetime
a, b, c = map(int, input().split())

# Please write your code here.

start = datetime(2011,11,11,11,11)
end = datetime(2011,11,a,b,c)

t = int((end-start).total_seconds()) // 60
print(t if t >= 0 else -1)