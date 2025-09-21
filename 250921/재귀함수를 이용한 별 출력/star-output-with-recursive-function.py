n = int(input())

# Please write your code here.

def printing_star(n):
    if n == 0:
        return
        
    printing_star(n-1)
    print("*"*n)

printing_star(n)