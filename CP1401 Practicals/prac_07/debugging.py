"""CP1401 - Practical 7 - Debugging."""
def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity
    print(parity)

def calculate_parity(number):
    return (number%2)

# Problem(s) for program 1:
# the argument while function calling is not provided

# Fixed code for program 1:
def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity(number)
    print(parity)

def calculate_parity(number):
    return (number%2)


def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = input("How many: ")
    for i in numnums:
        print(i * 2)

# Problem(s) for program 2:
# the loop has to run in a particular range, so there is a logical error in the line for i in numnums
#Also the variable num should be an integer not a string so there is an error in the statement num =input('How many')

# Fixed code for program 2:
def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = int(input("How many: "))
    for i in range(numnums+1):
        print(i * 2)

def main_3():
    """Determine the area of a rectangle."""
    length ,width =12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(l, w):
    result = l * w
    print(result)

# Problem(s) for program 3:
# Variable initialisation is wrong for length and breadth
#Also there are is no return statement in calculate_area function

# Fixed code for program 3:
def main_3():
    """Determine the area of a rectangle."""
    length=12
    width =10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(l, w):
    result = l * w
    return(result)


def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    while age < 0 and age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {age} years old!")

# Problem(s) for program 4:
# and operator is used instead of or operator
#the age has not been incremented

# Fixed code for program 4:


def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    while age < 0 and age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    age+=increment
    print(f"In {increment} years, you will be {age} years old!")

# main_1()
# main_2()  # Note: these are not good names; just something to reduce the amount of copying we need to do
# main_3()
main_4()