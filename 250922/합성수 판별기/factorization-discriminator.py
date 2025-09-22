n = int(input())

cnt = []
def simulate(n):
    for i in range(2,n):
        if n % i == 0:
            cnt.append(1)
        
simulate(n)
if 1 in cnt:
    print('C')
else:
    print('N')