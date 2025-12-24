n = int(input())

# Please write your code here.
bin_res = []
while True:
    if n < 2:
        bin_res.append(n)
        break

    bin_res.append(n%2)
    n //= 2

for binary in bin_res[::-1]:
    print(binary, end="")