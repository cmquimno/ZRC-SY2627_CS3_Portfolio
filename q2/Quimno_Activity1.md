### What is/are the parent class(es) of the `Programmer` class in the video?

**Answer:** The direct parent class of the `Programmer` class as shown in the video is the `Employee` class. An indirect parent class of the `Programmer` class as shown in the video is the `Person` class, and it serves as the grandparent class for the `Programmer` class.

### If you were to add a new role called `Intern`, where would you place it in the inheritance hierarchy? Why?

**Answer:** I would place the `Intern` class as a child class of the `Employee` class. This is because an intern matches an "is-a" relationship with an employee (an Intern is an Employee). By placing it under the `Employee` class, the `Intern` class automatically inherits the attributes and methods that are already defined in the `Employee` and `Person` ancestries. The reason I did not put it under the other classes is that a general intern is an employee. Since the type of intern is unspecified, it belongs under the class it represents a type of.