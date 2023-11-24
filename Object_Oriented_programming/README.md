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