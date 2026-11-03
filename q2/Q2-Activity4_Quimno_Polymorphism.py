# 1. Create three classes with a use() method
class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

# 2. Function with parameter item that calls use()
def apply_item(item):
    item.use()  # Fixed the teacher's text typo 'item.user();' to proper Python

if __name__ == "__main__":
    # 3. Create one object of each class
    health = HealthPotion()
    mana = ManaPotion()
    speed = SpeedBoost()

    # 4. Store the objects in a list named potions
    potions = [health, mana, speed]

    # Call apply_item() for each object using a loop
    for item in potions:
        apply_item(item)
