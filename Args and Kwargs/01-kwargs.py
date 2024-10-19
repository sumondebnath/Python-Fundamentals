
class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        self.make = kwargs.get("make")
        # self.model = kwargs["model"]
        self.model = kwargs.get("model")


# my_car = Car(make="Russia", model="janina")
my_car = Car(make="Russia")

# print(my_car)
print(my_car.model)
print(my_car.make)