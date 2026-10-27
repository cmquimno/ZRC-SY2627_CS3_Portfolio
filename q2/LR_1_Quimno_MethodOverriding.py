# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name  

    def feed(self):
        return f"{self.name} is eating."

    def make_sound(self):
        return f"{self.name} makes a sound."

# Child Class 1
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)  # Reuses parent constructor logic

    # METHOD OVERRIDING
    def make_sound(self):
        return f"{self.name} roars loudly!"

    # METHOD OVERRIDING
    def feed(self):
        return f"{self.name} eats fresh meat."

# Child Class 2
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    # METHOD OVERRIDING
    def make_sound(self):
        return f"{self.name} trumpets!"

    # METHOD OVERRIDING
    def feed(self):
        return f"{self.name} eats grass and fruits."

# Child Class 3
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    # METHOD OVERRIDING
    def make_sound(self):
        return f"{self.name} chatters!"

    # METHOD OVERRIDING
    def feed(self):
        return f"{self.name} eats bananas."

if __name__ == "__main__":
    lion = Lion("Simba")
    elephant = Elephant("Dumbo")
    monkey = Monkey("George")

    print(lion.make_sound())
    print(lion.feed())
    print("-----")

    print(elephant.make_sound())
    print(elephant.feed())
    print("-----")

    print(monkey.make_sound())
    print(monkey.feed())
    print("-----")