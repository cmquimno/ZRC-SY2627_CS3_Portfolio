# Activity 2: Follow-Along Challenge

### The Blueprint Concept
**Question:** The narrator says you shouldn't be able to create a generic "Vehicle" object. Why is an Abstract Class called a "blueprint"?
**Your Answer:** An abstract class is called a "blueprint" because it defines a conceptual layout and a strict set of rules, but it does not represent a complete, functional object on its own. Just as you cannot live inside a blueprint of a house, you cannot instantiate a generic abstract class; it must be fully built out by concrete child classes first.

### The "Must-Have" Rule
**Question:** When we use the `@abstractmethod` decorator, what are we forcing the Child Classes to do?

* [ ] Change their variable names.
* [x] **Implement their own version of that specific method.**
* [ ] Delete the parent class.

### Safety First
**Question:** What happens if you try to create an object directly from an Abstract Class? (e.g., `my_car = Vehicle()`)
**Your Answer:** Python blocks the instantiation and throws a `TypeError`. It acts as an automatic safety guardrail, screaming that you cannot instantiate an abstract class without an implementation for its abstract methods.