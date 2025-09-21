N = int(input())

# Please write your code here.
def printing(N):
    if N == 0:
        return
    print(N, end = " ")
    printing(N-1)
    print(N, end = " ")
    
printing(N)