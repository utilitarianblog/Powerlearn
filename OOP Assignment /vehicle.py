# Base Class - Vehicle
class Vehicle:
    def move(self):
        print("🚗 Vehicle is moving")

# Derived Class - Car
class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road")

# Derived Class - Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky")

# Polymorphism in Action
vehicles = [Car(), Plane(), Vehicle()]

for v in vehicles:
    v.move()
