my_set = set([1, 2, 3,])
print(type(my_set))
print(my_set)

other_set = {1, 2, 3}
print(type(other_set))
print(other_set)
# you get same exact answer from both:

# what can  you do with sets? it still gives 1 2 3 4 5 even it you have more of the same number
my_set = set([1, 2, 3, 4, 5, 1, 1, 1, 2, 2])
print(my_set)

# you can add tuples
my_set= set((1, 2, 3, 4, 5))
print(my_set)

my_set = set((1, 2, 3, 4, 5))
print(len(my_set))

# boolean
my_set = set((1, 2, 3, 4, 5))
print(2 in my_set)

# set joining
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)
# adding a number to our set
s1 = {1, 2, 3}
s1.add(4)
print(s1)

# remove
s1 = {1, 2, 3}
s1.remove(3)
print(s1)

# pop
s1 = {1, 2, 3}
draw =s1.pop()
print(draw)

# clear
s1 = {1, 2, 3}
s1.clear()
print(s1)

# practice :Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
# {"three", 4, 5}
my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)


# Remove a random item from the following set, using set methods.
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
draw = raffle.pop()
print(draw)

# Add the name Gunther to the following set, using set methods:
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle.add("Gunther")
print(raffle)