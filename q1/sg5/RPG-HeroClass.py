class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 120)

arthur.take_damage(10)

<<<<<<< HEAD
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")
=======
# arthur.take_damage(10)

# print(arthur.hp)     # Expected: 90
# print(morgana.hp)    # Expected: 100


# this is sodium
>>>>>>> upstream/main
