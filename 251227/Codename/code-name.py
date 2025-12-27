MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self,codename,score):
        self.codename = codename
        self.score = score

    def attribute(self):
        return self.codename, self.score

agents = []
for i in range(MAX_N):
    agents.append(Agent(codenames[i],scores[i]))

def who_is_low_score(arr):
    min_score = min(scores)
    for i in range(len(arr)):
        if arr[i].score == min_score:
            return arr[i]

res = who_is_low_score(agents)
print(res.codename, res.score)
