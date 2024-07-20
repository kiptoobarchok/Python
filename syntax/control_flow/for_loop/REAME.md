# For Loop

```
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
```

## How it works

In this program, we are printing a sequence of numbers. We generate this sequence of numbers using the built-in range function.

What we do here is supply it two numbers and range returns a sequence of numbers starting from the first number and up to the second number. For example, range(1,5) gives the sequence [1, 2, 3, 4]. By default, range takes a step count of 1. If we supply a third number to range, then that becomes the step count. For example, range(1,5,2) gives [1,3]. Remember that the range extends up to the second number i.e. it does not include the second number.

Note that range() generates only one number at a time, if you want the full list of numbers, call list() on the range(), for example, list(range(5)) will result in [0, 1, 2, 3, 4]. Lists are explained in the data structures chapter.

The for loop then iterates over this range - for i in range(1,5) is equivalent to for i in [1, 2, 3, 4] which is like assigning each number (or object) in the sequence to i, one at a time, and then executing the block of statements for each value of i. In this case, we just print the value in the block of statements.

