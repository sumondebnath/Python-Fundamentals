class Person:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.followers = 0
        self.following = 0

    def Follow(self, user):
        user.followers += 1
        self.following += 1


sumon = Person("sumon", "Sumon", "Debnath")

print(sumon)
print(sumon.username)
print(sumon.first_name, sumon.last_name)

# print(sumon.followers)
# sumon.followers = 100
# print(sumon.followers)

manu = Person("manu", "Manu", "Debnath")

sumon.Follow(manu)

print(sumon.followers)
print(sumon.following)

print(manu.followers)
print(manu.following)