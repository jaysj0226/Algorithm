a, b, c, d = map(int, input().split())

# Please write your code here.

h1 = a * 60 + b
h2 = c * 60 + d

ans = abs(h1-h2)
print(ans)