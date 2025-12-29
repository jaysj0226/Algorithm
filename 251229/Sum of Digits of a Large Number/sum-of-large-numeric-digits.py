a, b, c = map(int, input().split())

# Please write your code here.
def multiply(a,b,c):
    res = a*b*c
    return res

def get_sum(a):
    if a < 10:
        return a
    return get_sum(a // 10) + (a % 10)

def main():
    re = multiply(a,b,c)
    return get_sum(re)

print(main())