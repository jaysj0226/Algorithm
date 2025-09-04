n, m = map(int, input().split())

# Please write your code here.

def sol(n,m):
    res_arr = []
    a = max(n,m)
    for i in range(1,a+1):
        if (n%i==0) and (m%i==0):
            res_arr.append(i)
    
    res = 1
    for i in res_arr:
        res = res * i

    print(res)

sol(n,m)
    