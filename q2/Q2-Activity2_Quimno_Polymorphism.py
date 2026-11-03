# 1.
# a. What is duck typing, as explained in the video?
# Answer: Duck typing is another way to achieve polymorphism besides inheritance. Objects can be treated as if they are a different type as long as they meet the minimum necessary attributes and methods required of them. The adage is: "If it looks like a duck and quacks like a duck, it must be a duck."

# b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
# Answer: The Car class needed to have a method named speak() (instead of horn()) and an attribute named alive, matching the minimum requirements called inside the animal loop.

# 2.
# a. Create three separate classes with a move() method
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

# b. Standalone function that calls the move() method dynamically
def start_trip(vehicle):
    vehicle.move()

if __name__ == "__main__":
    print("Output:")
    
    # c. Create one object of each class
    car_obj = Car()
    boat_obj = Boat()
    drone_obj = Drone()

    # d. Call the start_trip() method for each object
    start_trip(car_obj)
    start_trip(boat_obj)
    start_trip(drone_obj)

# 3. How does the code demonstrate polymorphism?
# The code demonstrates polymorphism because the unified interface function start_trip(vehicle) can take entirely unrelated objects (none of which inherit from a common parent or base class) and execute vehicle.move() seamlessly.
# Python acts on duck-typing rules here. It doesn't care what type of vehicle object is passed in; it only cares that the object possesses the executable .move() method capability, producing unique behaviors for each instance at runtime.
