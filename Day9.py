# Exercise: day 9

# level 1
# No.1 comparing age for driving
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive")
elif age < 18:
    print("You need", 18-age, "more years to learn to drive")


# No.2 Comparing age
my_age = int(input("Enter My age: "))
your_age = int(input("Enter your age: "))
if my_age == your_age:
    print("We are exactly the same age")
else:
    if your_age > my_age:
        diff = your_age - my_age
        if diff == 1:
            print("You are 1 year older than me")
        else:
            print(f"You are {diff} years older than me")
    else:
        diff = my_age - your_age
        if diff == 1:
            print("You are 1 year younger than me")
        else:
            print(f"You are {diff} year younger than me")


# No.3 comparing any two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print("a is greater than b")
elif a <b:
    print("a is less than b")
else:
    print("a is equal to b")



# Level 2
# No.1 Calculating grade to students according to their scores:

score = int(input("Enter your obtained score: "))
if score <= 59:
    print("Try again your grade is F")
elif score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score <= 89:
    print("Your grade is B")
elif score >= 70 and score <= 79:
    print("Your grade is C")
elif score >= 60 and score <= 69:
    print("Your grade is D")
else:
    print("Invalid")

# No. 2 Finding season based on month

month = input("Enter the name of Month: ").strip().capitalize()
if month == 'September' or month == 'October' or month == 'November':
    print(f"{month} lies in Autumn")
elif month == 'December' or month == 'January' or month == 'February':
    print(f"{month} lies in Winter")
elif month == 'March' or month == 'April' or month == 'May':
    print(f"{month} lies in Spring")
elif month == 'June' or month == 'July' or month == 'August':
    print(f"{month} lies in Summer")
else:
    print("Invalid Input")

# No.3 Checking iteam in list and adding
fruits = ['banana', 'orange', 'mango', 'lemon']
a = input("Enter the name of fruit: ")
if a in fruits:
    print("These fruit is already in list")
else:
    fruits.append('apple')
    print(fruits)

# No.3 Modifying dictionary
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if skills in person:
    print(person(index))





