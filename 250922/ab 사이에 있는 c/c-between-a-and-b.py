arr = list(map(int,input().split()))

cnt = []
for i in range(arr[0],arr[1]+1):
    if i % arr[-1] == 0:
       cnt.append(1)
if 1 in cnt:
    print("YES")
else:
    print("NO") 