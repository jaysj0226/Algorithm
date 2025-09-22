n = int(input())

# Please write your code here.
def whether_is(n):
    ten = n // 10
    one = n % 10
    return ((ten + one) % 5 == 0) and (one%2==0)

if whether_is(n):
    print("Yes")
else:
    print("No")