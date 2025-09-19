n = int(input())

# Please write your code here.
def add_and_divide(n):
    a = 0
    for i in range(1,n+1):
        a += i
    return int(a / 10)

print(add_and_divide(n))

