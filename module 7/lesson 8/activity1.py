# Empty tuple
my_tuple = ()
print(my_tuple)

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuples = (1, "hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse",[8, 4, 6], (1, 2, 3))
print(my_tuple)

# Accessing tuple element using indexing
my_tuple = ('p', 'e', 'r', 'm', 'l', 't')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple
n_tuple = ("mouse",[8,4,6], (1, 2, 3))

# slicing
print("sliced:", my_tuple[1:4])

# iterating through tuple
for letter in(my_tuple):
    print("hello", letter)
