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
```
      and	      def	      False	      import      not	      True
      as	      del	      finally	in	      or	      try
      assert	elif	      for	      is	      pass	      while
      break	      else	      from	      lambda	print	      with
      class	      except	global	None	      raise	      yield
      continue	exec	      if	      nonlocal	return
```

