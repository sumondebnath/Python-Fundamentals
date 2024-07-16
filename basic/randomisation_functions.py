import random

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(random.choice(char))

print(random.choices(char))

print(char)

random.shuffle(char)
print(char)