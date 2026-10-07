# Activity 2 Reflection: @property Decorator

Using the `@property` decorator makes code much easier to read and write compared to traditional getter and setter methods.

It allows you to access and update private attributes using simple variable notation (like `rectangle.width = 5`) instead of calling functions with parentheses like `rectangle.set_width(5)`. Even though the code looks simple on the outside, Python still runs the getter and setter methods behind the scenes. This keeps the private data protected and ensures validation rules are enforced without making the code messy.