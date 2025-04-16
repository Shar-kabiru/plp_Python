# Defining a class
class Car:
    color = "red"  # Attribute

    # Method
    def drive(self):
        print("The car is driving 🚗")

# Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()

#Constructors
class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  # Output: blue
print(car2.model)  # Output: SUV

#Inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels)  # Output: 4
# Polymorphism
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())

#Encapsualtionclass SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

stash = SecretStash()
stash.take_chocolate()