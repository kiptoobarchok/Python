# Python RegEx

A **RegEx**, or _Regular Expression_, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern

# Resources
[Regular Expressions](https://youtu.be/nxjwB8up2gI?si=SluB4bSbkdRmYT8T)

[Tutorial: Important Regular Expressions](https://medium.com/@anindyasdas/important-regular-expressions-def051aa7425)

[Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

[re — Regular expression operations¶](https://docs.python.org/3/library/re.html)

[CS50P-Lecture 7 - Regular Expressions](https://youtu.be/hy3sd9MOAcc?si=NdublVql4wf2lxb5)

## RegEx Module

Python has a built-in package called ***re***, which can be used to work with Regular Expressions.

### Import the re module:
    import re

# Metacharacters
Metacharacters are characters with a special meaning:
similar to * in wild card.
Here's a complete list of the metacharacters −
    . ^ $ * + ? { } [ ] \ | ( )

# Matching Vs Searching

Python offers two different primitive operations based on regular expressions :match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).

Example
    import re
    line = "Cats are smarter than dogs";
    matchObj = re.match( r'dogs', line, re.M|re.I)
    if matchObj:
        print ("match --> matchObj.group() : ", matchObj.group())
    else:
        print ("No match!!")
    searchObj = re.search( r'dogs', line, re.M|re.I)
    if searchObj:
        print ("search --> searchObj.group() : ", searchObj.group())
    else:
        print ("Nothing found!!")
