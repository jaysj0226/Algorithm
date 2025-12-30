binary = input()

# Please write your code here.
def make_into_digits(binary):
    binary = binary[::-1]
    digits = 0
    for i in range(len(binary)):
        digits += int(binary[i]) * (2**i)
    return digits

print(make_into_digits(binary))