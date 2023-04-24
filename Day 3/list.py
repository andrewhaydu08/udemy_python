my_list = ["a", "b", "c"]
print(type(my_list))

# length of a list
my_list = ["a", "b", "c"]
result = len(my_list)
print(result)

# index a list
my_list = ["a", "b",  "c"]
result = my_list[0]
print(result)

my_list = ["a", "b",  "c"]
result = my_list[0:2]
print(result)

my_list = ["a", "b",  "c"]
result = my_list[0:1]
print(result)

# concatenation of list
my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
print(my_list + my_list2)

my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
print(my_list3)

my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3[0] = 'alpha'
print(my_list3)

my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3.append('g')
print(my_list3)

my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3.append('g')
my_list3.pop()
print(my_list3)

# pop deletes the last element
my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3.pop()
print(my_list3)

my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
my_list3.pop(0)
print(my_list3)

# you can store you variable also
my_list = ["a", "b",  "c"]
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
deleted = my_list3.pop(0)
print(my_list3)
print(deleted)

# sorting of list
list1 = ['g', 'o', 'b', 'm', 'c']
list1.sort()
print(list1)

# reverse
list1 = ['g', 'o', 'b', 'm', 'c']
list1.sort()
list1.reverse()
print(list1)

# practice: create a list with 5 elements inside the variable my_list. you can use strings booleans, numbers etc
my_list = ['a', 6, 'g', -1, 5]
result = my_list
print(result)

# add the element "motorcycle" to thr following list of the means of transportation:
transportation_means = ["plane", "car", "ship", "bicycle"]
transportation_means.append("motorcycle")
print(transportation_means)

# use the pop() method to remove the third item from the following list called fruits.
fruits = ["apple", "banana", "mango", "cherry", "watermelon"]
fruits.pop(2)
deleted = fruits.pop(2)
print(fruits)
print(deleted)




