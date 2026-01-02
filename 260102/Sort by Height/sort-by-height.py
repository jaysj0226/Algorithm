n = int(input())
people = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append((n_i,int(h_i),int(w_i)))
# Please write your code here.
people.sort(key=lambda x: x[1])
for name,height,weight in people:
    print(name, height, weight)