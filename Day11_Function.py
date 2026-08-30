#Question no 2
def convert_celsius_to_fahrenheit(c):
    f = (c*9/3)+32
    return f
print(convert_celsius_to_fahrenheit(c))

# Question no 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback      
def add_all_nums(*numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        return "Error: All arguments must be numbers"
    return sum(numbers)
print(add_all_nums(1,2,3,4,5))

# Question no 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.strip().lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'
print(check_season('January'))
  
#Quesiton no 6 Write a function called calculate_slope which return the slope of a linear equation
  def calculate_slope(x1, y1, x2, y2):
    if x2-x1 == 0:
        return "Error: x2-x1 cannot be zero (vertical line )"
    slope = (y2-y1)/(x2-x1)
    return slope
print(calculate_slope(1,2,3,4))

# Question no 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif dicriminant == 0:
        x = -b/(2*a)
        return "one real solution: x = {x}".format(x)
    else:
        x1 = (-b + discriminant**0.2)/(2*a)
        x2 = (-b - discriminant**0.2)/(2*a)
        return "two real solution: x1 = '{x1}', x2 = '{x2}'".format(x1=x1, x2=x2)
print(solve_quadratic_eqn(1, -3, 2 ))

# Question no 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(input_list):
    for i in input_list:
        print(i)
    return input_list

# Creating the list outside the function
numbers = [1, 2, 3, 4, 5]

# Calling the function and printing its returned value
print("Returned:", print_list(numbers))

# Question no 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(input_list):
    input_list.reverse()
    for i in input_list:
        print(i)
    return input_list
array = [1, 2, 3, 4, 5]
letter = [A, B, C, D]
print("Returned:", reverse_list(array))
print("Returned:", reverse_list(letter))

#QNO 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(input_list):
    new_list = []
    for i in input_list:
        capitalize_item = i.capitalize()
        print(capitalize_item)
        input_list.append(capitalize_item)
    return new_list
array = ['a', 'b', 'c', 'd']
array1 = ['d', 'f', 'e', 's']
print(capitalize_list_items(array))
print(capitalize_list_items(array1))

#QNA 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list):
    input_list.append("Banana")
    return input_list
lst = ["Apple", "Mango", "Pineapple", "Orange",]
print(add_item(lst))


#QNA 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(input_list):
    del input_list[0]
    return input_list
lst = ["Apple", "Mango", "Pineapple", "Orange",]
print(remove_item(lst))

# QNA 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050

def sum_of_numbers(n):
    total = 0
    for num in range(n+1):
        total += num
    return(total)
print(sum_of_numbers(10))


# QNA 13 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    total = 0
    for num in range(1,n+1,2):
        total += num
    return(total)
print(sum_of_odds(10))

# QNA 14 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    total = 0
    for num in range(0,n+1,2):
        total += num
    return(total)
print(sum_of_even(10))

# Exercise Level: 2
# QNA 1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

def evens_and_odds(number):
    odd = 0
    even = 0
    for num in range(n+1):
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print(f"Total Number of even number '{even} and total number of odd number '{odd}' ")
print(evens_and_odds(100))
        
