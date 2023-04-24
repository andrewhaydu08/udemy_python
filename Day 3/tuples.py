my_tuple = (1, 2, 3, 4)
print(type(my_tuple))

# you don't need the parenthesis for a tuple
my_tuple = 1, 2, 3, 4
print(type(my_tuple))

# query
my_tuple = (1, 2, 3, 4)
print(my_tuple[0])

# negative numbers right to left
my_tuple = (1, 2, 3, 4)
print(my_tuple[-1])

# tuples are immutable so you change them but you can create a new variable
my_tuple = (1, 2, (10, 20), 4)

print(my_tuple[2])

# select a certain index from the list
my_tuple = (1, 2, (10, 20), 4)

print(my_tuple[2][0])

# casting turn a tuple into a list etc.
my_tuple = (1, 2, (10, 20), 4)
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple = (1, 2, (10, 20), 4)
my_tuple = list(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))

# assign tuples to different variables
t = (1, 2, 3)
x, y, z = t
print(x, y, z)

# length
t = (1, 2, 3, 1)
print(len(t))

# methods
t = (1, 2, 3, 1)
print(t.count(1))

t = (1, 2, 3, 1)
print(t.index(2))
