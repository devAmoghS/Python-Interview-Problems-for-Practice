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
1. __Speed__ Python is __slower__ than C or C++. But of course, Python is a high-level language, unlike C or C++ it's not closer to hardware.

2. __Mobile Development__ Python is not a very good language for __mobile development__ . It is seen as a weak language for mobile computing. 

3. __Memory Consumption__ Python is not a good choice for __memory intensive__ tasks. Due to the flexibility of the data-types, Python's memory consumption is also __high__.

4. __Database Access__ Python has limitations with __database access__ . As compared to the popular technologies like JDBC and ODBC, the Python's database access layer is found to be bit underdeveloped and primitive .

5. __Runtime Errors__ Python programmers cited several issues with the __design__ of the language. Because the language is __dynamically typed__ , it requires more testing and has errors that only show up at __runtime__ .
