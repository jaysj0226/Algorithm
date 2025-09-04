n, m = map(int, input().split())

# Please write your code here.

def sol(n,m):
    res = []
    a = max(n,m)

    for i in range(1,a+1):
        if (n % i == 0) and (m % i == 0):
            res.append(i)
    
    print(max(res))

sol(n,m)