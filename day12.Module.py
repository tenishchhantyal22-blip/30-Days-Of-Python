#DAY12 module
#Module is the file contining set of codes, funtion and a single variable that can be used to an application

#Creating module
def generate_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name

#Importing module
import mymodule
print(mymodule.generate_full_name('Tenesh', 'Chhantyal'))

#Import function from a module:
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Tenesh', 'Chhantyl'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person['Firstname'])

#Import function from a module and rename
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname("Tenesh", "Chhantyal"))
print(total(1, 3))
mass = 23
weight = mass * g
print(weight)
print(p['Firstname'])

#Import built in module:
#There are a lot of built in module in python programming language such like other language, some popular built funtion
# are datetime, math, statistics, collection, random, os etc.

#eg. os is responsible for creating, changing, removing the directory
import os
os.mkdir('created.py')
os.rmdir('python.py')
os.getcwd()

#eg. sys provide variable and function to manipulate different parts of python runtime environment.
import sys
print('Welcome {}. enjoy {} challeng!'.format(sys.argv[1], sys.argv[2]))

#some important sys commands
sys.exit() # to exit sys
sys.maxsize # to know the largest variable integers it take
sys.path # to know environment path
sys.version #to know the version of python using

#Statistis module
#statistics module helps in calcualtion of statistical problem
from statistics import *
age = [12, 23, 23, 42, 23, 14, 24]
print(mean(age))
print(median(age))
print(mode(age))
print(stdev(age))

#mathematical module
import math
print(math.pi) # 3.14
print(math.sqrt(4)) # 2
print(math.pow(2, 3)) # 8
print(math.floor(9.81)) # 9
print(math.ceil(9.83)) # 10
print(math.log10(100)) # 2

# for specific value
from math import pi
print(pi)

# for multiple value at a single time
from math import pi, sqrt, pow, floor, ceil, log10
print(pi) # 3.14
print(sqrt(4)) # 2
print(pow(2, 3)) # 8
print(floor(9.81)) # 9
print(ceil(9.83)) # 10
print(log10(100)) # 2

# to import multiple module at a single time
from math import *
print(pi) # 3.14
print(sqrt(4)) # 2
print(pow(2, 3)) # 8
print(floor(9.81)) # 9
print(ceil(9.83)) # 10
print(log10(100)) # 2

#to rename
from math import pi as PI
print(PI)

#string module
#a string module is use in many purposes
print(string.ascii_letters) #abcdefghijklmnopqrstuvwxyz
print(string.digits) #123456789
print(string.punctuation) #!@#$%^&*()_+

#random module
#the random module has a lot of function but we use only random and randint
from random import random, randint
print(random()) # it doesn't take any arguments it return value between 0 and 0.9999
print(randint(2, 100)) # it returns a random number between 2 and 100

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs
# using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to
# be generated.
# print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
# print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

#Exercise Of DAY 12 Module
#QNA 1
import secrets
import string
import random

def generate_mixed_id():
    letters = string.ascii_leters
    digits = string.digits

    chosen_letters = [secrets.choice(letters) for _ in range(3)]
    chosen_digits = [secrets.choice(digits) for _ in range(3)]

    id_list = chosen_letters + chosen_digits
    random.shuffle(id_list)

    return ''.join(id_list)
print(generate_mixed_id())


# QNA 2
import string
import random
def user_id_gen_by_user():

    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the sencond number: "))

    char_pool = first_num + second_num

    for _ in range(second_num):
        generated_id = ''.join(random.choices(char_pool, k=first_num))
        print(generated_id)

user_id_gen_by_user()

#QNA 3
import random

def rgb_color_gen():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgf({r}, {g}, {b}"
print(rgb_color_gen())

#QNA 4


