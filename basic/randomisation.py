import random

random_int = random.randint(1, 20)

print(random_int)

random_float = random.random()

print(random_float)


random_side = random.randint(0, 1)

if(random_side):
    print("Head")

else: 
    print("Tails")