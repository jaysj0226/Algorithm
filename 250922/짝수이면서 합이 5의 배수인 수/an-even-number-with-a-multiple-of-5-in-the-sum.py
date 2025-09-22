n = int(input())

# Please write your code here.

def function(n):
    dat = [int(d) for d in str(n)]
    dat_sum = sum(dat)
    return (dat_sum % 5 == 0) and (dat[0] % 2 == 0)

if function(n):
    print("Yes")
else:
    print("No")