N = int(input())
command = []
A = []

        
def empty(arr):
    return len(arr) == 0

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    elif line[0] == "empty":
        print(1 if empty(A) else 0)
    elif line[0] == "size":
        print(len(A))
    elif line[0] == "front":
        print(A[0])
    elif line[0] == "pop":
        print(A[0])
        A.pop(0)
    
     

# Please write your code here.

