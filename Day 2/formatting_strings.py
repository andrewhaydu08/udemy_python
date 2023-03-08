x = 10
y = 5
print("my numbers are " + str(x) +" and " + str(y))
"this is not practical but it works"

"use the format function next"
x = 10
y = 5
print("my numbers are {} and {}" .format(x,y))


x = 10
y = 5
print("the sum of {} and {} is equal to {}" .format(x,y, x+y))

"this is more efficient than the second one"
x = 10
y = 5
z = x + y
print("the sum of {} and {} is equal to {}" .format(y, x, z))

"a better way to do this is:"
color = "red"
license_plate = 54678
print(f"car color is {color} and its license plate is {license_plate}")

"strings formatting practice"
associate_name = "Jesse Pinkman"
associate_number = 39058
print(f"Dear {associate_name}, your associate number is : {associate_number}")

"tell the user the amount of points earned practice"
new_points = 350
total_points = 1225
print(f"You have earned {new_points} points! In total you have accumulated {total_points}")

"tell the user the amount od points earned plus the total"
previous_points = 875
new_points = 350
total_points = previous_points + new_points
print(f"This time the amount of points accumulated {total_points} will be equal to the {previous_points} plus the {new_points}")

