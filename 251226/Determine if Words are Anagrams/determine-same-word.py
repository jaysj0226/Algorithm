word1 = input()
word2 = input()

# Please write your code here.
word1 = sorted(word1)
word2 = sorted(word2)

res = "Yes" if word1 == word2 else "No"

print(res)