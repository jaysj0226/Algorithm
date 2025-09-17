str = input()
str = list(str)

# Please write your code here.
cnt = 0
for i in range(len(str)):
    if str[i] == "(":
        cnt += 1
    else:
        cnt -= 1

if cnt == 0:
    print("Yes")
else:
    print("No")
        


    
