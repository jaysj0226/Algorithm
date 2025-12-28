unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

    def attribute(self):
        return self.unlock_code, self.wire_color, self.seconds


bomb = Bomb(unlock_code, wire_color, seconds)
print(f"code : {bomb.attribute()[0]}")
print(f"color : {bomb.attribute()[1]}")
print(f"second : {bomb.attribute()[2]}")