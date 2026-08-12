age = int(input("Enter your age: "))
height = float(input("Enter you height "))
print('Your age is: ', age)
print('Your height is: ', height)
complex_number = 3 + 4j

# area of triangle
base = int(input("Enter base "))
height = int(input("Enter height "))
area_of_traingle = 0.5*base*height
print('The area of the triangle is ')

# perimeter of triangle
a = int(input('Enter the value of a' ))
b = int(input('Enter the value of b' ))
c = int(input('Enter the value of c' ))
perimeter_of_triangle = a+b+c
print("The perimeter of traingle", perimeter_of_triangle)

# area and perimeter of rectangle
length = float(input('Enter the value of length '))
width = float(input('Enter the value of width '))
area_of_rectangle = length*width
perimeter_of_rectangle = 2 * (length + width)
print('The area of rectangle is ', area_of_rectangle)
print('The perimeter of rectangle is ', perimeter_of_rectangle)

# Calculating the slope
x = float(input('Enter the value of x-intercept' ))
y = 2 * x - 2
m = 2 # (y = mx+c)
print('The slope is ', m)

# calculating slope of two different points
x2 = 6
y2 = 10
x1 = 2
y1 = 2
slope_m = (y2 - y1) / (x2 - x1)
print("The slope of line is ", slope_m)

# comparing slope of first and second
slope_m1 = 2
slope_m2 = 2
print(slope_m1 == slope_m2)

# Finding vlaue of x when y == 0
x = int(input("Enter the value of x"))
y = x**2 + 6 * x + 9
print("The value of y is ", y)


# comparing length of python and dragon
len_python = 'python'
len_dragon = 'dragon'
print(len(len_python))
print(len(len_dragon))
print(len(len_python) > len(len_dragon)) # False cause python == dragon
print(len(len_python) < len(len_dragon)) # False cause pytong == dragon
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'on' not in 'python')

# calculating value of length of python and convert it into float and string
len_python = 'python'
float_v = float(len_python)
int_v = int(float_v)
print(float_v)
print(int_v)

# Determining if the number is even or not
n = int(input("Enter the value of n "))
if n / 2 == 0;
print("The number is even number")
else:
print("The number is odd number")

#checking value
a = 7
b = 3
c = 7 // 3
print(c)
d = 2.7
e = int(d)
print('c' == 'e')

#checking '10' and 10
a = 10
b = '10'
print('a' == 'b')
x = '9.8'
c = int(float(x))
d = 10
print( 'c' == 'd')

# Calculating total payment
hours = int(input("Enter the number of hours "))
rate_per_hour = int(input("Enter the rate per hour "))
total_payment = hours * rate_per_hour
print("Your weekly earning ", total_payment)

# Calculating total second people lived
year = int(input("Enter your age "))
number_of_second = year * 365 * 24 * 60 * 60
print('You have live for', number_of_second, 'seconds')

# printing number in different lines
print('1 1 1 1 1 \n2 1 2 4 8 \n3 1 3 9 27 \n4 1 4 16 64 \n5 1 5 25 125')




