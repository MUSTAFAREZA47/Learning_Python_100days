class User:
    # creating attribute of class
    def __init__(self, id, user_name, address):
        self.id = id
        self.user_name = user_name
        self.address = address
        self.followers = 0
        self.following = 0
    
    # creating class method
    
    def follow(self, user):
        user.followers += 1
        user.following += 1
        

user_1 = User("001", "Ahmed", "Sasaram")
user_2 = User("002", "Hamid", "UP")

# creating attributes 
# user_1.id = "001"
# user_1.name = "Ahmed"
# user_1.address = "sasaram"

# print(user_1.user_name)

user_1.follow(user_2)

print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)


