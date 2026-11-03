# 1. Create three classes with a special_move() method
class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

# 2. Function with parameter character that calls special_move()
def perform_move(character):
    character.special_move()

if __name__ == "__main__":
    # 3. Create one object of each class
    warrior = Warrior()
    mage = Mage()
    archer = Archer()

    # 4. Store the objects in a list named characters
    characters = [warrior, mage, archer]

    # Call perform_move() for each object using a loop
    for character in characters:
        perform_move(character)
