# define our Animal Code


# sudo code
# Looks / Characteristics of every animal
    # Name, Age, Colour, Heart, Brain

# Behaviours ? Methods of every animal
    # east, sleep, reproduce, potty, make_sound

class Animal():
    # define behaviour and characteristics

    # define characteristics of EVERY animal

    def __init__(self, name, age, colour):
        self.name = name # self refers to the instance
        self.age = age
        self.colour = colour
        self.heart = True
        self.brain = True

    # defining the method .eat(), sleep(), reproduce(), potty(), make_sound()
    def eat(self):
        return "nom nom nom nom"

    def sleep(self):
        return "zzzzzzZZZZZ"

    def reproduce(self):
        return "NSFW"

    def potty(self):
        return "0_0 HUMM!!! o_0 AHHHH! SPLOSH! o_o"

    def make_sound(self):
        return "Woof"


# To call methods we need an object of this class


# Creating an instance of class animal
print("Ringo")
ringo = Animal("Ringo", 200, "Blueish") # creates instance of class Animal and assigns it to variable ringo
# checking and printing the instance
print(ringo)
print(type(ringo))

# Calling methods on instance of Animal
print(ringo.eat())
print(ringo.potty())
print(ringo.sleep())


# Check the Attribute of an Instance
print(ringo.name)   # ringo becomes self as is the instance variable
print(ringo.age)


# Create a second animal
print("mini")
mini = Animal("Stacy", 25, "Greenish")
print(mini.name)
print(mini.age)
print(mini.colour)
