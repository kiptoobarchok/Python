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