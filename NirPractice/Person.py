class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def speak(self):
        x = "Hi my name is " + self.name + " and I am {} feet tall"
        print(x.format(self.height))


person1 = Person("Nir", 5.8)
#Person Class

