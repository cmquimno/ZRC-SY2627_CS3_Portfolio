# Optional Activity: Code Review

### ❌ Teacher Question: If I run `my_dog = Dog()`, will it work?

**No, it will not work.** The code will crash immediately with a `TypeError`.

---

### 🔍 What is Wrong With It?

The `Animal` parent class defines a strict contract using the `@abstractmethod` decorator for `make_sound()`. 

When the `Dog` class inherits from `Animal`, it is **forced** to implement its own version of `make_sound()`. Instead, the `Dog` class defines a completely new method (`wag_tail`) and completely ignores the required `make_sound` method.

### 🚨 The Python Error Message
When you try to run `my_dog = Dog()`, Python will block the creation of the object and throw this exact error:

```text
TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'make_sound'
```

### 🛠️ How to Fix It
To make the code legal, the `Dog` class must fulfill the blueprint contract by defining the missing method:

```python
class Dog(Animal):
    def make_sound(self):
        print("Bark! Bark!")  # Fulfills the abstract contract

    def wag_tail(self):
        print("Wagging!")
```