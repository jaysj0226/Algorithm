n = int(input())

# Please write your code here.
def print_word(n):
    if n == 0:
        return
    print("HelloWorld")
    print_word(n-1)

print_word(n)