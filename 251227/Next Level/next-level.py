user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self,user_id="codetree", user_level=10):
        self.user_id = user_id
        self.user_level = user_level
    
    def attribute(self):
        return self.user_id, self.user_level

user1 = User()
user2 = User(user2_id, user2_level)
print(f"user {user1.attribute()[0]} lv {user1.attribute()[1]}")
print(f"user {user2.attribute()[0]} lv {user2.attribute()[1]}")
    