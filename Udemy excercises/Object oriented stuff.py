class Food():

#Class Object attribute
    edible = True
    

    def __init__(self, size, colour):

        self.size = size
        self.colour = colour

    #Methods
    def eat(self):
        self.size -= 1

    #Special methods
    def __str__(self):
        return f"This food's size is {self.size} and it is {self.colour}."




apple = Food(87, "Red")

print(apple.size)
apple.eat()
print(apple.size)

print(apple)
