MAX_NUM = 1002
essential_num = (1920,2880)
minimal, maxinum = map(int,input().split())
cnt = [0] * MAX_NUM

for i in range(minimal, maxinum+1):
    if (essential_num[0] % i == 0) and (essential_num[1] % i == 0):
        cnt[i] = 1
    
if 1 in cnt:
    print(1)
else:
    print(0)