N = int(input())

# Please write your code here.

def what_is_N(n):
    arr=[]
    # odd
    if n % 2:
        for i in range(1,n+1,2):
            arr.append(i)
        return arr
    # even
    else:
        for i in range(2,n+1,2):
            arr.append(i)
        return arr

def f(n):
    arr = what_is_N(n)
    return sum(arr)

print(f(N))



