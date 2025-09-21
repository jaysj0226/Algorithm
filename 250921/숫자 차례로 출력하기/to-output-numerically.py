n = int(input())

# Please write your code here.

def recursive(n):
    if n == 0:
        return
    recursive(n-1)
    print(n,end = " ")

def back_recursive(n):
    if n==0:
        return
    print(n, end= " ")
    back_recursive(n-1)
recursive(n)
print()
back_recursive(n)
