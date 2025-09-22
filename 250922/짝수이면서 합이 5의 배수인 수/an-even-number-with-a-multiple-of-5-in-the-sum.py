n = int(input())

# Please write your code here.
def whether_is(n):
    ten = n // 10
    one = n % 10
    return ((ten + one) % 5 == 0) and (one%2==0)

def function(n):
    dat = [int(d) for d in str(n)]
    dat_sum = sum(dat)
    return (dat_sum % 5 == 0) and (dat[0] % 2 == 0)
    
if function(n):
    print("Yes")
else:
    print("No")