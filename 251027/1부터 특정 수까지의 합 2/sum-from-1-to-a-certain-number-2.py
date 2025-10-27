N = int(input())

# Please write your code here.
def hap(n):
    if n == 1:
        return 1
    return n + hap(n-1)

print(hap(N))