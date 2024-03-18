# print function immediately followed by ()
# in the parentheses, we need the thing we're printing
print("Hello World")
print("They're taking the hobbits to Isengard")


# saving a string to a variable and printing that variable
my_string_in_a_variable = "Hello World, Again!"
print(my_string_in_a_variable)
# you can use anythign as a variable as long as it adheres to the naming rules
potato = "Ryan"
potatos = "Ryan and Craig" 
# They should be relevant to the data you're setting
my_name = "Ryan"
our_names = "Ryan and Craig"

# renaming variables
my_dog = "Eyo"
# print(my_dog)
my_dog = "Peaches"
print(my_dog)

# Numbers
# Integers or Whole Numbers
print(3)
x = 3
print(x)
# Floats or Decimals
print(3.33)
y = 3.33
print(y)

# reassignign my x varaible
x = 100
print(x)

# addition
strawberries = 10
blueberries = 15
# 25    =         10         +      15 
mixed_fruit = strawberries + blueberries
print(mixed_fruit)
# adding more fruits to the fruit salad yummy yummy
bananas = 20
#  25       =    25       +   20     
mixed_fruit = mixed_fruit + bananas
print(mixed_fruit)
# addition shorthand
# mixed_fruit += bananas
# print(mixed_fruit)

# Subtraction
initial_cheese_slices = 5
cheese_stolen = 2
#   3        =         5             -      2
cheese_left = initial_cheese_slices - cheese_stolen
print(cheese_left)

# multiplication
slices_per_person = 2
party_guests = 5 
# 10                =    2              *     5
total_slices_needed = slices_per_person * party_guests
print(total_slices_needed)

# division
pie_pieces = 8
people_at_table = 4
# 2.0          =    8       /      4
pie_per_person = pie_pieces / people_at_table
print(pie_per_person)

# answer = 10 / 2

# Modulo %
# returns the remainder of a division problem
remainder = 5 % 2
print(remainder)
is_even = 4 % 2
print(is_even)

cookies = 14
cookies_per_jar = 5
leftover_cookies = cookies % cookies_per_jar
print(leftover_cookies)

# Floor Division //
total_sandwiches = 7
people = 3
sandwiches_each = total_sandwiches // people
print(sandwiches_each)

# Exponentiation **
tea_strength = 3
cups_of_tea = tea_strength ** 2
print(cups_of_tea)

# Boolean Comparison Operators
# == is this equal to that
num1 = 5
num2 = 5
# num1 == num2 --> True
# < less than
num3 = 10
num4 = 15
# num3 < num4 --> True
# != not equal - opposite of double equal
num5 = 12
num6 = 8
# num5 != num6
# print(num5!=num6)

#less than or equal to
# <=
num7 = 10
num8 = 20
num9 = 20
# num7 <= num9 --> True
# num8 <= num9 --> True
# print(num7<=num9)

# Greater than or equal
# >=
num10 = 30
num11 = 25
num12 = 25
# print(num10>=num11)
# num10 >= num11 --> True
# num12 >= num11 --> True

# Indentation
# we have something here
#     we have something here
#         we have somethign here
# this happens
    # this happens
#       then this happens
# then this happens

if 5 > 2: #colon denote the end of a line of code
    print("Five is greater than two!")
# several nested conditions with hella indentation
if 5 > 2:
    if 6 < 10: #new block
        if 7 >3: #new block
            if 121 > 120: #new block
                print("ALL THESE THINGS ARE TRUE!")

# Common Whitespace Errors
# Always check your indentation
# indentation inconsistency example
if True:
    print("This looks fine")
    print("Oh no, a tab sneaked in!")
            
print("All is Well")
    # print("Oh no what am i doing here, what is my purpose? who am i?") UNEXPECTED INDENT

# Expected Indent
# if True:
# print("I need to be indented please")

# Code Correction
weather = "Sunny"
if weather == "sunny":
    print("Wear Sunglasses")
else:
    print("Take an umbrella")

mood = "excited"

excited = "excited"
mood = excited

if mood == "excited":
    print("Yay! Lets have fun!")
else:
    print("I am sad")

# this is a comment
    
print("# <-- this is not a comment")
# print("Hello from a comment")
#docstring
a = """
I can type whatever I want it can be on many lines
 and it does not matter because I am using a docstring. 
 it might go off the page if i keep typing then i have to scrool 
 and no one can see my code
"""
print(a)

b = "Hello There! Thanks for doing\
    python stuff with me today. I hope\
        you're having a nice time"

print(b)

"""Instructions
1. Create a multi-line string using triple quotes. 
This string should be a small paragraph about your favorite hobby, passion, or a general thought.
2. Write a Python statement to perform a simple calculation, such as adding two numbers. 
Add a comment explaining the purpose of this statement.
"""

multi_line_quote = """This is a multi line string using the tripple quotes. I love watching movies, 
going to the gym, and long walks on the beach.
Sour patch kids are life!"""
print(multi_line_quote)
# Adding some stuff
num1 = 10
num2 = 25
total_num = num1 + num2
print(total_num)


my_favorite_hobby = '''
I like video games! I've been playing them
for a really long time, and I think they're
so fun! I wish I was playing them now!'''
print(my_favorite_hobby)




Anthony='''Hello my name is Anthony and 
and i just had a quesadilla for
lunch.'''
print(a)
pizza_slices=3
wings=8
lunch_items=pizza_slices + wings
print(lunch_items)

hobby = """ My favorite hobby and only thing I live and/
               breathe for is gaming, playing Valorant competitive./
                My general thoughts are, when am I gonna game. """
print(hobby)
#2. Write a Python statement to perform a simple calculation, such as adding two numbers. Add a comment explaining the purpose of this statement.
#adding the total of cats and dogs
cats = 10
dogs = 20
a = cats + dogs
print(a)


its_ja_boi = '''My hobby is music!
I play bass and sing in multiple bands but I first started learning on Acoustic Guitar.
My favorite genres to play are Rock and Roll, Blues, and Punk.'''
print(its_ja_boi)
a = 400
b = 19
c = a + b
print(c)

c = """
My current hobbies are 
playing video games, 
watching movies, tv shows,
learning about crypto,
and eating good food"""

print(c)

token_price = 1.5 # in dollars
amount_of_tokens = 100 # unit
total_price = token_price * amount_of_tokens
print(total_price)

mahrus = """ Hey coding temple crew. 
It's been a pleasure working with all of you. 
Feels like we've been through a lot together. 
I'm excited to see what the future holds for all of us."""
#This is a simple calculation to find the BMI of a person
weight = 150;
height = 66;
BMI = (weight / (height**2)) * 703;
print(BMI)
print(mahrus)
'''
Underweight: BMI less than 18.5
Normal weight: BMI 18.5–24.9
Overweight: BMI 25–29.9
Obese: BMI 30 or more
'''

a = """I have been playing pickleball for 8 years now. \
I really love the sport; it's a great workout but \
not nearly as exhausting as some other sports I've played. \
It's also much easier to learn than most other sports. \
Everyone should try pickleball!"""
print(a)
x = 90
y = 65
daily_high = x
daily_low = y
daily_temp_range = x - y
print(daily_temp_range)
 


my_hobbies = """At the moment my favorite hobbies include hanging out with
family, watching anime and reading new books. At the moment 
I am not reading anything, but always looking for recommendations.
"""
print(my_hobbies)

x = 2 + 2
print(x)
# this equation is meant to add the two numbers 
# and the print functions is there to calculate the numbers

nun_major = """Some of my hobbies are finding lil hotspots by the water
chilling with the family, just being outside on a good day,
now learning to code, and of course all things $$$$ ."""
print(nun_major)


my_hobby = """my favorite hobby when 
not working would be gaming.
Mainly first person shooters
as they test my reflexes and awareness level. my favs
would be call of duty or counter strike. Otherwise on weekends
i go to archery
"""
print(my_hobby)

general_thought =  """
During my time here at Coding Temple,\
 I've progressed from day one until now.\
   I intend on becoming better with each new skill we're taught. """
num35 = 35
num40 = 40
total_number = num35 + num40 
print(total_number)
# example addition


# case sensitivity
print("hello" == "Hello")
print("h" == "H")

# examples of case-sensitivity in variable names
class CoolCar():
    wheels = 4

cool_car = CoolCar()

# coffee case sensitivity
Coffee = "Strong Dark Roast"
coffee = "Light Cold Brew"

print("Welcome to the Python Coffee Cafe! We have Coffee and Pythons that drink Coffee")
print("\nIn Python: ")
print("'Coffee' holds: " + Coffee)
print("'coffee' holds: " + coffee)

# string concatenation
my_string = "Hello " + "There"
print(my_string)

# set multiple variables at a time
x,y, z = "apple", "banana", "cherry"
print(x, y, z)
print(x)
print(y)
print(z)

# Taking a user input
# user_input = input("Hello, please give me a string! ")
# print("You entered: ", user_input)

# user_name = input("What is your username? ")
# print("your user name is: ", user_name)

# amount = input("How many bagels would you like? ")
# bagel_price = 1.99
# print("Your total for bagels is: ", amount*bagel_price)

# Python Type Casting
silly_twelve = "12"
print(silly_twelve)
print(type(silly_twelve))
# changing a valid string to an int type using int()
regular_int = int(silly_twelve)
print(regular_int)
print(type(regular_int))

new_int = int("12")
print(type(new_int))

# amount = int(input("How many bagels would you like? "))
# bagel_price = 1.99
# print("Your total for bagels is: ", amount*bagel_price)
# str()
my_number = 63
print(type(my_number))

string_num = str(my_number)
print(type(string_num))

# float()
another_number = 6
print(type(another_number))
print(another_number)

new_float = float(another_number)
print(new_float)
print(type(new_float))

video_games = "git gud"

# games_int = int(video_games)


num1 = 10

num2 = 5

num1 = 5

num2 = 10

if num2 == 10:
    print("yay)")