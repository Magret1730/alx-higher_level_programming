# When we create a class, we can inherit all of its field and methods
# from another class. This is called INHERITANCE.

# The class that inherits is called the SUB CLASS and the class we
# inherit from is called the SUPER CLASS.

# SUPER CLASS
class Animal:
    def __init__(self, birthType="Unknown",
                  appearance="Unknown",
                  blooded="Unknown"):
        self.__birthType = birthType
        self.__appearance = appearance
        self.__blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    #can be used to cast our object as a string
    # type(self).__name__ returns the class name
    def __str__(self):
        return "A {} is {} it is {} it is {}" \
                .format(type(self).__name__,
                                           self.birthType,
                                           self.appearance,
                                           self.blooded)

# Create a mammal class that inherits from Animal
# You can inherit from multiple classes by separating
# the classes with a coma in the parenthesis
class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurseYoung="True"):

        # Call for the super class to intialize fields
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overwrite __str__
    # You can use super() to refer to the superclass
    def __str__(self):
        return super().__str__() + "and it is {} they nurse " \
               "their young".format(self.nurseYoung)

class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive",
                 appearance="dry scales",
                 blooded="cold blooded"):

        # Call for the super class to initialize fields
        Animal.__init__(self, birthType, appearance, blooded)

    # Operator overloading isnt necessary in Python because Python allows
    # you to enter unknown numbers of values. Always make sure self is the
    # first attribute in your class methods
    def sumAll(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum

def main():
    animal1 = Animal("born alive")
    print(animal1.birthType)

    # Call __str__()
    print(animal1)
    print()

    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print()

    reptile1 = Reptile()
    print(reptile1.birthType)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print()

    # result = Animal.sumAll(i for i in range(20))

    # Operate overloading in Python
    print("Sum : {}".format(reptile1.sumAll(1, 2, 3, 4, 5)))

if __name__ == "__main__":
    main()
