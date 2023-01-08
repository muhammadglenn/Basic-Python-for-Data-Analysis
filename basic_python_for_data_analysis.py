## Arithmetic

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 3)
print(10 // 3)
print(10 ** 3)
print(2 + 3 * 5 ** 2)
print(((2 + 3) * 5) ** 2)
print(100 % 75)

import math
print(math.log(1000000))
print(math.sqrt(36))
print(math.log(100,10))
print(math.exp(10))

print(round(233.234))
print(round(233.234, 1))
print(round(233.234, -1))
print(math.floor(2.8))
print(math.ceil(2.2))


## Data Types

# Integer
print(type(12))
print(type(4 + 5))

# Float
print(type(6.0))
print(type(4/2))
print(type(1/3))
print(type(7.3))

# Convert Data Types
print(int(6.0))
print(float(8))

# Booleans
print(type(True))
print(type(False))
print(20 > 10)
print(20 < 10)
print(20 >= 20)
print(10 == 10)
print(40 == 40.0)
print(1 != 2)
print((2>1) and (10 > 11))
print((2>1) or (10 > 11))
print(bool(1))
print(bool(0))

# String
print(type("Jono"))
print(type('45'))


## Variables

x = 10
y = "INDONESIA"
z = 144**0.5 == 12

print(x)
print(y)
print(z)
print(x + z)

a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

p = y.lower()
print(p)


## List
"""A list is a mutable, ordered collection of objects"""
# Create a list
list_1 = ["Lesson", 5, True]
print(list_1)

# Create list from a string
list_2 = list("Life is Study")
print(list_2)

# Menambahkan 1 item dalam list
list_1.append("Singapore")
print(list_1)

# Menghapus item dalam list
list_1.remove("Lesson")
print(list_1)

# Menambahkan lebih dari 1 item dalam list
newlist = [45, 67, 3]
list_3 = list_1 + newlist
print(list_3)

num_list = [1, 5, 4, 2, 3, 6, 8]
print(len(num_list))                # Check the length
print(max(num_list))                # Check the max
print(min(num_list))                # Check the min
print(sum(num_list))                # Check the sum
print(sum(num_list)/len(num_list))  # Check the mean
print(num_list.count(3))            # Menghitung jumlah item dalam list

# Reverse List
num_list.reverse()
print(num_list)

# Sort List
num_list.sort()
print(num_list)


## Tuples
"""Tuples are an immutable sequence data type that are commonly used to hold short collections of related data."""
# Creat Tuple
tuple_1 = (2, 6, 4, 5, 8, 5, 9, 1)
print(tuple_1)
print(type(tuple_1))

# Convert list to tuple
list_cth = [2, 3, 1, 4]
tuple_2 = tuple(list_cth)
print(tuple_2)

# Index
print(tuple_1[6])

# Slice
print(tuple_1[2:4])

# Functions
print(len(tuple_1))
print(min(tuple_1))
print(max(tuple_1))
print(sum(tuple_1))

# Sort
print(sorted(tuple_1))


## String

# Create string variable
string_1 = "Hello World"
print(string_1)
print(type(string_1))

# Index
print(string_1[4])

# Slice
print(string_1[5:])     #Slice from teh fifth index to the end
print(string_1[::-1])   #Reverse the string

# Functions
print(len(string_1))
print(string_1.count("l"))  #Count the l's in the string
print(string_1.lower())     #Make all characters lowercase
print(string_1.upper())     #Make all characters uppercase
print(string_1.title())     #Make the first letter of each word up

# Find and Replace
print(string_1.find("H"))           #The original case exist
print(string_1.find("h"))           #Not original case, doesnt exist
print(string_1.replace("World",     #Substring to replace
                       "Friend"))   #New substring

# Split
print(string_1.split())     #Splits on spaces
print(string_1.split("l"))  #Split on "l" values

# Split
multiline_string = """I am
a multiline 
string!"""
print(multiline_string.splitlines())    #Join multiline string into 1 line

# Strip : leading and trailing characters from both ends of a string
extra_spaces = "    strip white space!   "
print(extra_spaces.strip())                 #removes whitespace
extra_x = ":BuyNOW:"
print(extra_x.strip(":"))                   #removes :

# Join Strings
print(" ".join(["Hello", "World!", "Join", "Me!"]))

name = "Joe"
age = 10
city = "Paris"
print(f"My name is {name} I am {age} and I live in {city}")


## Dictionaries
"""
Dictionaries are mutable, so you can add and remove keys and their associated values. 
A dictionary's keys must be immutable objects, such as ints, strings or tuples, 
but the values can be anything.
"""
# Create a dictionary
dict_1 = {"name": "Yon",
           "age": 18, 
           "city": "London"}
print(dict_1)

# Index
print(dict_1["name"])

# Add new items
dict_1["Height"] = "171 cm"
print(dict_1)

# Delete existing key: value pairs
del dict_1["Height"]
print(dict_1)

# Functions
print(len(dict_1))
print("name" in dict_1)
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

# Store multi data in a dictionary
my_table_dict = {"name": ["Joe", "Bob", "Harry"],
                 "age": [10,15,20] , 
                 "city": ["Paris", "New York", "Tokyo"]}
print(my_table_dict)

## Sets
"""
Sets are unordered, mutable collections of immutable objects that cannot contain duplicates. 
Sets are useful for storing and performing operations on data where each value is unique.
"""
# Create a set
my_set = {1,2,3,4,5,6,7}
print(type(my_set))

# Add items from a set
my_set.add(8)
print(my_set)

# Remove items from a set
my_set.remove(7)
print(my_set)

# Union
set1 = {1,3,5,6}
set2 = {1,2,3,4}
print(set1.union(set2))

# Intersection
print(set1.intersection(set2))

# Difference
print(set1.difference(set2))

## Numpy Arrays
"""Numpy implements a data structure called the N-dimensional array or ndarray"""

import numpy as np

# Convert a list to an ndarray
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(type(my_array))

# Create an array with more than one dimension
second_list = [5, 6, 7, 8, 9]
two_d_array = np.array([my_list, second_list])
print(two_d_array)

# Check the number and size of dimensions of an ndarray
print(two_d_array.shape)

# Check the total size (total number of items) in an array
print(two_d_array.size)

# Check the type of the data in an ndarray
print(two_d_array.dtype)

# Index
print(my_list[2])           #Get the item at index 2
print(two_d_array[1,2])     #Get the element at row index 1, column index 2

# Slice
print(my_list[2:])          #Get a slice from index 2 to the end
print(my_list[::-1])        #Slice backwards to reverse the array
print(two_d_array[1:, 2:])  #Slice elements starting at row 2, and column 3

# Math Operations
print(two_d_array + 100)
print(two_d_array - 100)
print(two_d_array * 4)
print(two_d_array ** 3)
print(two_d_array + two_d_array)
print(two_d_array - two_d_array)
print(two_d_array * two_d_array)
print(two_d_array * two_d_array)
print(np.mean(two_d_array))             #Mean of all the elements in an array
print(np.mean(two_d_array,
              axis = 1))                #Get means of each row
print(np.mean(two_d_array,
              axis = 0))                #Get means of each column
print(np.std(two_d_array))
print(np.sum(two_d_array))
print(np.log(two_d_array))              #Log of each element in an array
print(np.sqrt(two_d_array))             #Square root of each element