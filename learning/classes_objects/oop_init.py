class Person:
    def __init__(self, name):  # name is a field. init, say_hi() are methods. p is object or instance.
        self.name = name
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Magret")
p.say_hi()
Person("Magret").say_hi()
