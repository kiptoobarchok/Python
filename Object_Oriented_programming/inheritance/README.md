# Inheritance

Inheritance allows programmers to create classes that are built upon existing classes, and this enables a class created through inheritance to inherit the attributes and methods of the parent class.


> Python not only supports inheritance but multiple inheritance as well.


This allows for code reusability.

Syntax for definition of a class is as follows:
```
class DerivedClassName(BaseClassName):
    pass
```

The name BaseClassName must be defined in a scope containing the derived class definition


To keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function:

```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```


Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent:

```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

note:
>When using the parent's class name to call it's init function then we
>must pass `self` unlike when using the **super()** function