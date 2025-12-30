def make_into_digits(a, n):
    total = 0
    for digit in n:
        total = total * a + int(digit)
    return total

def make_into_B_num(n, b):
    res = []
    while n > 0:
        res.append(n % b)
        n //= b
    return res[::-1]

def main():
    a, b = map(int, input().split())
    n = input()
    n = make_into_digits(a,n)
    res = make_into_B_num(n,b)
    for i in res:
        print(i, end="")
    return

main()
    
