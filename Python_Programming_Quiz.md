#### 1. When do you use a list in place of tuple ? <br>

##### What are tuples ?
A tuple is a data structure in-built in Python to store data, similar to arrays. <br>
The syntax to declare a tuple is <br>
``` location = (28.99, 51.34)``` <br>
We use parenthesis `()` to declare a tuple <br>

In order to access a element, we use **indexing**. <br>
``` latitude, longitude = location[0], location[1]```

Tuples also make use of **slicing**
```
fruits = ("apple", "banana", "orange")
last_fruit = fruits[:-1]
```
Tuples can be deleted using the `del` command

##### What are lists ?
Similar to tuple, lists is another built-in data structure of Python to store data <br>
The synatx to declare a list is <br>
`breakfast = ["bread", "butter", "eggs"]`

Similar to tuples , list also supports **indexing and slicing**

##### Difference between tuple and lists ?
A list is mutable while a tuple is not. By mutabliity, I mean we can change the data stored inside the structure <br>

Everything in Python is a object. So when i declare a list<br>
`numbers = [1,2,3,4,5]` <br>
`numbers` is an object of the type `list` containing numbers 1 to 5 <br>
In case I want to change the second element of the lis to 6, I will do this <br>
`numbers[1] = 6` <br>
`numbers` will now contain `[1,6,3,4,5]`

Doing the same with a tuple will give me an error <br>
`TypeError: ‘tuple’ object does not support item assignment`

Suppose you want to delete a slice of the tuple, you will get the following error <br>
`TypeError: ‘tuple’ object does not support item deletion`

##### Functions and methods to use on both ?
Both the data structures support the following functions: <br> 
`len(), max(), min(), sum(), any(), all(), sorted()`

Common methods in list and tuple: `index(), count()` <br>
Methods in list: `append(), insert(), remove(), pop(), clear(), sort(), and reverse()`

#### 2. What is a ternary operator in Python ? <br>
#### 3. What are negative indices in Python ? <br>
#### 4. List some of the keywords in Python ? <br>
and | def | False | import | not | True
--- | --- | --- | --- | --- | ---
__as__ | __del__ | __finally__ | __in__ | __lambda__ | __try__
__assert__ | __elif__ | __for__ | __is__ | __nonlocal__ | __while__
__break__ | __else__ | __from__ | __None__ | __print__ | __with__
__class__ | __except__ | __global__ | __or__ | __return__ | __yield__
__continue__ | __exec__ | __if__ | __pass__ | __raise__ | 

#### 4. Which are some useful string methods in Python ? <br>
Methods | Description | 
--- | --- |
`tolower()` | Converts a string into lower case | 
`toupper()` | Converts a string into upper case |
`swapcase()` | Swaps cases, lower case becomes upper case and vice versa |
`islower()` | Returns True if all characters in the string are lower case | 
`isupper()` | Returns True if all characters in the string are upper case | 
`isalnum()` | Returns True if all characters in the string are alphanumeric |
`isalpha()` | Returns True if all characters in the string are in the alphabet | 
`isnumeric()` | Returns True if all characters in the string are numeric | 
`capitalize()` | Converts the first character to upper case | 
`startswith()` | Returns true if the string starts with the specified value | 
`endswith()` | Returs true if the string ends with the specified value |
`replace()` | Returns a string where a specified value is replaced with a specified value | 
`split()` | Splits the string at the specified separator, and returns a list |
`splitlines()` | Splits the string at line breaks and returns a list |
`join()`  | Joins the elements of an iterable to the end of the string |
`strip()` | Returns a trim version of the string |
`lstrip()` | Returns a left trim version of the string |
`rstrip()` | Returns a right trim version of the string |
`count()` | Returns the number of times a specified value occurs in a string | 
`find()` | Searches the string for a specified value and returns the position of where it was found | 

#### 5. Although Python is riding the hype wave pretty well since its high usage in fields of AI , what are some of the pitfalls of Python as a language? <br>
1. __Speed:__ Python is __slower__ than C or C++. But of course, Python is a high-level language, unlike C or C++ it's not closer to hardware.

2. __Mobile Development:__ Python is not a very good language for __mobile development__ . It is seen as a weak language for mobile computing. 

3. __Memory Consumption:__ Python is not a good choice for __memory intensive__ tasks. Due to the flexibility of the data-types, Python's memory consumption is also __high__.

4. __Database Access:__ Python has limitations with __database access__ . As compared to the popular technologies like JDBC and ODBC, the Python's database access layer is found to be bit underdeveloped and primitive .

5. __Runtime Errors:__ Python programmers cited several issues with the __design__ of the language. Because the language is __dynamically typed__ , it requires more testing and has errors that only show up at __runtime__ .

#### 6. What are the benefits of Python ? <br>
- Beginner's Language : 
- Simple and Easy to Learn
- Interpreted Language
- Cross-platform language
- Free and Open Source
- Object-Oriented language
- Extensive Libraries
- Integration with other languages
- Databases Connectivity interfaces to all commercial databases

#### 6. How do you remove a duplicate from a Python list ? <br>
Convert the `list()` to `set()`

#### 7. What is the life cycle of a thread in Python ? <br>
A Thread is defined in computer science as the smallest unit that can be scheduled in an operating system

- To create a thread, we create a class that we make override the `run` method of the thread class. Then, we instantiate it.
- A thread that we just created is in the new state. When we make a call to `start()` on it, it forwards the threads for scheduling. These are in the ready state.
- When execution begins, the thread is in the running state.
- Calls to methods like `sleep()` and `wait()` make a thread wait. Such a thread is in the waiting/blocked state.
- When a thread is done waiting or executing, other waiting threads are sent for scheduling.
- A running thread that is done executing terminates and is in the dead state

![Life cycle of a thread](https://www.tutorialspoint.com/java/images/Thread_Life_Cycle.jpg)

#### 7. What is the `dict()` data structure in Python ? <br>
It is best to think of a dictionary as a __set of key: value pairs__, with the requirement that the __keys are unique (within one dictionary)__. <br>

A pair of braces creates an empty dictionary. Something like this <br>
`empty_dic = {}` <br>

Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary <br>
`student = {'name': "Narendra", 'class': "Junior", 'dob': "2002-01-03"}` <br>

Dictionaries are sometimes found in other languages as __associative memories__ or __associative arrays__. <br> 
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by __keys__, which can be any __immutable type__ <br> 
`strings` and `numbers` can always be keys

#### 8. Which are the assignment operators in Python ? <br>
Operator | Description | 
--- | --- |
`=` | Assign |
`+=` | Add and Assign |
`-=` | Subtract and Assign |
`*=` | Multiply and Assign |
`/=` | Divide and Assign |
`%=` | Modulus and Assign |
`**=` | Exponent and Assign |
`//=` | Floor Divide and Assign |

#### 9. What is recursion ? <br>
When a function makes a call to itself, it is termed recursion.<br>
But then, in order for it to avoid forming an infinite loop, we must have a base condition.<br>

Let’s take an example. <br>
```
def facto(n):
  if n==1:
    return 1
return n*facto(n-1)

facto(4)    # This will compute 4x3x2x1 = 24
```

#### 10.What does the function `zip()` do? <br>
The `zip()` function returns a `zip` object, which is an **iterator of tuples** where the first item in each passed iterator is **paired together**, and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

zip can also work with **lists**

__Syntax:__ `zip(iterator1, iterator2, iterator3 ...) -> zip object`

```
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x))
# prints (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

```
#### 11. Given the first and last names of all employees in your firm, what data type will you use to store it?

#### 12.What does the function `range()` do? <br>
The range() function is used to generate a sequence of numbers over time. <br>
At its simplest, it accepts an integer and returns a `range` object (a type of iterable) <br>

__Syntax:__ `range([start,] stop [, step]) -> range object`

Paramter | Description | 
--- | --- |
`start`(optional) |  Starting point of the sequence. It defaults to 0. |
`stop` (required) | Endpoint of the sequence. This item will not be included in the sequence. |
`step` (optional) | Step size of the sequence. It defaults to `1`.|

```
>>>
>>> range(5, 10)
range(5, 10)
>>> 
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>>
```

When `range()` is called with a single argument it generates a sequence of numbers from `0` upto the argument specified __(but not including it)__. That's why the number `5` is not included in the sequence.

Here the `range()` function is called with a `step` argument of `3`, so it will return __every third element__ from `1` to `20` (off course not including 20).

```
>>> 
>>> range(1, 20, 3)
range(1, 20, 3)
>>> 
>>> 
>>> list(range(1, 20, 3))
[1, 4, 7, 10, 13, 16, 19]
>>>
```

You can also use the step argument to count backwards. `step` becomes a negative number in that case

```
>>> 
>>> list(range(20, 10, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> 
>>> list(range(20, 10, -5))
[20, 15]
>>>
```

#### 13. How can you declare multiple assignments in one statement?

This is one of the most asked interview questions for Python freshers<br>
There are two ways to do this:

__First:__ This assigns 3, 4, and 5 to a, b, and c respectively <br>
` >>> a,b,c=3,4,5`  <br>   
__Second:__  Ths assigns 3 to a, b, and c <br>
`>>> a=b=c=3`<br>

#### 14. What is the `with` keyword in Python?
The `with` statement in Python ensures that cleanup code is executed when working with unmanaged resources by encapsulating common preparation and cleanup tasks. <br>
- It may be used to open a file, do something, and then __automatically close the file at the end.__
- It may be used to open a database connection, do some processing, then __automatically close the connection to ensure resources are closed and available for others__. 

`with` will __cleanup the resources even if an exception is thrown__

#### 15. What is the `PYTHONPATH` variable?
`PYTHONPATH` is the variable that tells the __interpreter where to locate the module files imported into a program__.<br>
Hence, it must include the Python source library directory and the directories containing Python source code. <br>
You can manually set PYTHONPATH, but usually, the Python installer will preset it.

#### 16. Can you do functional programming (FP) in Python ? If yes, then list the commonly used functions to enforce FP in Python. 

Function | Description | 
--- | --- |
`filter()` |  Filter lets us filter in some values based on conditional logic. |  
`map()` | Map applies a function to every element in an iterable. |
`reduce()` | Reduce repeatedly reduces a sequence pair-wise until we reach a single value. |

#### filter()
```
>>> list(filter(lambda x:x>5,range(8)))
# range(8) -> [0,1,2,3,4,5,6,7]
# now filter all numbers greater than 5
[6, 7]
```
#### map()
```
>>> list(map(lambda x:x**2,range(8)))
# range(8) -> [0,1,2,3,4,5,6,7]
# now map will apply function x -> x**2 to all numbers from 0 to 7
[0, 1, 4, 9, 16, 25, 36, 49]
```
#### reduce()
```
>>> from functools import reduce
>>> reduce(lambda x,y:x-y,[1,2,3,4,5])
# step 1 : [-1,3,4,5]
# step 2 : [-4,4,5]
# step 3 : [-8,5]
-13
```

#### 17. Differentiate between the `append()` and `extend()` methods of a list.

`append()` __adds an element__ to the end of the list <br> 
`extend` __adds another list__ to the end of a list.

```
>>> list1, list2 = [1, 2, 3], [5, 6, 7, 8]

# This is how append() works:

>>> list1.append(4)
>>> list1
[1, 2, 3, 4]

And this is how extend() works:

>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8]
```

#### 16. Explain `try`, `raise` and `finally`.

These are the keywords we use with __exception-handling__.<br> 
- We put risky code under a `try` block 
- Use the `raise` statement to __explicitly raise an error__ 
- Use the `finally` block to put code that __we want to execute anyway__.

```
>>> try:
        print(1/0)
except ValueError:
        print("This is a value error")
finally:
        print("This will print no matter what.")
        
# OUTPUT:
# This will print no matter what.
```
Because in the try block we got a __DivisionByZeroException__ and not ValueError, so that is not caught and `finally` block is executed.

#### 17. What is the `enumerate()` function in Python?
`enumerate()` iterates through a sequence and __extracts the index position and its corresponding value__ too.

```
>>> for i,v in enumerate(['Python','C++','Scala']):
        print(i,v)
# OUTPUT:
# 0 Python
# 1 C++
# 2 Scala
```
#### 18. Evaluate the output of the last line in the following code snippet.
```
>>> A0= dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
>>> A1= range(10)
>>> A2= sorted([i for i in A1 if i in A0])
>>> A3= sorted([A0[s] for s in A0])
>>> A4= [i for i in A1 if i in A3]
>>> A5= {i:i*i for i in A1}
>>> A6= [[i,i*i] for i in A1]
>>> A0,A1,A2,A3,A4,A5,A6
```

#### 19. Implement a switch case function using Python.

#### 20. Write a program in Python to count the number of capital letter in a file.

```
import os

dir_path = "C:\Users\1090\"
filename = "blob.txt"

# change working directory to dir_path
os.chdir(dir_path)

# open the file
with open(filename) as f:
  cap_count = 0
  # read all characters of the file
  for char in f.read():
    if char.isupper():
      cap_count += 1

print(cap_count)
    for word in 
```

#### 21. If you installed a module with pip but it doesn’t import in your IDLE, what could it possibly be?

#### 22. If while installing a package with pip, you get the error No matching installation found, what can you do?

#### 23. What is the difference between a Python module and a Python library?

#### 24. Explain memory management in Python. (Optional: for CS Students)
Python manages objects by using __reference counting__. <br>
This means that the memory manager keeps track of the number of references to each object in the program.<br>
When an object's reference count drops to __zero__, which means the object is no longer being used, __the garbage collector (part of the memory manager) automatically frees the memory from that particular object.__

The user need not to worry about memory management as __the process of allocation and de-allocation of memory is fully automatic__. The reclaimed memory can be used by other objects.


#### 25. What are lambda expressions in Python ?
A lambda function is a small anonymous function.<br>
A lambda function can take any number of arguments, but can only have one expression.<br>
__Syntax:__  `lambda arguments : expression`

```
A lambda function that adds 10 to the number passed in as an argument, and print the result:

x = lambda a : a + 10
print(x(5))
# prints 15
```

- Lambda functions can take any number of arguments

```
A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))
# prints 30
```
- The power of lambda is better shown when you use them as an __anonymous function inside another function.__

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

```
def myfunc(n):
  return lambda a : a * n
```

Use that function definition to make a function that always doubles the number you send in

```
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
# prints 22
```
Note: __Use lambda functions when an anonymous function is required for a short period of time__

#### 26. What are generators in Python ?

#### 27. What are iterators in Python ?

#### 28. What is the difference between an iterator and a generator ?

#### 29. What do you know about palindromes? Can you implement one in Python?

A palindrome is a phrase, a word, or a sequence that reads the same forward and backward. <br> 
One such example will be _pip_ An example of such a phrase will be _‘nurses run’_.

__Normal Function Implementation:__

```
def isPalindrome(string):
  left, right = 0, len(string)-1
  while right >= left:
  if not string[left] == string[right]:
    return False
  left+=1;right-=1
  return True

isPalindrome('redrum murder')
# returns True

isPalindrome('CC.')
# returns False
```

__Iterator Implementation:__

```
def isPalindrome(string):
  left, right = iter(string), iter(string[::-1])
  i=0
  while i < len(string)/2:
    if next(left) != next(right):
      return False
    i+=1
    return True
    
isPalindrome('redrum murder')
# prints True

isPalindrome('CC.')
# prints False

isPalindrome('CCC.')
# prints False

isPalindrome('CCC')
# prints True
```

#### 30. What do you mean by `*args` and `**kwargs`?

In cases when we don’t know how many arguments will be passed to a function, like when we want to pass a list or a tuple of values, we use `*args`.
```
def func(*args):
  for i in args:
    print(i)
       

func(3,2,1,4,7)
3
2
1
4
7
```

`**kwargs` takes keyword arguments when we don’t know how many there will be.

```
def func(**kwargs):
  for i in kwargs:
    print(i,kwargs[i])


func(a=1,b=2,c=7)
a.1
b.2
c.7
```

#### 31. How will you find, in a string, the first word that rhymes with ‘cake’?

For our purpose, we will use the `search()` function, and then use `group()` to get the output.

`search()` will scan through a string, looking for any location where this `re` matches. It returns __None__ if no match is found. <br>
__Syntax:__  `search(pattern, string)`<br>

`group()` will return the match found in `search()`. Defaults to first match<br>
__Syntax:__  `group(index)`
`# group() and group(0) will give the same output` <br>
In case there are multiple matches found, they can be retrieved using `group(index)` where __index__ starts from `0` <br>
To access all the matches as a tuple, use `groups()` function.

`.` is a wild card which will __match any character except newline__

```
>>> import re
>>> rhyme=re.search('.ake','I would make a cake, but I hate to bake')
>>> rhyme.group()
‘make’
```

#### 32. Write a regular expression that will accept an email id. Use the re module.

`.` is a wild card which will __match any character except newline__ <br>
`[0-9a-zA-Z]+`	Any character of character class `0-9` or `a-z` or `A-Z` any number of times <br>
`\` is used to escape a special character, in this case `.` <br>
`()` is used to specify a group and `|` stands for __or__ <br>
`$` is end of the string <br>

Reference: [Regular Expressions Cheat Sheet](debuggex.com/cheatsheet/regex/python)

```
>>> import re
>>> e=re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','abc@gmail.com')
>>> e.group()
‘abc@gmail.com’
```
