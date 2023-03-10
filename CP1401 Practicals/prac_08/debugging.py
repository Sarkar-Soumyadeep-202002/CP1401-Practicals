"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")
#
# # Problem(s) for program 1:
# # The range function has incorrect parameters
# # The last block in the formatted string in the last print statement is incorrect
# # The 1st block in the formatted string in print statement inside the for loop is incorrect.
#
# # Fixed code for program 1:
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(0, len(names)):
    print(f"{i+1}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number-1]}")


# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# countries is a tuple and hence its elements cannot be modified.

# Fixed code for program 2:
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now
