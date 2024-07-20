# 1. Object Oriented Programming

The principles for object-orientation are:
- Encapsulation
- Data Abstraction
- Polymorphism
- Inheritance

everything is a class in Python.
>Guido van Rossum has designed the language
>according to the principle "first-class everything".

Below is a simple definition of a class:
    
    class Robot:
        pass
    if  __name__ == "__main__":
        x = Robot()
        y = Robot()
        y2 = y
        print(y == y2)
        print(y == x)

The output is :

```
True
False
```

## 2. Class vs. Instance Attributes

Instance attributes are owned by the specific instances of a class. That is, for two different instances, the instance attributes are usually different

Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class. Therefore they have the same value for every instance. Class attributes are defined outside all the methods.

```
class A:
    a = "Class attribute"

    def method(self, name):
        self.name = name #instance attribute
    

x = A()
y = A()
x.a
```

In Python, you can override the value of a class attribute for a specific instance. However, it's important to note that doing so will only affect that specific instance, and the class attribute's original value will remain unchanged for other instances of the class.

## class methods
A class method is a method that is bound to the class and not the instance of the class. It takes the class itself as its first argument, conventionally named `cls`. Class methods are defined using the ***`@classmethod`*** decorator.

```
@classmethod
    def class_method(cls):
        print(f"This is a class method. Accessing class variable: {cls.class_variable}")
```

- They take the class itself as their first parameter, conventionally named `cls`.

- They have access to the class and its attributes but not to instance-specific data.

- They are bound to the class, meaning they can be called on the class itself or on an instance of the class.

## static methods
Like class methods they are not bound to instances
Class attributes can be either public , protected(_attr) or private(__attr). If the class attributes are private then we need a possibility to access and change these private class attributes.
We could use instance methods for this purpose:
```
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances(self):
        return Robot.__counter
```

- Static methods are defined using the `@staticmethod` decorator.
- They don't have access to the instance or the class itself as their first parameter.
- They are defined within a class, but they do not have access to the class or instance-specific data.
- They are not bound to a class or instance, and they behave like regular functions within the class namespace.